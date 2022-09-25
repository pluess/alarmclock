# This allows to have all dependencies in a lib folder in the project
import sys
if not './lib' in sys.path:
    sys.path.insert(0, './lib')