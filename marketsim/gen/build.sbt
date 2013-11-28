name := "pygen"

version := "0.1"

resolvers ++= Seq(
    "Sonatype OSS Releases"  at "http://oss.sonatype.org/content/repositories/releases/",
    "Sonatype OSS Snapshots" at "http://oss.sonatype.org/content/repositories/snapshots/"
)

scalaVersion := "2.10.2"

libraryDependencies += "com.jsuereth" % "scala-arm_2.10" % "1.3"

libraryDependencies += "com.github.nikita-volkov" % "sext" % "0.2.3"

libraryDependencies ++= Seq(
    "com.chuusai" % "shapeless" % "2.0.0-M1" cross CrossVersion.full
    //  "com.chuusai" % "shapeless_2.10.2" % "2.0.0-M1" // alternatively ...
)

scalacOptions in ThisBuild ++= Seq("-feature", "-language:reflectiveCalls", "-language:implicitConversions")