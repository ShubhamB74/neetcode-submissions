class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<numbers.length; i++){
            int t = target - numbers[i];
            if(map.containsKey(t)){
                return new int[] {map.get(t), i+1};
            }
            map.put(numbers[i],i+1);
        }
        return new int[0];
    }
}
