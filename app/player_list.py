class PlayerList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None and self.last is None
    
    def find_from_start(self, key):
        current = self.first
        while current and current != key:
            current = current.next

        return current
        
    def find_from_end(self, key):
        current = self.last
        while current and current != key:
            current = current.previous

        return current
        
    def insert_first(self, val):
        # new_node = PlayerNode(val)
        new_node = (val)

        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return
        
        new_node.next = self.first
        self.first.previous = new_node
        self.first = new_node

    def insert_last(self, val):
        new_node = (val)

        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return
        
        new_node.previous = self.last
        self.last.next = new_node
        self.last = new_node

    def delete(self, key):
        current = self.first
        previous = self.first

        while current.val != key:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
            self.first.previous = None
        else:
            previous.next = current.next
            current.next.previous = previous

        return current

    def display(self):
        result = ["List first --> last:"]

        current = self.first
        while current:
            result.append(
                        f"#<#_prev: {current.previous}, "
                        f"#-#_node: {current}, "
                        f"#>#_next: {current.next}"
                    )
            current = current.next

        return "\n".join(result)