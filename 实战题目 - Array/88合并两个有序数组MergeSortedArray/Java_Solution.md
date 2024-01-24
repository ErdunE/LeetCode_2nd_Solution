```
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1;
        int p2 = n - 1;
        int len = m + n - 1;

        while(p2 >= 0){
            if(p1 >=0 && nums1[p1] > nums2[p2]){
                nums1[len] = nums1[p1];
                len--;
                p1--;
            }else{
                nums1[len] = nums2[p2];
                len--;
                p2--;
            }
        }
    }
}
```


双指针倒序遍历

初始化三个指针 p1=m−1指向nums1的末尾，p2=n−1指向nums2的末尾，p=m+n−1指向合并后的数组末尾
不断比较nums1[p1]和nums2[p2]的大小，将较大值放入nums[len],然后将指针-1，并开始比较下一个

时间复杂度：O(m+n)。最坏情况形如 nums1=[4,5,6,∗,∗,∗],nums2=[1,2,3]，每个数都需要移动一次。
空间复杂度：O(1)。仅用到若干额外变量。
