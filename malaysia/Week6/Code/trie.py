"""
Simple implementation of Trie (Iterative)
> Sorting make easy for strings
    - Edges or links are in-order (from a to z)
    - O(MN) complexity
> However, may sometimes be slower than hash table (rare)
> Wasted space if the self.link array is left empty most of the time
"""


class Node:
    def __init__(self, data=None, level=None, size=27):
        # Terminal $ at index 0
        self.link = [None] * size
        # Data payload
        self.data = data
        # Terminal value
        self.terminal = True
        # Level of pointer
        self.level = level

class Trie:
    def __init__(self):
        self.root = Node(level=0)

    def insert(self, key, data=None):
        count_level = 1
        # Being from root
        current = self.root
        # Go through the key 1 by 1
        for char in key:
            # Calculate index
            index = (ord(char) - 97) + 1
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path doesn't exist
            else:
                current.link[index] = Node(level=count_level)
                current = current.link[index]
            count_level += 1
        # Go through the terminal $
        # If path exist
        if current.link[0] is not None:
            current = current.link[0]
        # If path doesn't exist
        else:
            current.link[0] = Node(level=count_level)
            current = current.link[0]
        # Add in the payload
        current.data = data
        

    def search(self, key):
        """
        O(M) Time Complexity, where M is length of the string
        """
        # Being from root
        current = self.root
        # Go through the key 1 by 1
        for char in key:
            # Calculate index
            index = (ord(char) - 97) + 1
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path doesn't exist
            else:
                return Exception(str(key) + "doesn't exist")
        # Go through the terminal $
        # If path exist
        if current.link[0] is not None:
            current = current.link[0]
        # If path doesn't exist
        else:
            return Exception(str(key) + "doesn't exist")
        print(f'Levels Descended = {current.level}')
        return current.data

if __name__ == "__main__":
    bla = Trie()
    bla.insert("lol", "123")
    print(bla.search("lol"))
    