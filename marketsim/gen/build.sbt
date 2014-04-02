name := "pygen"

version := "0.1"

scalaVersion := "2.10.2"

resolvers ++= Seq(
    "Sonatype OSS Releases"  at "http://oss.sonatype.org/content/repositories/releases/",
    "Sonatype OSS Snapshots" at "http://oss.sonatype.org/content/repositories/snapshots/"
)

libraryDependencies += "com.github.scopt" %% "scopt" % "3.2.0"

libraryDependencies += "com.jsuereth" % "scala-arm_2.10" % "1.3"

libraryDependencies += "com.github.nikita-volkov" % "sext" % "0.2.3"

scalacOptions in ThisBuild ++= Seq("-feature", "-language:reflectiveCalls", "-language:implicitConversions")
