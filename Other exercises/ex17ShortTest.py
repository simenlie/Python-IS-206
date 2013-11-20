# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

this = open(to_file,'w'); this.write(open(from_file).read()); this.close()





