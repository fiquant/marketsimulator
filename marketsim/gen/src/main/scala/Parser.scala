import scala.util.parsing.combinator._

/*
case class Memoize[A,B](f: A => B) extends (A => B) {
    private val cache = mutable.Map.empty[A, B]
    def apply(x: A) = cache getOrElseUpdate (x, f(x))
} */

class Parser() extends JavaTokenParsers with PackratParsers
{
    lazy val expr : Parser[Expr] = conditional | arithmetic

    lazy val conditional = ("if" ~> boolean) ~ ("then" ~> expr) ~ ("else" ~> expr) ^^ {
        case (cond ~ x ~ y) => IfThenElse(cond, x, y)
    } withFailureMessage "conditional expected"

    lazy val boolean : Parser[BooleanExpr] = boolean_factor ~ rep("or" ~ boolean_factor) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "or" ~ y) => Or(x, y)
        }
    } withFailureMessage "boolean expected"

    lazy val logic_op = (
                "<>" ^^ { _ => NotEqual() }
            |   "<=" ^^ { _ => LessEqual() }
            |   "<"  ^^ { _ => Less() }
            |   ">=" ^^ { _ => GreaterEqual() }
            |   ">"  ^^ { _ => Greater() }
            |   "="  ^^ { _ => Equal() }) withFailureMessage "comparison symbol expected"


    lazy val boolean_factor = boolean_term ~ rep("and" ~ boolean_term) ^^ {
        case op ~ list => list.foldLeft(op) {
            case (x, "and" ~ y) => And(x, y)
        }
    } withFailureMessage "boolean_factor expected"

    lazy val boolean_term = (expr ~ logic_op ~ expr ^^ { case (x ~ op ~ y) => Condition(op, x, y) }
                        | "not" ~> boolean ^^ { Not }
                        | "(" ~> boolean <~ ")" ) withFailureMessage "boolean_term expected"

    lazy val addsub_op = ("+" ^^ { _ => Add() } | "-" ^^ { _ => Sub() }) withFailureMessage "+ or - expected"
    lazy val muldiv_op = ("*" ^^ { _ => Mul() } | "/" ^^ { _ => Div() }) withFailureMessage "* or / expected"

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
                floatingPointNumber ^^ { s => Const(s.toDouble) }
            |   funcall
            |   ident ^^ { Var }
            |   "(" ~> expr <~ ")"
            |   "-" ~> term ^^ { Neg }) withFailureMessage "term expected"

    lazy val funcall = qualified_name ~ ("(" ~> repsep(expr, ",") <~ ")") ^^ {
        case name ~ list => FunCall(name, list)
    } withFailureMessage "funcall expected"

    lazy val parameter = rep(annotation) ~ ident ~ opt(":" ~> ident) ~ opt("=" ~> expr) ^^ {
        case (annotations ~ name ~ ty ~ initializer) => Parameter(name, ty, initializer, annotations)
    } withFailureMessage "parameter expected"

    lazy val function  = opt(docstring) ~ rep(annotation) ~ ("def" ~> ident) ~ ("(" ~> repsep(parameter, ",") <~ ")") ~ opt("=" ~> expr) ^^ {
        case (doc ~ annotations ~ name ~ parameters ~ body) => FunDef(name, parameters, body, doc, annotations)
    } withFailureMessage "function expected"

    lazy val definitions = rep(function)

    private def strip(s : String) = {
        def not_whitespace(ch : Char) = !ch.isWhitespace
        val begin = s.indexWhere(not_whitespace)
        val end = s.lastIndexWhere(not_whitespace)
        if (begin > 0 && end > 0) s.substring(begin, end+1) else ""
    }

    lazy val comment = "/\\*(?:.|[\\n\\r])*?\\*/".r ^^ {
        _ stripPrefix "/*" stripSuffix "*/" stripMargin '*'
    }

    lazy val docstring = comment ^^ { comment => {
            val idx = comment.indexOf("\r\n")
            if (idx > 0) {
                val brief = strip(comment.substring(0, idx))
                val detailed = comment.substring(idx + 2)
                DocString(brief, detailed)
            } else {
                DocString(comment, "")
            }
        }
    }

    lazy val string = stringLiteral ^^ { _ stripPrefix "\"" stripSuffix "\"" }

    lazy val qualified_name = rep1sep(ident, ".") ^^ { QualifiedName }

    lazy val annotation = ("@" ~> qualified_name) ~ opt("(" ~> repsep(string, ",") <~ ")") ^^ {
        case (name ~ parameters) => Annotation(name, parameters.getOrElse(List()))
    }
}

