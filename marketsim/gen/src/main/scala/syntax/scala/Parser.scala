package syntax.scala

import scala.util.parsing.combinator._
import AST._

class Parser() extends JavaTokenParsers with PackratParsers
{
    lazy val expr : Parser[Expr] =  boolean | conditional | castable | string_literal

    lazy val string_literal = string ^^ AST.StringLit

    lazy val float_literal = floatingPointNumber ^^ { s => { if (s contains ".") FloatLit(s.toDouble) else IntLit(s.toInt)}  }

    lazy val conditional = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
        case (cond ~ x ~ y) => IfThenElse(cond, x, y)
    } withFailureMessage "conditional expected"

    lazy val boolean : Parser[Expr] = boolean_factor ~ rep("or" ~ boolean_factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "or" ~ y) => Or(x, y)
        }
    } withFailureMessage "boolean expected"

    lazy val logic_op = (
                "<>" ^^^ NotEqual
            |   "<=" ^^^ LessEqual
            |   "<"  ^^^ Less
            |   ">=" ^^^ GreaterEqual
            |   ">"  ^^^ Greater
            |   "="  ^^^ Equal
            ) withFailureMessage "comparison symbol expected"


    lazy val boolean_factor = boolean_term ~ rep("and" ~ boolean_term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "and" ~ y) => And(x, y)
        }
    } withFailureMessage "boolean_factor expected"

    lazy val boolean_term = ((conditional | castable) ~ logic_op ~ expr ^^ { case (x ~ op ~ y) => Condition(op, x, y) }
                        | "not" ~> boolean ^^ Not
                        | "(" ~> boolean <~ ")" ) withFailureMessage "boolean_term expected"

    lazy val addsub_op = ("+" ^^^ Add | "-" ^^^ Sub) withFailureMessage "+ or - expected"

    lazy val muldiv_op = ("*" ^^^ Mul | "/" ^^^ Div) withFailureMessage "* or / expected"

    lazy val castable = arithmetic ~ opt(":" ~> typ) ^^ {
        case a ~ None    => a
        case a ~ Some(t) => Cast(a, t)
    }

    lazy val arithmetic = factor ~ rep(addsub_op ~ factor) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => BinOp(op, x, y)
        }
    } withFailureMessage "arithmetic expected"

    lazy val factor = term ~ rep(muldiv_op ~ term) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => BinOp(op, x, y)
        }
    } withFailureMessage "factor expected"

    lazy val term : Parser[Expr] = (
                float_literal
            |   funcall
            |   ident ^^ Var
            |   "(" ~> expr <~ ")"
            |   "-" ~> term ^^ Neg) withFailureMessage "term expected"

    lazy val funcall = qualified_name ~ ("(" ~> repsep(expr, ",") <~ ")") ^^ {
        case name ~ list => FunCall(name, list :: Nil)
    } withFailureMessage "funcall expected"

    lazy val typ : Parser[Type] = (
              typ2 ~ "=>" ~ typ ^^ {
                  case (x ~ "=>" ~  y) => FunctionType(x match {
                      case UnitType => Nil
                      case x : SimpleType => List(x)
                      case TupleType(types) => types
                      case x : FunctionType => List(x)
                  }, y)
              }
            | typ2) withFailureMessage "type expected"

    lazy val typ2 = (
            "(" ~> repsep(typ, ",") <~ ")" ^^ {
                case Nil => UnitType
                case x :: Nil => x
                case x => TupleType(x)
            }
            | (qualified_name ~ opt("[" ~> repsep(typ, ",") <~ "]")) ^^ {
                case (n ~ gen) => SimpleType(n, if (gen.isEmpty) Nil else gen.get)
            }) withFailureMessage "tuple or simple type expected"

    lazy val parameter = comment_lst ~ ident ~ opt(":" ~> typ) ~ opt("=" ~> expr) ^^ {
        case (c ~ name ~ ty ~ initializer) => Parameter(name, ty, initializer, c)
    } withFailureMessage "parameter expected"

    lazy val function_alias = ("def" ~> ident) ~ ("=" ~> qualified_name) ^^ {
        case (n ~ target) => FunAlias(n, target)
    }

    lazy val generics = opt("[" ~> rep1sep(ident, ",") <~ "]") ^^ {
        case Some(xs) => Generics(xs)
        case None     => Generics(Nil)
    }

    lazy val function  = (opt(docstring)
                        ~ rep(decorator)
                        ~ ("def" ~> ident)
                        ~ ("(" ~> repsep(parameter, ",") <~ ")")
                        ~ opt(func_type)
                        ~ opt("=" ~> expr)) ^^ {
        case (doc ~ decorators ~ name  ~ parameters ~ t ~ body) => FunDef(name, parameters, body, t, doc, decorators)
    } withFailureMessage "function expected"

    lazy val func_type = ("=>" ~> typ ^^ {
        case t => FunctionType(Nil, t)
    }) | (":" ~> typ)

    lazy val type_bases = ":" ~> repsep(typ, ",")

    lazy val type_declaration = "type" ~> ident ~ generics ~ opt(type_bases) ^^ {
        case (name ~ g ~ bases) => Interface(name, g, bases match { case None => Nil case Some(x) => x })
    }

    lazy val type_alias = "type" ~> ident ~ generics ~ ("=" ~> typ) ^^ {
        case (name ~ g ~target) => Alias(name, g, target)
    }

    lazy val package_body = ("{" ~> definitions <~ "}") | definitions

    lazy val `package` = rep(attribute) ~ ("package" ~> opt(qualified_name)) ~ package_body ^^ {
        case attributes ~ name ~ members => PackageDef(name, members, attributes)
    }

    lazy val definition = type_alias | type_declaration | function_alias | function | `package`

    lazy val definitions : Parser[AST.Definitions] = rep(definition) ^^ Definitions

    private def strip(s : String) = {
        def not_whitespace(ch : Char) = !ch.isWhitespace
        val begin = s.indexWhere(not_whitespace)
        val end = s.lastIndexWhere(not_whitespace)
        if (begin > 0 && end > 0) s.substring(begin, end+1) else ""
    }

    lazy val comment = "/\\*(?:.|[\\n\\r])*?\\*/".r ^^ {
        _ stripPrefix "/*" stripSuffix "*/" stripMargin '*'
    }

    lazy val comment_lst = opt(comment) ^^ {
        case Some(s) => s.lines.toList
        case None => Nil
    }

    private def strip_empty_tail(lst : List[String]) : List[String] = lst match {
        case Nil => Nil
        case hd :: Nil => {
            val s = strip(hd)
            if (s == "") Nil else s :: Nil
        }
        case hd :: tl => hd :: strip_empty_tail(tl)
    }

    private def strip_empty_lines(lst : List[String]) : List[String] = lst match {
        case Nil => Nil
        case hd :: tl => {
            val s = strip(hd)
            if (s == "") strip_empty_lines(tl) else s :: strip_empty_tail(tl)
        }
    }

    lazy val docstring = comment ^^ { comment => {
            val lines = comment.lines.toList
            if (lines.isEmpty) {
                DocString("", Nil)
            }  else {
                val hd :: tl = strip_empty_lines(lines)
                DocString(hd, tl)
            }
        }
    }

    lazy val string = stringLiteral ^^ { _ stripPrefix "\"" stripSuffix "\"" }

    lazy val qualified_name = opt(".") ~ rep1sep(ident, ".") ^^ {
        case (dot ~ names) => QualifiedName(if (dot.nonEmpty) "" :: names else names)
    }

    lazy val annotation = ("@" ~> qualified_name) ~ opt("(" ~> repsep(string, ",") <~ ")") ^^ {
        case (name ~ parameters) => Annotation(name, parameters.getOrElse(List()))
    }

    lazy val attribute = ("@" ~> ident) ~ ("=" ~> string) ^^ {
        case (name ~ value) => Attribute(name, value)
    }

    lazy val decorator =  attribute | annotation
}

