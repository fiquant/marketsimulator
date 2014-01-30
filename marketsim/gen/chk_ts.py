import os, sys
import targets
import subprocess

timestamp_filename = ".timestamp"

sourcedir   = os.path.abspath(os.path.dirname(__file__))
rootdir     = os.path.abspath(os.path.normpath(os.path.join(sourcedir, "..")))

def generate_if_needed():

    olddir = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    if gen_needed():
        print "Running scala generator..."

        from marketsim import config
        sources = " ".join(config.sources)
        #subprocess.call("sbt clean", shell=True)
        subprocess.call("""sbt "run %s " """ % sources, shell=True)

        print "done."

        open(timestamp_filename, "w")

    os.chdir(olddir)

def gen_needed():

    exts = ['.py', '.scala','.sc']

    timestamp = 0

    if os.path.exists(timestamp_filename):
        timestamp = os.path.getmtime(timestamp_filename)

    changed_files = []

    def process_files(_, dirname, fs):
        if dirname == ".":
            for f in [".output", ".idea", "project", "target", "_out", "_intrinsic", ".parsed"]:
                if f in fs:
                    fs.remove(f)
        for f in fs:
            if os.path.splitext(f)[1] in exts:
                full = os.path.join(dirname, f)
                if os.path.getmtime(full) > timestamp:
                    changed_files.append(full)

    os.path.walk(".", process_files, None)
    
    if changed_files:
        print "Changed files:"
        for f in changed_files:
            print "\t", f

    return  len(changed_files) > 0
