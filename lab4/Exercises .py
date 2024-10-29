class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


def evaluate_postfix(expression):
    
    stack = Stack()
    for token in expression.split():
        if token.isdigit(): 
            stack.push(int(token))
        else:  
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.push(left + right)
            elif token == '-':
                stack.push(left - right)
            elif token == '*':
                stack.push(left * right)
            elif token == '/':
                stack.push(left / right)
    return stack.pop()


def queue_using_two_stacks():
    stack1 = Stack()
    stack2 = Stack()

    def enqueue(item):
        stack1.push(item)

    def dequeue():
        if stack2.is_empty():
            while not stack1.is_empty():
                stack2.push(stack1.pop())
        if stack2.is_empty():
            raise IndexError("Queue is empty")
        return stack2.pop()

    return enqueue, dequeue


def task_scheduler(tasks):
    """Use a queue to implement a basic task scheduler."""
    task_queue = Queue()
    for task in tasks:
        task_queue.enqueue(task)

    while not task_queue.is_empty():
        current_task = task_queue.dequeue()
        print(f"Processing task: {current_task}")


def infix_to_postfix(expression):
   
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = Stack()
    output = []

    for token in expression.split():
        if token.isalnum(): 
            output.append(token)
        elif token in precedence: 
            while (not stack.is_empty() and
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[token]):
                output.append(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop() 
    while not stack.is_empty():
        output.append(stack.pop())

    return ' '.join(output)


postfix_expression = "3 4 + 2 * 7 /"
result = evaluate_postfix(postfix_expression)
print(f"Postfix Evaluation of '{postfix_expression}': {result}")

enqueue, dequeue = queue_using_two_stacks()
enqueue(1)
enqueue(2)
enqueue(3)
print(f"Dequeued from two stacks queue: {dequeue()}")
print(f"Dequeued from two stacks queue: {dequeue()}")

tasks = ["Task 1", "Task 2", "Task 3"]
print("Task Scheduler Output:")
task_scheduler(tasks)

infix_expression = "A + B * C - D"
postfix_result = infix_to_postfix(infix_expression)
print(f"Infix to Postfix of '{infix_expression}': {postfix_result}")