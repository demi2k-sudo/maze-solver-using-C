import sys
try:
    print(sys.argv)
except IOError:
    print("passed")