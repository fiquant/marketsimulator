import os, sys
import targets
import subprocess

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
    if gen_needed():
        print " -> Regenerating..."
        
        for key in dir(targets):
            if key[0:2] != '__':
                module = getattr(targets, key)
                m = __import__('marketsim.gen.'+key, globals(), locals(), ['defs'], -1)
                write(key, m.defs)    
        print "done." 

        print "Running scala generator..."

        olddir = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        subprocess.call("sbt run", shell=True)
        os.chdir(olddir)

        print "done."

def gen_needed():
    missing_targets = []
    changed_sources = []
    
    oldest_target_ts = sys.maxint
        
    for t in dir(targets):
        if t[0:2] != "__":
            trg = target(t)
            if not os.path.exists(trg):
                missing_targets.append(trg)
            else:
                oldest_target_ts = min(oldest_target_ts, os.path.getmtime(trg))
    
    for root, _, files in os.walk(sourcedir):
        for f in files:
            if os.path.splitext(f)[1] == ".py":
                fullpath = os.path.join(root, f)
                if os.path.getmtime(fullpath) > oldest_target_ts:
                    changed_sources.append(fullpath)
    
    if missing_targets != []:
        print "Missing targets:"
        for t in missing_targets:
            print "\t", rel(t)
            
    if changed_sources != []:
        print "Changed sources:"
        for t in changed_sources:
            print "\t", rel(t)
    
    return missing_targets != [] or changed_sources != []        
