```
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < numRows; i++){
            List<Integer> curRow = new ArrayList<>();
            
            for(int j = 0; j <= i; j++){
                if(j == 0 || j == i){
                    curRow.add(1);
                }else{
                    curRow.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
                }
            }

            res.add(curRow);
        }
        return res;
    }
}
```


暴力解法    
二次遍历  
创建数组用来保存结果  
设置循环来遍历每一行   
每一行都建立新的数组，然后遍历当前行并分别计算每个位置的结果并保存进去  
将该行结果保存到总结果中  

时间复杂度O(numRows^2)   
空间复杂度O(1) 
