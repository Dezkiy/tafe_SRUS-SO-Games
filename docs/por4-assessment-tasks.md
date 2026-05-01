# Step 1 – Knowledge Question (20-50 words)
**In your own words, describe what a Binary Search Tree (BST) is.**
A BST is a data structure that where each node has up to two children. Left child values are smaller, and right child values are large, which makes searching and inserting data faster.  

**In addition, describe two important properties of a BST: depth and height. How are they different?**
In BST, depth is a number of edges from the root to a specific node. Height is the number of edges from a node to the deepest leaf below it. Depth measures how far the node is from the root. Height measures how tall the subtree is.
# Step 2 – Knowledge Question (50-80 words)
**In your own words, describe how an algorithm to find an item in a Binary Search Tree works.**
To find an items in BST, we start at the root and compare the target value with the current node's value. If they match we have found the item. If the target value is smaller, we move to the left child, if it is larger we move to the right child. We repeat this process until we find the item or reach a leaf node (which means the item is not in the tree). This algorithm is efficient because is eliminates half of the remaining nodes at each step, resulting in a time complexity if O(Log n) in a balance tree. However, in the worst case (skewed tree) it can degrade to O(n).

# Step 3 – Knowledge Question (20-60 words)
**In your own words, describe what a balanced BST is.**
A balanced tree is a BST where left and right sides have similar height, so operations like search and insert stay fast.

# Step 8 - Knowledge Question 
**With the newly balanced BST, how many steps does it take at most to find an existing item in the
search tree?**
At most, it takes about log2(n) steps to find an existing item in a balanced BST, because each step removes about half of the remaining tree.
