# python2

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check_brackets():
    text = sys.stdin.read()
    op = None

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        elif next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                bracket = opening_brackets_stack.pop()
                if bracket.Match(next):
                    continue
            op = i + 1
            break
    # Printing answer, write your code here
    if op==None:
        if opening_brackets_stack:
            op = opening_brackets_stack.pop().position + 1
        else:
            op = 'Success'
    return op


if __name__ == "__main__":
    op = check_brackets()
    print op
