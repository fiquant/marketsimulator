package syntax.scala

import scala.util.parsing.combinator._
import AST._
/*
case class Memoize[A,B](f: A => B) extends (A => B) {
    private val cache = mutable.Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
} */

class Parser() extends JavaTokenParsers with PackratParsers
{
    lazy val expr : Parser[Expr] = conditional | arithmetic

    lazy val conditional = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
        case (cond ~ x ~ y) => new IfThenElse(cond, x, y) with PP.IfThenElse
    } withFailureMessage "conditional expected"

    lazy val boolean : Parser[BooleanExpr] = boolean_factor ~ rep("or" ~ boolean_factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "or" ~ y) => Or(x, y)
        }
    } withFailureMessage "boolean expected"

    lazy val logic_op = (
                "<>" ^^ { _ => new NotEqual() with PP.NotEqual }
            |   "<=" ^^ { _ => new LessEqual() with PP.LessEqual }
            |   "<"  ^^ { _ => new Less() with PP.Less }
            |   ">=" ^^ { _ => new GreaterEqual() with PP.GreaterEqual }
            |   ">"  ^^ { _ => new Greater() with PP.Greater }
            |   "="  ^^ { _ => new Equal() with PP.Equal }
            ) withFailureMessage "comparison symbol expected"


    lazy val boolean_factor = boolean_term ~ rep("and" ~ boolean_term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "and" ~ y) => And(x, y)
        }
    } withFailureMessage "boolean_factor expected"

    lazy val boolean_term = (expr ~ logic_op ~ expr ^^ { case (x ~ op ~ y) => Condition(op, x, y) }
                        | "not" ~> boolean ^^ Not
                        | "(" ~> boolean <~ ")" ) withFailureMessage "boolean_term expected"

    lazy val addsub_op = ("+" ^^ { _ => new Add() with PP.Add }
                        | "-" ^^ { _ => new Sub() with PP.Sub }
                        ) withFailureMessage "+ or - expected"

    lazy val muldiv_op = ("*" ^^ { _ => new Mul() with PP.Mul }
                        | "/" ^^ { _ => new Div() with PP.Div}
                        ) withFailureMessage "* or / expected"

    lazy val arithmetic = factor ~ rep(addsub_op ~ factor) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => new BinOp(op, x, y) with PP.BinOp
        }
    } withFailureMessage "arithmetic expected"

    lazy val factor = term ~ rep(muldiv_op ~ term) ^^ {
        case start ~ list => list.foldLeft(start) {
            case (x, op ~ y) => new BinOp(op, x, y) with PP.BinOp
        }
    } withFailureMessage "factor expected"

    lazy val term : Parser[Expr] = (
                floatingPointNumber ^^ { s => new Const(s.toDouble) with PP.Const }
            |   funcall
            |   ident ^^ { new Var(_) with PP.Var }
            |   "(" ~> expr <~ ")"
            |   "-" ~> term ^^ { new Neg(_) with PP.Neg }) withFailureMessage "term expected"

    lazy val funcall = qualified_name ~ ("(" ~> repsep(expr, ",") <~ ")") ^^ {
        case name ~ list => new FunCall(name, list) with PP.FunCall
    } withFailureMessage "funcall expected"

    lazy val typ : Parser[Type] = (
              typ2 ~ "=>" ~ typ ^^ {
                  case (x ~ "=>" ~  y) => new FunctionType(x, y) with PP.FunctionType
              }
            | typ2) withFailureMessage "type expected"

    lazy val typ2 = (
            "(" ~> repsep(typ, ",") <~ ")" ^^ {
                case Nil => new UnitType() with PP.UnitType
                case x :: Nil => x
                case x => new TupleType(x) with PP.TupleType
            }
            | ident ^^ { new SimpleType(_) with PP.SimpleType }) withFailureMessage "tuple or simple type expected"

    lazy val parameter = rep(annotation) ~ ident ~ opt(":" ~> typ) ~ opt("=" ~> expr) ^^ {
        case (annotations ~ name ~ ty ~ initializer) => new Parameter(name, ty, initializer, annotations) with PP.Parameter
    } withFailureMessage "parameter expected"

    lazy val function  = (opt(docstring)
                        ~ rep(annotation)
                        ~ ("def" ~> ident)
                        ~ ("(" ~> repsep(parameter, ",") <~ ")")
                        ~ opt(":" ~> typ)
                        ~ opt("=" ~> expr)) ^^ {
        case (doc ~ annotations ~ name ~ parameters ~ t ~ body) => new FunDef(name, parameters, body, t, doc, annotations) with PP.FunDef
    } withFailureMessage "function expected"

    lazy val definitions = rep(function) ^^ { new Definitions(_) with PP.Definitions }

    private def strip(s : String) = {
        def not_whitespace(ch : Char) = !ch.isWhitespace
        val begin = s.indexWhere(not_whitespace)
        val end = s.lastIndexWhere(not_whitespace)
        if (begin > 0 && end > 0) s.substring(begin, end+1) else ""
    }

    lazy val comment = "/\\*(?:.|[\\n\\r])*?\\*/".r ^^ {
        _ stripPrefix "/*" stripSuffix "*/" stripMargin '*'
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
                new DocString("", "") with PP.DocString
            }  else {
                val hd :: tl = strip_empty_lines(lines)
                new DocString(hd, tl.mkString(crlf)) with PP.DocString
            }
        }
    }

    lazy val string = stringLiteral ^^ { _ stripPrefix "\"" stripSuffix "\"" }

    lazy val qualified_name = rep1sep(ident, ".") ^^ { new QualifiedName(_) with PP.QualifiedName }

    lazy val annotation = ("@" ~> qualified_name) ~ opt("(" ~> repsep(string, ",") <~ ")") ^^ {
        case (name ~ parameters) => new Annotation(name, parameters.getOrElse(List())) with PP.Annotation
    }
}

