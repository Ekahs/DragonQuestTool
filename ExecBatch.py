import sys
import importlib

args = sys.argv
m = importlib.import_module('batch.' + args[1])
