class Stack(object):

    def __init__(self):
        self.list_stack = []
    
    def is_empty(self):
        if self.list_stack:
            return False
        else:
            return True
    
    def push(self,item):
        self.list_stack.append(item)
    
    def pop(self):
        if self.list_stack:
            return self.list_stack.pop()
        else:
            return None

    def peek(self):
        if self.list_stack:
            return self.list_stack[-1]
        else:
            return None
    
    def __repr__(slef):
        return repr(self.list_stack)

    
