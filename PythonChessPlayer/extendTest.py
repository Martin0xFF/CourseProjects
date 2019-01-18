from chesslib import *
from chessPlayer_tree import tree
a = initBoard(None)
root = tree(a)
# print root.store
looks = extend(root,2,10)
basket = processNode(looks,2)
weight = sum(basket)/len(basket)

print weight


