class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.add(c); // Push opening brackets onto the stack
            } else {
                // If the stack is empty or the brackets don't match, return false
                if (stack.size() == 0) {
                    return false;
                }
                char pop_out = stack.remove(stack.size() - 1); // Pop the top of the stack
                if (!isValidPair(pop_out, c)) {
                    return false;
                }
            }
        }

        // Return true if all opening brackets were matched, otherwise false
        return stack.size() == 0;
    }

    // Helper method to check if the pair of brackets is valid
    private boolean isValidPair(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '{' && close == '}') ||
               (open == '[' && close == ']');
    }
}
