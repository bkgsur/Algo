# Search path - sequence of nodes from root to a node
# depth of a node - number of nodes in search path to node (not counting the node)
# height of a tree - max depth of any node
# level of a tree - all nodes at same depth

# FULL binary tree - all nodes have 2 children -
#   number of non leaf nodes is one less than number of leaves
# PERFECT binary tree - FULL + all leaves same level.
#   if height h - nodes = 2^h+1 -1  of which 2^h are leaves
# COMPLETE binary tree - all levels (except last) completely filled
#   and all nodes as left as possible. height = floor(log n).

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


def preordertraverse(root: binarytreenode) -> None:
    if root is not None:
        print(root.data, end=" ")
        inordertraverse(root.left)
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


# inordertraverse(t)
# traverse(t)

def buildsymmetrictree() -> binarytreenode:
    r = binarytreenode(0)
    r.left = binarytreenode(1)
    r.right = binarytreenode(1)

    r.left.right = binarytreenode(2)
    r.left.right.right = binarytreenode(3)
    r.right.left = binarytreenode(2)
    r.right.left.left = binarytreenode(3)
    return r


def issymmetric(tree: binarytreenode) -> bool:
    def helper(node0: binarytreenode, node1: binarytreenode) -> bool:
        if not node0 and not node1:
            return True
        elif node0 and node1:
            return (node0.data == node1.data) and helper(node0.left, node1.right) and helper(node0.right, node1.left)
        else:
            return False

    return not tree or helper(tree.left, tree.right)


# t1 = buildsymmetrictree()
#
# preordertraverse(t1)
# print("\n")
# inordertraverse(t1)
# print("\n")
# print(issymmetric(t1))

def lca(root: binarytreenode, p: int, q: int) -> binarytreenode:
    if root.data == p or root.data == q:
        return root
    # leaf nodes
    if root.left is None and root.right is None:
        return None
    leftnode: binarytreenode = None
    rightnode: binarytreenode = None
    if root.left:
        leftnode = lca(root.left, p, q)
    if root.right:
        rightnode = lca(root.right, p, q)
    if leftnode and rightnode:
        return root
    if leftnode is None:
        return rightnode
    else:
        return leftnode


t1 = buildbinarytree([1, 2, 3, 4, 5, 6])
# inordertraverse(t1)
print(lca(t1, 2, 3).data)
