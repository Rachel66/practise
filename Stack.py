class Stack:

   def __init__(self):    
      self.stack = []
      self.top = 0

   def is_empty(self):    
      return (self.top == 0)

   def push(self, item):       
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):       
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]


if __name__ == "__main__":

    list=[65,4,71,33,18,9,56,7,123,99]
    stack = Stack()
    
    for i in range(0,len(list)):
        stack.push(list[i])
        
    for i in range(0,len(list)):
        print(stack.pop())
    
    
