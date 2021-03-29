# 使用python实现树的数据结构
class BinaryTree(object):
    def __init__(self, value=None):
        self.data = [value, None, None]

    def __str__(self):
        return "[根结点：{}, 左节点：{}, 右节点：{}]".format(self.value, self.left_tree, self.right_tree)

    @property
    def left_tree(self):
        return self.data[1]

    @left_tree.setter
    def left_tree(self, left_tree):
        self.data[1] = left_tree

    @property
    def right_tree(self):
        return self.data[2]

    @right_tree.setter
    def right_tree(self, right_tree):
        self.data[2] = right_tree

    @property
    def value(self):
        return self.data[0]

    @value.setter
    def value(self, value):
        self.data[0] = value

    def insert_node(self, tvalue, tree_obj, direction='left'):
        if self.value == tvalue:
            if direction == 'left':
                self.left_tree = tree_obj
            else:
                self.right_tree = tree_obj
            return True
        else:
            if self.left_tree and self.left_tree.insert_node(tvalue, tree_obj, direction):
                return True
            elif self.right_tree and self.right_tree.insert_node(tvalue, tree_obj, direction):
                return True
            else:
                return False


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_node(1, BinaryTree(2), 'left')
    tree.insert_node(1, BinaryTree(3), 'right')
    tree.insert_node(2, BinaryTree(4), 'left')
    tree.insert_node(2, BinaryTree(5), 'right')
    tree.insert_node(3, BinaryTree(6), 'left')
    print(tree)