import os, sys

from types import cached_property

import chk_ts
    
if chk_ts.gen_needed():
    print " -> Regenerating...",
    
    import rnd
    
    print "done."
            
    


