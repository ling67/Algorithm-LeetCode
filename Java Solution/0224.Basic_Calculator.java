class Solution {
    public int calculate(String s) {
        Stack<Integer> resSt = new Stack<>();
        Stack<Integer> signSt = new Stack<>();
        int res = 0, sign = 1;
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (Character.isDigit(ch)) {
                int num = s.charAt(i) - '0';
                while(i + 1 < s.length() && Character.isDigit(s.charAt(i + 1))) {
                    num = 10 * num + s.charAt(i + 1) - '0';
                    i++;
                }
                res += num * sign;
            } else if (ch == '+') {
                sign = 1;
            } else if (ch == '-') {
                sign = -1;
            } else if (ch == '(') {
                resSt.push(res);
                signSt.push(sign);
                res = 0;
                sign = 1;
            } else if (ch == ')')  {
                res = resSt.pop() + signSt.pop() * res;
            }
            i++;
        }
        return res;
    }
}
