class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> st = new Stack<>();
        for (String t : tokens) {
            if ("+-*/".contains(t)) {
                st.push(eval(st.pop(), st.pop(), t));
            } else {
                st.push(Integer.parseInt(t));
            }
        }
        return st.pop();
    }

    private int eval(int b, int a, String op) {
        if ("+".equals(op)) {
            return a + b;
        } else if ("-".equals(op)) {
            return a - b;
        } else if ("*".equals(op)) {
            return a * b;
        } else {
            return a / b;
        }
    }
}
