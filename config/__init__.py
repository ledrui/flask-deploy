import os
import sys
import config.settings 

APP_ENV = os.environ.get('APP_ENV', 'DEV')
_current = getattr(os.modules['config.settings'], '{0}Config'.format(APP_ENV))()

# copy attribute to the module for convenience

for atr in [f for f in dir(_current) if not '__' in f]:
    # environment can override anything 
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)

def as_dict():
    res = {}
    for atr in [f for f in dir(config) if not '__' in f]:
        val = getattr(config, atr)
        res[atr] = val

