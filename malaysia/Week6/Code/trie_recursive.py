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

    def insert_recursive(self, key, data=None):
        current = self.root
        self.insert_recursive_aux(current, key, data)

    def insert_recursive_aux(self, current, key, data=None):
        # Base Case
        if len(key) == 0:
            # Handle Terminal $
            current.link[0] = Node()
            current = current.link[0]
            current.data = data
            return
        else:
            index = (ord(key[0]) - 97) + 1
            # If path exist
            if current.link[index] is not None:
                current = current.link[index]
            # If path doesn't exist
            else:
                current.link[index] = Node()
                current = current.link[index]
                # Recursion
                self.insert_recursive_aux(current, key[1:], data)

    def search(self, key):
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
                return Exception(str(key) + " doesn't exist")
        # Go through the terminal $
        # If path exist
        if current.link[0] is not None:
            current = current.link[0]
        # If path doesn't exist
        else:
            return Exception(str(key) + " doesn't exist")
        return current.data

if __name__ == "__main__":
    bla = Trie()
    bla.insert_recursive("lol", "123")
    print(bla.search("lol"))
    