# object-oriented-programming
I will post here some of my OOP tasks.

## Binary search tree

A binary search tree is a data structure composed of nodes.  
Each node has a key,  which determines the node’s position in the tree.  (The node may also have a “value” field, whereadditional data is stored.)
The top of the tree is the “root,” and the nodes contain pointers to other nodes.  
Specifically,each node has a left child, a right child, and a parent (some of which may be NIL). In Figure12.1(b), the left child of 7 is 6 and the left child of 5 is None.
Also, the parent of 5 is 2, andsince 2 is the root of the tree, the parent of 2 is None

Binary search trees support several operations, including Search, Minimum, Maximum, Pre-decessor, Successor, Insert, and Delete.
These operations run in time proportional to theheight  of  the  tree.
In  the  best  case  scenario,  the  tree  is  a  complete  binary  tree,  and  the height of the tree is Θ(logn).
In the worst case scenario, the tree is a linear chain, so theheight of the tree is Θ(n)

