#! /usr/bin/env python

import argparse
import sys

##
# Load a tree from from traversal and then again traverse tree.
##


class BinaryNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class Tree(object):

    def __init__(self):
        self.root = None

    def post_order_load(self, nodes):
        # last node is root
        self.root, _ = self._do_post_order_load(nodes=nodes,
                                                idx=len(nodes) - 1,
                                                val=nodes[len(nodes) - 1],
                                                min_=-sys.maxint - 1,
                                                max_=sys.maxint)

    def _do_post_order_load(self, nodes, idx, val, min_, max_):
        if val < min_ or val > max_ or idx < 0:
            return None, idx
        node = BinaryNode(val)
        idx = idx - 1
        if idx > -1:
            node.right, idx = self._do_post_order_load(nodes, idx, nodes[idx],
                                                       val, max_)
            node.left, idx = self._do_post_order_load(nodes, idx, nodes[idx],
                                                      min_, val)
        return node, idx

    def traverse_inorder(self, node=None, out=None):
        if node is None:
            node = self.root
        if out is None:
            out = []
        if node.left:
            self.traverse_inorder(node.left, out=out)
        out.append(node.data)
        if node.right:
            self.traverse_inorder(node.right, out=out)
        return out

    def traverse_postorder(self, node=None, out=None):
        if node is None:
            node = self.root
        if out is None:
            out = []
        if node.left:
            self.traverse_postorder(node.left, out=out)
        if node.right:
            self.traverse_postorder(node.right, out=out)
        out.append(node.data)
        return out

    def traverse_postorder_iterative(self, node=None, out=None):
        if node is None:
            node = self.root
        mem_st = []
        out_st = []
        mem_st.insert(0, node)
        while len(mem_st) > 0:
            node = mem_st.pop(0)
            out_st.insert(0, node.data)
            if node.left:
                mem_st.insert(0, node.left)
            if node.right:
                mem_st.insert(0, node.right)
        return out_st

    def traverse_preorder(self, node=None, out=None):
        if node is None:
            node = self.root
        if out is None:
            out = []
        out.append(node.data)
        if node.left:
            self.traverse_preorder(node.left, out=out)
        if node.right:
            self.traverse_preorder(node.right, out=out)
        return out

    def traverse_preorder_iterative(self, node=None):
        if node is None:
            node = self.root
        out = []
        mem_st = []
        mem_st.insert(0, node)
        while len(mem_st) > 0:
            node = mem_st.pop(0)
            out.append(node.data)
            if node.right:
                mem_st.insert(0, node.right)
            if node.left:
                mem_st.insert(0, node.left)
        return out


#
# ./construct_tree.py --post 1 2 4 5 3 7 9 10 8 6
#
def main(args_):
    tree = Tree()
    if args_.post:
        tree.post_order_load(args_.post)
    print '[inorder]  \n%s' % ' '.join(map(str, tree.traverse_inorder()))
    print '[postorder]\n%s' % ' '.join(map(str, tree.traverse_postorder()))
    print '[postorder_iterative]\n%s' % ' '.join(
        map(str, tree.traverse_postorder_iterative()))
    print '[preorder] \n%s' % ' '.join(map(str, tree.traverse_preorder()))
    print '[preorder_iterative] \n%s' % ' '.join(
        map(str, tree.traverse_preorder_iterative()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # setup for different kinds of loads
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--post', nargs='+', type=int)
    args_ = parser.parse_args()
    main(args_)
