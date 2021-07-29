open_brackets = ["[", "{", "("]
closed_brackets = ["]", "}", ")"]

def validate_brackets(str):
    stack = []
    for i in str:
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            brackets = closed_brackets.index(i)
            if ((len(stack) > 0) and (open_brackets[brackets] == stack[len(stack) -1])):
                stack.pop()
            else:
                return False, "Unbalanced"
    if len(stack) == 0:
        return True, "Balanced"
    else:
        return False, "Unbalanced"
# Brackets = {
#      "{" : "}",
#      "(" : ")",
#      "[" : "]"
# }

# class Node:
#     def __init__(self, value, next = None):
#         self.value = value
#         self.next = next

# class Stack:
#     def __init__(self, top=None):
#         self.top = top

#     def push(self, value):
#         node = Node(value)
#         node.next = self.top
#         self.top = node

#     def isEmpty(self):
#         return self.top == None

#     def validate_brackets(self, arg):
#         while len(arg) < 0:
#             for i in  arg:
#                 if i in Brackets.keys():
#                     self.push(i)
#                 elif i in Brackets.values():
#                     for key, value in Brackets.items():
#                         if key == value:
#                             self.push(value)
#                         else:    
#                             return False
#         return True
