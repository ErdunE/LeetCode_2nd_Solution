class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, row, col):
            if root is None:
                return
            d[col].append((row,root.val))
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)

        d = defaultdict(list)
        dfs(root, 0, 0)
        res = []

        for col, node_list in sorted(d.items()):

            node_list_sorted = sorted(node_list, key = lambda item:item[0])

            node_values = []

            for row, value in node_list_sorted:
                node_values.append(value)

            res.append(node_values)

        return res