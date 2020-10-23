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

def is_balanced(string):
    '''Takes one string as an argument and checks to make sure that 
    the brackets are ballaned.
    Returns Ture if balanced
    Returns False if unbalanced
    Returns None is passed argument is not a string'''

    if type(string) != str:          #Check for valid argument
        return None

    my_dict = {"(":")", ")":0,
               "[":"]", "]":0,
               "{":"}", "}":0,
               "<":">", ">":0}
    
    my_stack = Stack()

    for character in string:          #Iterate over string
        if character not in my_dict:  #Pass over non brackets
            pass
        elif my_dict[character]:      #Check for opening brackets in dict. (0 returns false)
            my_stack.push(my_dict[character]) #If so push to stack
        else:                         #Else must be closing brackets
            if character != my_stack.pop():#Check against top of stack
                return False          #Return false if not matching
    if my_stack.is_empty():
        return True
    else:
        return False

print(is_balanced([]))