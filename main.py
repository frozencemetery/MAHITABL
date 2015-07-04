#!/usr/bin/env python
import argparse
import os
import sys

def fix_fname(e):
  # TODO(frozencemetery) implement this
  print e
  return e

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
      e = fix_fname(e)
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
  args = p.parse_args(argv[1:])
  sys.exit(process_files(args.targets))

if __name__ == "__main__":
  main(sys.argv)
  pass
