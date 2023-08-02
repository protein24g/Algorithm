import sys
input = sys.stdin.readline

ary = input()
stack = []
result = ''

priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}

for char in ary:
    if char.isalpha():
        result += char
    else:
        if char == '(':
            stack.append(char)
        elif char == '*' or char == '/' or char == '+' or char == '-':
            while stack and priority[char] <= priority[stack[-1]]:
                result += stack.pop()
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)
