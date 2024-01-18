```
class Solution {
    public int[] plusOne(int[] digits) {
        
        // 创建变量保存数组长度
        int len = digits.length;

        // 循环从数组最后以为开始，直到第一位
        for(int i = len - 1; i >= 0; i--){    
            // 数组最后一位加一后除10
            digits[i] = (digits[i] + 1) % 10;
            // 如果数组当前最后一位不是0 返回结果
            if(digits[i] != 0){
                return digits;
            }
        }
        // 如果上面的循环中没有返回结果，说明该数组为特殊情况即 99 或 999，需要特殊处理
        digits = new int[len + 1];
        digits[0] = 1;
        return digits;
    }
}
```


遍历

时间复杂度：O(n)其中 n 是数组 digits的长度。

空间复杂度：O(1)。返回值不计入空间复杂度。