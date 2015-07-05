#!/usr/bin/env python
import argparse
import os
import sys

allowed = "qwertyuiopasdfghjklzxcvbnm.QWERTYUIOPASDFGHJKLZXCVBNM1234567890_-"

def fix_fname(e, full):
  newe = None

  for i in xrange(len(e)):
    if e[i] not in allowed:
      if not newe:
        # strings do not allow modification because reasons?
        newe = list(e)
        pass
      if args.default:
        newe[i] = args.default
        pass
      else:
        print "TODO(frozen) banned character with no replacement!"
        pass
      pass
    pass

  return ''.join(newe) if newe else None

def process_files(queue):
  while len(queue) > 0:
    (lead, e) = queue.pop()
    full = lead + e
    print full
    if not os.path.lexists(full):
      print "Path %s doesn't exist!" % e
      return 1

    # These are "magic" locations unrelated to actual filenames that we care
    # about.  If present, they will have been passed by the user since we're
    # storing relative paths and os.listdir will not return them.
    if e not in [".", ".."]:
      newe = fix_fname(e, full)
      if newe:
        full = lead + newe
        print "TODO(frozen) Would rename `%s' to `%s'" % (e, newe)
        e = newe
        pass
      pass

    if os.path.isdir(full):
      queue += [(full + '/', d) for d in os.listdir(full)]
      pass
    pass
  return 0

def main(argv):
  global args

  p = argparse.ArgumentParser(description=
                              "Sanitize filenames for foreign fileystems")
  p.add_argument("targets", nargs='+', help="Entries to operate on")
  p.add_argument("-d", "--default",
                 help="Default character for replacement (default: off)")
  args = p.parse_args(argv[1:])
  print args
  sys.exit(process_files([("", s) for s in args.targets]))

if __name__ == "__main__":
  main(sys.argv)
  pass
