```
class RandomizedSet {
    List<Integer> nums;
    Map<Integer, Integer> indices;
    Random random;

    public RandomizedSet() {
        nums = new ArrayList<Integer>();
        indices = new HashMap<Integer, Integer>(); //可变长数组，即链表，即使后面删除了元素，链表中的元素也是紧挨着的，像数组一样
        random = new Random();
    }
    
    public boolean insert(int val) {
        if(indices.containsKey(val)){
            return false;
        }
        int index = nums.size();
        nums.add(val); //链表存入数据
        indices.put(val, index);//哈希表中存入该数据和它在链表中的下标
        return true;
    }
    
    public boolean remove(int val) {
        if(!indices.containsKey(val)){
            return false;
        } 

        //总体思路：用链表最后一个元素覆盖要删除的元素，然后把链表最后一个元素删掉，更新哈希表中的数据
        int index=indices.get(val);//在哈希表中查找该数据在链表中的下标
        int last=nums.get(nums.size()-1);//获取链表中最后一个元素
        nums.set(index,last);//把最后一个元素移到需要删除的元素处，替换掉
        indices.put(last,index);//把替换后的元素和它的新下标一起存入哈希表
        nums.remove(nums.size()-1);//删掉链表最后一个元素
        indices.remove(val);//删掉哈希表中要删除的元素
        return true;     
    }
    
    public int getRandom() {
        int randomIndex=random.nextInt(nums.size());//获取一个范围为[0,nums.size())的随机整数
        return nums.get(randomIndex);
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```


变长数组 + 哈希表   
变长数组可以在O(1)的时间内完成获取随机元素操作，但是由于无法在O(1)的时间内判断元素是否存在，因此不能在O(1)的时间内完成插入和删除操作。哈希表可以在O(1)的时间内完成插入和删除操作，但是由于无法根据下标定位到特定元素，因此不能在O(1)的时间内完成获取随机元素操作。为了满足插入、删除和获取随机元素操作的时间复杂度都是O(1)，需要将变长数组和哈希表结合，变长数组中存储元素，哈希表中存储每个元素在变长数组中的下标。

插入操作时，首先判断val是否在哈希表中，如果已经存在则返回false，如果不存在则插入val，操作如下：

1. 在变长数组的末尾添加val；

2. 在添加val之前的变长数组长度为val所在下标index，将val和下标index存入哈希表；

3. 返回true。

删除操作时，首先判断val是否在哈希表中，如果不存在则返回false，如果存在则删除val，操作如下：

1. 从哈希表中获得val的下标index；

2. 将变长数组的最后一个元素last移动到下标index处，在哈希表中将last的下标更新为 index；

3. 在变长数组中删除最后一个元素，在哈希表中删除val；

4. 返回true。

删除操作的重点在于将变长数组的最后一个元素移动到待删除元素的下标处，然后删除变长数组的最后一个元素。该操作的时间复杂度是O(1)，且可以保证在删除操作之后变长数组中的所有元素的下标都连续，方便插入操作和获取随机元素操作。

获取随机元素操作时，由于变长数组中的所有元素的下标都连续，因此随机选取一个下标，返回变长数组中该下标处的元素。



时间复杂度：初始化和各项操作的时间复杂度都是O(1)。
空间复杂度：O(n)，其中n是集合中的元素个数。存储元素的数组和哈希表需要O(n)的空间。

