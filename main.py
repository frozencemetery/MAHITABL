#!/usr/bin/env python
import argparse
import os
import sys

allowed = "qwertyuiopasdfghjklzxcvbnm"

def fix_fname(e):
  newe = None

  for i in xrange(len(e)):
    if e[i] not in allowed:
      if newe == None:
        # strings do not allow modification because reasons?
        newe = list(e)
        if args.default:
          newe[i] = args.default
          pass
        else:
          print "TODO(frozen) banned character with no replacement!"
          pass
        pass
      pass
    pass
  print e

  if newe:
    print ''.join(newe)
    pass

  return ''.join(newe) if newe else e

def process_files(queue):
  while len(queue) > 0:
    e = queue.pop()
    if not os.path.lexists(e):
      print "Path %s doesn't exist!" % e
      return 1

    # These are "magic" locations unrelated to actual filenames that we care
    # about.  If present, they will have been passed by the user since we're
    # storing relative paths and os.listdir will not return them.
    if e not in [".", ".."]:
      newe = fix_fname(e)
      if newe != e:
        print "TODO(frozen) Would rename `%s' to `%s'" % (e, newe)
      pass

    if os.path.isdir(e):
      queue += ["%s/%s" % (e, d) for d in os.listdir(e)]
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
  sys.exit(process_files(args.targets))

if __name__ == "__main__":
  main(sys.argv)
  pass
