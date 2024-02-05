```
class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        int temp[] = new int[len];

        for(int i = 0; i < len; i++){
            temp[i] = nums[i];
        }
        for(int i = 0; i < len; i++){
            nums[(i + k) % len] = temp[i];
        }
    }
}
```


使用额外的数组  
可以使用一个临时数组，先把原数组的值存放到一个临时数组中，然后再把临时数组的值重新赋给原数组，重新赋值的时候要保证每个元素都要往后移k位，如果超过数组的长度就从头开始，所以这里可以使用(i + k) % length来计算重新赋值的元素下标

时间复杂度O(n) 数组的长度
空间复杂度O(n) 
