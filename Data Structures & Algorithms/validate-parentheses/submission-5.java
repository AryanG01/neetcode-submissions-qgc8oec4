class Solution {
    public static boolean isValid(String s) {
        List<Character> stack = new ArrayList<> ();

        for (char c : s.toCharArray()) {
            if(c == '(' || c == '{' || c == '[') {
                stack.add(c);
            } else {
                if(stack.size() == 0) {
                    return false;
                }
                char pop_out = stack.remove(stack.size() - 1);
                if (c == ')' && pop_out != '(') {
                    return false;
                } else if (c == '}' && pop_out != '{') {
                    return false;
                } else if (c == ']' && pop_out != '[') {
                    return false;
                }
            }
            
        }


        return stack.size() == 0;
    }
}
