import importlib, traceback
try:
    m = importlib.import_module('source.utils')
    print('MODULE_FILE:', getattr(m, '__file__', None))
    print('HAS_save_object:', hasattr(m, 'save_object'))
    print('NAMES:', [n for n in dir(m) if not n.startswith('_')])
except Exception:
    traceback.print_exc()
