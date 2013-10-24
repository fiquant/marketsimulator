import os, sys
import targets
import subprocess

timestamp_filename = ".timestamp"

sourcedir   = os.path.abspath(os.path.dirname(__file__))
rootdir     = os.path.abspath(os.path.normpath(os.path.join(sourcedir, "..")))

def target(t):
    return os.path.join(rootdir, *getattr(targets, t))

def rel(f):
    return os.path.relpath(f, rootdir)

def write(t, strings):
    filename = target(t)
    print "\t", rel(filename)
    with open(filename, "w") as out:
        for d in strings:
            out.write(d)
            out.write('\n')

def generate_if_needed():            

    olddir = os.getcwd()
    os.chdir(os.path.dirname(__file__))

    if gen_needed():
        print " -> Regenerating..."
        
        for key in dir(targets):
            if key[0:2] != '__':
                module = getattr(targets, key)
                m = __import__('marketsim.gen.'+key, globals(), locals(), ['defs'], -1)
                write(key, m.defs)    
        print "done."

        print "Running scala generator..."

        subprocess.call("sbt run", shell=True)

        print "done."

        open(timestamp_filename, "w")

    os.chdir(olddir)

def gen_needed():

    exts = ['.py', '.scala']

    timestamp = 0

    if os.path.exists(timestamp_filename):
        timestamp = os.path.getmtime(timestamp_filename)

    changed_files = []

    def process_files(_, dirname, fs):
        if dirname == ".":
            for f in [".idea", "project", "target"]:
                fs.remove(f)
        for f in fs:
            if os.path.splitext(f)[1] in exts:
                full = os.path.join(dirname, f)
                if os.path.getmtime(full) > timestamp:
                    changed_files.append(full)
        print dirname

    os.path.walk(".", process_files, None)
    
    if changed_files:
        print "Changed files:"
        for f in changed_files:
            print "\t", f

    return  len(changed_files) > 0
