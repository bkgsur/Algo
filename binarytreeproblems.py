# Search path - sequence of nodes from root to a node
# depth of a node - number of nodes in search path to node (not counting the node)
# height of a tree - max depth of any node
# level of a tree - all nodes at same depth

# FULL binary tree - all nodes have 2 children - number of non leaf nodes is one less than number of leaves
# PERFECT binary tree - FULL + all leaves same level. if height h - nodes = 2^h+1 -1  of which 2^h are leaves
# COMPLETE binary tree - all levels (except last) completely filled and all nodes as left as possible. height = floor(log n).

# Traversal -
# preorder - root , left, right
# Inorder - left subtree, root, right subtree
# postorder - left, right, root
# n nodes/h height - O(n) time complexity, O(h) - space . If each node has a parent field, the traversals can be
# done with O(1) additional space complexity.


class binarytreenode:

    def __init__(self, data=None, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def buildbinarytree(A: [], i: int = 0) -> binarytreenode:
    root: binarytreenode = None
    if i < len(A):
        root = binarytreenode(A[i])

        # insert left child
        root.left = buildbinarytree(A, 2 * i + 1)

        # insert right
        root.right = buildbinarytree(A, 2 * i + 2)
    return root


t = buildbinarytree([*range(7)])


def inordertraverse(root: binarytreenode) -> None:
    if root is not None:
        inordertraverse(root.left)
        print(root.data, end=" ")
        inordertraverse(root.right)


# time - O(n)
# space - for complete bt O(h) - for skewed O(n)
def traverse(root: binarytreenode) -> None:
    txt = "{data:d}"
    if root:
        # preorder - process root
        print('preorder', txt.format(data=root.data))
        # inorder
        traverse(root.left)
        print('inorder', txt.format(data=root.data))
        # postorder
        traverse(root.right)
        print('postorder', txt.format(data=root.data))


inordertraverse(t)
traverse(t)
