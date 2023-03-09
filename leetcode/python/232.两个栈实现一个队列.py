class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_out:
            return self.stack_out.pop()
        if self.stack_in:
            while self.stack_in:
                num = self.stack_in.pop()
                self.stack_out.append(num)
            return self.stack_out.pop()
        return -1


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_out:
            return self.stack_out[-1]
        if self.stack_in:
            while self.stack_in:
                num = self.stack_in.pop()
                self.stack_out.append(num)
            return self.stack_out[-1]
        return -1


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_in and not self.stack_out



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()