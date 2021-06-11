import treeswift as ts
from sys import argv

def unroot(tree):
    """
    Unroots treeswift tree. Adapted from treeswift 'deroot' function.
    This one doesn't contract (A,B); to A;

    Parameters
    ----------
    tree: treeswift tree

    Returns unrooted treeswift tree
    """
    if tree.root == None:
        return tree
    if tree.root.num_children() == 2:
        [left, right] = tree.root.child_nodes()
        if not right.is_leaf():
            right.contract()
        elif not left.is_leaf():
            left.contract()
    tree.is_rooted = False
    return tree

def strip(t):
    for node in t.traverse_postorder():
        if node.is_leaf and node.label:
            node.label = node.label.split("_")[0]
        elif (not node.is_leaf) and node.label:
            node.label = None
        else:
            node.label = None
        if (node.label and "." in node.label):
            node.label = None
        node.edge_length = None
    return unroot(t)


if __name__ == '__main__':
    fn = argv[1]
    outf = argv[2]
    with open(outf, "w+") as outh:
        with open(fn) as fh:
            for l in fh:
                t = ts.read_tree_newick(l)
                t = strip(t)
                op = unroot(t).newick()
                outh.write(op)
                outh.write("\n")