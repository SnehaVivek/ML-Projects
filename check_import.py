import importlib,traceback
try:
    m = importlib.import_module('source.utils')
    print('MODULE_LOADED')
    print('has_save_object=', hasattr(m,'save_object'))
    print('names=', [n for n in dir(m) if not n.startswith('_')])
except Exception:
    traceback.print_exc()