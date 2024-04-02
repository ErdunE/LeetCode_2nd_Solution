```
class Solution {

    // 做减法

    public List<String> generateParenthesis(int n) {
        
        List<String> res = new ArrayList();
        // 特判
        if(n == 0){
            return res;
        }
        // 执行深度优先遍历，搜索可能的结果
        dfs("", n, n, res);
        return res;
    }
    // curStr 当前递归得到的结果
    // left   左括号还有几个可以使用
    // right  右括号还有几个可以使用
    // res    结果集
    public void dfs(String curStr, int left, int right, List<String> res){
        // 因为每一次尝试，都使用新的字符串变量，所以无需回溯
        // 在递归终止的时候，直接把它添加到结果集即可
        if(left == 0 && right == 0){
            res.add(curStr);
            return;
        }
        // 剪枝（左括号可以使用的个数严格大于右括号可以使用的个数，才剪枝，注意这个细节）
        if(left > right){
            return;
        }

        if(left > 0){
            dfs(curStr + "(" , left - 1, right, res);
        }

        if(right > 0){
            dfs(curStr + ")" , left, right - 1, res);
        }
    }
}
```

时间复杂度: $ O(\frac {{4}^{n}} {\sqrt {n}}) $，在回溯过程中，每个答案需要 O(n) 的时间复制到答案数组中。

空间复杂度: O(n)，除了答案数组之外，所需要的空间取决于递归栈的深度，每一层递归函数需要 O(1) 的空间，最多递归 2n 层，因此空间复杂度为 O(n)。




