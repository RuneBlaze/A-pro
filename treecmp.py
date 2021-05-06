import ete3
import argparse
import json
from ete3 import Tree

parser = argparse.ArgumentParser(description='compare tree')
parser.add_argument('trees', metavar='T', type=str, nargs='+')
args = parser.parse_args()
assert len(args.trees) == 2

trees = []
for i in args.trees:
    with open(i) as fh:
        trees.append(Tree(fh.read()))

a, b = trees
res = a.robinson_foulds(b, unrooted_trees=True)
diff = res[0]
total = res[1]
nrf = diff / total

obj = {"differences" : diff, "total_bipartitions" : total, "nrf" : nrf}
formatted_json = json.dumps(obj, sort_keys=True, indent=4)
print(formatted_json)