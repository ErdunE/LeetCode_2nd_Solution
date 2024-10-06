class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = set()
        node = p
        while node:
            a.add(node)
            node = node.parent
        node = q
        while node not in a:
            node = node.parent

        return node