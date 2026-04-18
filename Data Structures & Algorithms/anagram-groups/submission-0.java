class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> result = new HashMap<>();
        for (String s: strs){
            char[] c = s.toCharArray();
            Arrays.sort(c);

            String sorted = new String(c);
            result.putIfAbsent(sorted, new ArrayList<>());
            result.get(sorted).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
