import os, argparse

parser = argparse.ArgumentParser(description='Script for renaming files!')
parser.add_argument("dir", help="Root dir")
parser.add_argument("old_name", help="Old name of file")
parser.add_argument("new_name", help="New name")
args = parser.parse_args()

def _rename(current_directory):
    for root, subdirs, files in os.walk(current_directory):
        for dir in subdirs:
            _rename(dir)
        for f in files:
            if f == args.old_name:
                old_path = os.path.join(root, f)
                new_path = os.path.join(root, args.new_name)
                print "Renaming %s to %s" % (old_path, new_path)
                os.rename(old_path, new_path)
_rename(args.dir)