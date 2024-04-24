class TodoList:
    def __init__(self):
        self.content = []
    
    def add_todo(self, item):
        if item in self.content:
            raise Exception("Item already in Todo list")
        else:
            self.content.append(item)
            
    
    def list_todo(self):
        return self.content
    
    def complete_todo(self, item):
        if item not in self.content:
            raise Exception("No Item in the list")
        else:
            self.content.remove(item)
        return self.content
    