## Binary Tree and BST Implementation
### Binary Search Tree
- Create a Binary Search Tree class
  - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  - Add
   - Arguments: value
   - Return: nothing
   - Adds a new node with that value in the correct location in the binary search tree.
  - Contains
   - Argument: value
   - Returns: boolean indicating whether or not the value is in the tree at least once.  
### Structure and Testing
Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

- Write tests to prove the following functionality:

Can successfully instantiate an empty tree  
Can successfully instantiate a tree with a single root node  
Can successfully add a left child and right child to a single root node  
Can successfully return a collection from a preorder traversal  
Can successfully return a collection from an inorder traversal  
Can successfully return a collection from a postorder traversal  
