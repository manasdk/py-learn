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



class Tree(object):

    def __init__(self):
        self.root = None

    def post_order_load(self, nodes):
        # last node is root
        self.root, _ = self._do_post_order_load(nodes=nodes, idx=len(nodes) - 1,
            val=nodes[len(nodes) - 1], min_=-sys.maxint-1, max_=sys.maxint)

    def _do_post_order_load(self, nodes, idx, val, min_, max_):
        if val < min_ or val > max_ or idx < 0:
            return None, idx
        node = BinaryNode(val)
        idx = idx - 1
        if idx > -1:
            node.right, idx = self._do_post_order_load(nodes, idx, nodes[idx], val, max_)
            node.left, idx = self._do_post_order_load(nodes, idx, nodes[idx], min_, val)
        return node, idx

    def traverse_inorder(self, node=None, out=None):
        if node == None:
            node = self.root
        if out == None:
            out = []
        if node.left:
            self.traverse_inorder(node.left, out=out)
        out.append(node.data)
        if node.right:
            self.traverse_inorder(node.right, out=out)
        return out

    def traverse_postorder(self, node=None, out=None):
        if node == None:
            node = self.root
        if out == None:
            out = []
        if node.left:
            self.traverse_postorder(node.left, out=out)
        if node.right:
            self.traverse_postorder(node.right, out=out)
        out.append(node.data)
        return out

    def traverse_preorder(self, node=None, out=None):
        if node == None:
            node = self.root
        if out == None:
            out = []
        out.append(node.data)
        if node.left:
            self.traverse_preorder(node.left, out=out)
        if node.right:
            self.traverse_preorder(node.right, out=out)
        return out


def main(args_):
    tree = Tree()
    if args_.post:
        tree.post_order_load(args_.post)
    print '[inorder]  \n%s' % ' '.join(map(str, tree.traverse_inorder()))
    print '[postorder]\n%s' % ' '.join(map(str, tree.traverse_postorder()))
    print '[preorder] \n%s' % ' '.join(map(str, tree.traverse_preorder()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # setup for different kinds of loads
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--post', nargs='+', type=int)
    args_ = parser.parse_args()
    main(args_)
