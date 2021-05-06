# generates ASTRID-multi mapping files from multicopy gene trees

import treeswift as ts
from treeswift import Tree, Node
from collections import deque, defaultdict
from random import choice
from itertools import groupby
from random import sample
import os, sys
fn = sys.argv[1]

labels = set()

with open(fn + ".rp", "w+") as of:
    with open(fn) as fh:
        for l in fh:
            tre = ts.read_tree_newick(l)
            tre.root.resolve_polytomies()
            of.write(tre.newick() + "\n")