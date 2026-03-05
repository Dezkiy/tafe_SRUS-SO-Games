class PlayerList:
    def __init__(self):
        self.first = None
        # Tail instance variable: points to the last node in the list.
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
        new_node = (val)

        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return
        
        new_node.next = self.first
        self.first.previous = new_node
        self.first = new_node

    def insert_last(self, val):
        """
        Insert a new item at the end of the player list.

        If the list is empty, the new node becomes both the first
        and last element in the list.

        Otherwise, the node is linked to the current last node,
        and the list's last reference is updated.

        Args:
            val (PlayerNode): The node to insert at the end of the list.

        Returns:
            None
        """
        new_node = (val)

        if self.is_empty():
            self.first = new_node
            self.last = new_node
            return
        
        new_node.previous = self.last
        self.last.next = new_node
        self.last = new_node

    def delete_first(self):
        """
        Delete and return the first node in the list.

        Returns:
            PlayerNode | None: The removed node, or None when the list is empty.
        """
        if self.is_empty():
            return None

        removed = self.first

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = removed.next
            self.first.previous = None

        removed.next = None
        removed.previous = None
        return removed

    def delete_last(self):
        """
        Delete and return the last node in the list.

        Returns:
            PlayerNode | None: The removed node, or None when the list is empty.
        """
        if self.is_empty():
            return None

        removed = self.last

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.last = removed.previous
            self.last.next = None

        removed.next = None
        removed.previous = None
        return removed

    def delete(self, key):
        """
        Delete and return the first node that matches ``key``.

        The key is matched against ``PlayerNode.key`` (player uid).

        Args:
            key (str): Player uid to remove.

        Returns:
            PlayerNode | None: The removed node, or None when no match exists.
        """
        current = self.first

        while current and current.key != key:
            current = current.next

        if current is None:
            return None

        if current == self.first and current == self.last:
            self.first = None
            self.last = None
        elif current == self.first:
            self.first = current.next
            self.first.previous = None
        elif current == self.last:
            self.last = current.previous
            self.last.next = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous

        current.next = None
        current.previous = None
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
