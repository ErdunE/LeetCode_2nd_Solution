```
class Solution {
    public int[][] merge(int[][] intervals) {

        // 创建新的数组用来保存结果
        List<int[]> res = new ArrayList<>();
        // 空数组处理
        if(intervals == null || intervals.length == 0){
            // new int[0][]表示不指定行、行自动填充，如果为new int[4][], 即使结果为[[1,6],[8,10],[15,18]]， 也会强制输出[[1,6],[8,10],[15,18],null]，即不足行null补充
            return res.toArray(new int[0][]);
        }
        // 对数组进行排序
        // lambda表达式 相当于 Arrays.sort(intervals, (Comparator.comparingInt(o -> o[0])));
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);

        int i = 0;
        // 遍历数组，当i小于数组长度时，一直循环
        while(i < intervals.length){
            // 定义每个数组左右数字
            int left = intervals[i][0];
            int right = intervals[i][1];
            // 当i小于数组长度-1 且 下一个左边数字小于或等于当前右边数字是 一直循环
            while(i < intervals.length - 1 && intervals[i + 1][0] <= right){
                i++;
                // 不停取右边最大的数字 直到满足该循环停止条件
                right = Math.max(right, intervals[i][1]);
            }
            // 结果数组加入该左右数字
            res.add(new int[]{left, right});
            // 寻找下一个符合的数组
            i++;
        } 
        // 返回最终结果
        return res.toArray(new int[0][]);   
    }   
}
```

贪心算法 注释在上面

时间复杂度：O(nlog⁡n)，其中 n 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlog⁡n)

空间复杂度：O(log⁡n)，其中 n 为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(log⁡n) 即为排序所需要的空间复杂度。