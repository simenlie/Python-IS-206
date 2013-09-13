# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file).read()
print "Saving..."
out_file = open(to_file,'w')
out_file.write(in_file)

print "Done!"

out_file.close()

