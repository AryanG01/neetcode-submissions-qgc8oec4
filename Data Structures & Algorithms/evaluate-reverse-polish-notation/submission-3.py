class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                s_num = stack.pop()
                f_num = stack.pop()
                stack.append(f_num + s_num)
            elif token == '-':
                s_num = stack.pop()
                f_num = stack.pop()
                stack.append(f_num - s_num)
            elif token == '*':
                s_num = stack.pop()
                f_num = stack.pop()
                stack.append(f_num * s_num)
            elif token == '/':
                s_num = stack.pop()
                f_num = stack.pop()
                stack.append(int(f_num / s_num))
            else:
                stack.append(int(token))
        
        return stack[0]