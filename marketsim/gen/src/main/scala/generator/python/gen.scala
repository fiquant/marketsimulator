package generator.python

import java.io.File

object gen
{
    def apply(p : Typed.Package, dst_dir : String) { apply(p, new File(dst_dir)) }

    def apply(p : Typed.Package, dir : File)
    {
        if (!dir.exists()) {
            dir.mkdirs()
            if (!dir.exists())
                throw new Exception("cannot create directory " + dir.getName)
        }

        p.packages.values foreach { sub => apply(sub, new File(dir, sub.name) ) }
    }

}
