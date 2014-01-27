Syntax
======

.. code-block:: scala

    QualifiedName ::= Ident("." Ident)*

    Decorator ::= "@" (Annotation | Attribute)

    Annotation ::= QualifiedName "(" (Expr ("," Expr)*)? ")"

    Attribute ::= Ident "=" Expr

    PackageDef ::= Attribute* "abstract"? "package" QualifiedName? ("extends" QualifiedName)*
                        ("{" MemberDef* "}") | MemberDef*

    MemberDef ::= PackageDef | FunctionDef | TypeDef

    Type ::= UnitType | SimpleType | TupleType | FunctionType

    UnitType ::= "()"

    SimpleType ::= QualifiedName

    TupleType ::= "(" Type ("," Type)+ ")"

    FunctionType ::= Type "=>" Type

    TypeDef ::= TypeAliasDef | InterfaceDef

    GenericArgs ::= "[" Ident ("," Ident)* "]"

    TypeAliasDef ::= "type" Ident GenericArgs? "=" Type

    InterfaceDef ::= "type" Ident GenericArgs? (":" Type ("," Type)*)?

    Parameter ::= Ident (":" Type)? ("=" Expr)?

    FunctionDef ::= Decorator* "def" Ident "(" Parameter? ("," Parameter)* ")" (":" Type)? ("=" Expr)? | FunctionAlias

    FunctionAlias ::= "def" Ident "=" QualifiedName

    Expr ::= Expr ":" Type                                      // cast to a weaker type
           | "if" Expr "then" Expr "else" Expr                  // conditional
           | Expr ("+" | "-" | "*" | "/") Expr                  // aritmethic binary expression
           | "-" Expr                                           // unary minus
           | Expr ("and" | "or") Expr                           // logic binary expression
           | "not" Expr                                         // logic negation
           | Expr ("<" | "<=" | ">" | ">=" | "==" | "<>")  Expr // comparison expression
           | "(" Expr ")"
           | Expr "(" (Expr ("," Expr)*)? ")"                   // function application
           | QualifiedName                                      // reference to a name, local or global
           | FloatLiteral                                       // Float and Int literals
           | QuotedString                                       // String literal
