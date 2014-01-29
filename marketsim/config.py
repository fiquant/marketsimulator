
# FlaskApp settings
secret_key = 'A0Zr98j/8769876IUOYOHOA0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Veusz settings
runTwoTimes = False
showTiming = True
checkConsistency = False
usePandas = True
useMinorTraders = True

collectRSI = False
collectMoving = True

sources = ["defs"]

import subprocess, importlib, sys

try:
    gitname = subprocess.check_output("git config user.name").strip()
    m = importlib.import_module("marketsim.usr." + gitname)
    getattr(m, "adjust")(sys.modules[__name__])
except Exception:
    pass
