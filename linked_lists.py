

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """adds element to end of a list"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1
        if position < 1:
            return None
        while current and count <= position:
            if count == position:
                return current
            current = current.next
            count += 1
        return None      
        
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements. Will take "3'"s place
        and push it to the right"""
        current = self.head
        count = 1
        if position > 1:
            while current and count < position:
                if count == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                count +=1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
         
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        
    def list_print(self):
        """prints a linked list"""
        thing = self.head
        blank = []
        while thing:
            blank.append(thing.value)
            thing = thing.next
        print blank

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted


class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
        
    def pop(self):
        return self.ll.delete_first()
 

# Initializing linked list and makings some values to insert
ll2 = LinkedList()

#a, b, c, d ARE EACH ONE INSTANCE OF ELEMENT CLASS
a = Element([3,21,4])
b = Element(['daf', 34])
c = Element(['paf', 'fa', (65, 5)])
d = Element(('saf','dasf',23))

#APPENDING INSTANCES ABC FROM CLASS ELEMENT TO A SINGLE LINKED LIST INSTANCE
ll2.append(a)
ll2.append(b)
ll2.append(c)

#print "This tests list_print"
#ll2.list_print()

#print "This tests get_position for position 2"
#print ll2.get_position(2).value

#print "This tests delete for ['paf', 'fa', (65, 5)]"
#ll2.delete(['paf', 'fa', (65, 5)])
#ll2.list_print()

#print "This tests insert for element d at position 2"
#ll2.insert(d, 2)
#ll2.list_print()


