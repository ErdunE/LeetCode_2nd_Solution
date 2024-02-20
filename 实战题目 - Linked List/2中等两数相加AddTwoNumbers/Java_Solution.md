```
class Solution {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int res = 0;

        while(i < j){
            res = Math.max(res, (j - i) * Math.min(height[i], height[j]) );
            if(height[i] < height[j]){
                i++;
            }
            else{
                j--;
            }
        }

        return res;
    }
}
```


暴力解法  
双指针  
双指针分别指向水槽左右两端  
短板向中间移动，双指针相遇就停止  
依次计算当前面积并保存于变量res中  
选定两板高度中的短板，向中间收窄一格  
最后返回res即是最大的结果  

时间复杂度O(N) 遍历一遍底边长度  
空间复杂度O(1) 变量 i j res 仅适用常量变数空间
