```
class Solution {
    public int removeDuplicates(int[] nums) {

        int p = 0, q = 1;

        while(q < nums.length){
            if(nums[p] == nums[q]){
                q++;
            }
            else{
                nums[p + 1] = nums[q];
                p++;
                q++;
            }
        }

        return p + 1;

    }
}
```


暴力解法  
双指针  
双指针分别指向第一个数字和第二个数字  
如果两个指针相同，快指针继续向右  
如果两个指针不同，慢指针+1等于快指针，然后两个指针都继续向右  
当右指针到头的时候，返回慢指针+1  

时间复杂度O(N) 遍历一遍数组
空间复杂度O(1) 变量 p q 仅使用常量变数空间
