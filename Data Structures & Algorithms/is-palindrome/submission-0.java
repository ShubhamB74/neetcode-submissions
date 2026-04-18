class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder newstring = new StringBuilder();
        for (char c: s.toCharArray()){
            if (Character.isLetterOrDigit(c)){
                newstring.append(Character.toLowerCase(c));
            }
        } 
        return newstring.toString().equals(newstring.reverse().toString());
    }
}
