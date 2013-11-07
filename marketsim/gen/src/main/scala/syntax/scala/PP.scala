
package object PP {

    val crlf = "\r\n"

    trait Parameter extends AST.Parameter
    {
        override def toString = (annotations.map({ _ + " "}).mkString("")
                + name
                + (if (ty.nonEmpty) " : " + ty.get else "")
                + (if (initializer.nonEmpty) " = " + initializer.get else ""))
    }

    trait QualifiedName extends AST.QualifiedName
    {
        override def toString = names.mkString(".")
    }

    trait Annotation extends AST.Annotation
    {
        override def toString = "@" + name + "(" + parameters.map({ "\"" + _ + "\""}).mkString(", ") + ")"
    }

    trait DocString extends AST.DocString
    {
        override def toString = "/** " + brief + detailed.lines.map({ crlf + " *" + _ }).mkString("") + crlf + " */" + crlf
    }

    trait FunDef extends AST.FunDef
    {
        override def toString = (
                (if (docstring.nonEmpty) docstring.get else "")
                + annotations.map({_ + crlf}).mkString("")
                + "def " + name
                + "(" + parameters.mkString(", ") + ")"
                + (if (ret_type.nonEmpty) " : " + ret_type.get else "")
                + (if (body.nonEmpty) " = " + body.get else ""))
    }

    trait Definitions extends AST.Definitions {
        override def toString = definitions.map({_ + crlf + crlf}).mkString("")
    }
}
