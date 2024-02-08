```
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        if(len == 0){
            return new int[0];
        }
        int[] ans = new int[len];
        ans[0] = 1;
        int tmp = 1;
        for(int i = 1; i < len; i++){
            ans[i] = ans[i - 1] * nums[i - 1];
        }
        for(int i = len - 2; i >= 0; i--){
            tmp = tmp * nums[i + 1];
            ans[i] = ans[i] * tmp;
        }
        return ans;
    }
}
```


暴力算法  
初始化：数组 ans，其中 ans[0]=1 辅助变量 tmp=1  
计算 ans[i] 下三角 各元素的乘积，直接乘入 ans[i]  
计算 ans[i] 的 上三角 各元素的乘积，记为 tmp，并乘入 ans[i]  
返回 ans  

时间复杂度O(N) 其中 N 为数组长度，两轮遍历数组 nums，使用 O(N)时间。   
空间复杂度O(1) 变量 tmp使用常数大小额外空间（数组 ans作为返回值，不计入复杂度考虑）。
