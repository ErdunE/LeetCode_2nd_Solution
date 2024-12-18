# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Initialize a counter to keep track of nodes that match the condition
        result = 0

        # Define a recursive function to traverse the tree using DFS
        def dfs(node):
            nonlocal result # Allows the function to modify the count variable from the outer scope

            # Base case: If the node is None, return a sum of 0 and a count of 0 nodes
            if not node:
                return 0, 0
            else:
                # Recursively calculate the sum and count of nodes in the left subtree
                left_sum, left_num = dfs(node.left)
                # Recursively calculate the sum and count of nodes in the right subtree
                right_sum, right_num = dfs(node.right)

                # Calculate the total sum of the current subtree
                total_sum = left_sum + right_sum + node.val
                # Calculate the total number of nodes in the current subtree
                total_num = left_num + right_num + 1

                # Calculate the average of the current subtree (rounded down using integer division)
                avg = total_sum // total_num

                # If the current node's value matches the average, increment the counter
                if avg == node.val:
                    result += 1

                # Return the sum and count of the current subtree to the parent node
                return total_sum, total_num

        # Start DFS traversal from the root node
        dfs(root)
        # Return the final count of nodes that match the condition
        return result

