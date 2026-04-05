class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2 - op1)
            elif token == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(float(op2) / op1))
            else:
                stack.append(int(token))
        
        return stack[0]