from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of a character 't'
    def get_index(self, t):
        return ord(t) - ord('a')
        # ord(): Given a string of length one,
        # returns an integer representing the Unicode code of the character.

    # Function to insert a key in the Trie
    def insert(self, key):
        # None keys are not allowed
        if key is None:
            return
        key = key.lower()  # Keys are stored in lowercase
        current_node = self.root
        index = 0  # To store the character index

                # Iterate the trie with the given character index,
        # If the index points to None
        # simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                print(key[level] + " inserted")

            current_node = current_node.children[index]

        # Mark the end character as leaf node
        current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current_node = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node is not None and current_node.is_end_word:
            return True

        return False
        # Iterate the Trie with given character index,
        # If it is None at any point then we stop and return false
        # We will return true only if we reach leafNode and have traversed the
        # Trie based on the length of the key






    # Function to delete given key from Trie
    def delete(self, key):
        pass
trie = Trie()
print(trie.get_index('f'))


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i])


# Search for different keys
if t.search("the") is True:
    print("the --- " + output[1])
else:
    print("the --- " + output[0])

if t.search("these") is True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc") is True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[0])