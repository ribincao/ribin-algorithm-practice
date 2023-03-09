class MyStack:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q1 and not self.q2:
            return -1
        if not self.q2:
            self.q1, self.q2 = self.q2, self.q1
        if not self.q1:
            while len(self.q2) > 1:
                num = self.q2.pop(0)
                self.q1.append(num)
            return self.q2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q1 and not self.q2:
            return -1
        if not self.q2:
            self.q1, self.q2 = self.q2, self.q1
        if not self.q1:
            while len(self.q2) > 0:
                num = self.q2.pop(0)
                self.q1.append(num)
            return num

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return (not self.q1 and not self.q2)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()