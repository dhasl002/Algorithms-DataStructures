class Stack:
    def __init__(self):
        self.elements = []

    def pop(self):
        if not self.is_empty():
            top_element = self.elements[len(self.elements)-1]
            self.elements.pop(len(self.elements)-1)
            return top_element
        else:
            print("The stack is empty, you cannot pop")

    def push(self, element):
        self.elements.append(element)

    def peek(self):
        if not self.is_empty():
            top_element = self.elements[len(self.elements)-1]
        else:
            print("The stack is empty, you cannot peek")
        return top_element

    def is_empty(self):
        if len(self.elements) > 0:
            return False
        else:
            return True

    def access_element_n(self, n):
        if n > len(self.elements)-1:
            return None

        tmp_stack = Stack()
        for i in range(0, n-1):
            tmp_stack.push(self.pop())
        element_to_return = self.peek()
        for i in range(0, n-1):
            self.push(tmp_stack.pop())

        return element_to_return


if __name__ == "__main__":
    print("Creating a stack with values 0-4")
    stack = Stack()
    for i in range(0, 5):
        stack.push(i)
    print("Is the stack we built empty? {}".format(stack.is_empty()))
    print("Peek the top of the stack: {}".format(stack.peek()))
    print("Pop the top of the stack: {}".format(stack.pop()))
    print("Peek to make sure the pop worked: {}".format(stack.peek()))
    print("Access the 3rd element: {}".format(stack.access_element_n(2)))

