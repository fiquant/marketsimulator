import os, sys
import targets

sourcedir   = os.path.dirname(__file__)
rootdir     = os.path.normpath(os.path.join(sourcedir, ".."))

def target(t):
    return os.path.join(rootdir, *getattr(targets, t))

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
            print "\t", t
            
    if changed_sources != []:
        print "Changed sources:"
        for t in changed_sources:
            print "\t", t
    
    return missing_targets != [] or changed_sources != []        
