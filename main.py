class Stack:

    def __init__(self, stack:str =""):
        self.stack = list(stack)

    def is_empty(self) -> bool: 
        return len(self.stack) == 0

    def push(self, item:str):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    

def stack_is_balanced(stacks: Stack):
    if not stacks.is_empty() and not stacks.size() % 2:
        right_stack = Stack()
        while stacks.size() > 1:
            last_item = stacks.pop()
            next_item = stacks.peek()
            is_closed = (next_item + last_item) in ['()', '{}', '[]']
            if right_stack.size() > stacks.size():
                check = False 
                break
            if not is_closed:
                right_stack.push(last_item)
                continue
            stacks.pop()
            check = True 
            while not right_stack.is_empty():
                next_item = stacks.pop()
                last_item = right_stack.pop()
                is_closed = (next_item + last_item) in ['()', '{}', '[]']
                if not is_closed:
                    check = False
    else:    
        check = False

    if check == True:
        print (f"Стек сбалансированный")
    else:
        print (f"Стек не сбалансированный")

    return check

    
def tests():
    stack = Stack('(((([{}]))))')
    assert stack_is_balanced(stack)
    stack = Stack('[([])((([[[]]])))]{()}')
    assert stack_is_balanced(stack)
    stack = Stack('{{[()]}}')
    assert stack_is_balanced(stack)
    stack = Stack('}{}')

    print("Все сбалансированные тесты прошли успешно!")

    assert not stack_is_balanced(stack)
    stack = Stack('{{[(])]}}')
    assert not stack_is_balanced(stack)
    stack = Stack('[[{())}]')
    assert not stack_is_balanced(stack)
    stack = Stack('()((((((((((((((((((')

    print("Все не сбалансированные тесты прошли успешно!")

if __name__ == '__main__':

    tests()

    

       