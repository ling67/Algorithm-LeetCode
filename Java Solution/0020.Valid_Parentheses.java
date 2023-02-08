// Stack 

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        
        Stack<Character> st = new Stack<>();
        for(char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
                continue;
            }
            if (st.size() == 0 || map.get(ch) != st.pop()) {
                return false;
            }
        }
        return st.size() == 0 ? true : false;
    }
}
