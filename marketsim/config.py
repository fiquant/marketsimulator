class Settings:

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

import subprocess, importlib, sys

try:
    gitname = subprocess.check_output("git config user.name").strip()
    m = importlib.import_module("marketsim.usr." + gitname)
    ms = m.__dict__["Settings"]
    for k in dir(ms):
        if not k.startswith("__"):
            setattr(Settings, k, getattr(ms, k))
except Exception:
    pass

sys.modules[__name__] = Settings()