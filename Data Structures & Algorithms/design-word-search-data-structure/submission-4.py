class TrieNode:
    def __init__(self, text=''):
        self.text = text
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root =  TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children :
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches
        word or false otherwise. word may contain dots '.' where dots can be
        matched with any letter.
        """
        def search_recursive(node: TrieNode, index: int) -> bool:
            if index == len(word):
                return node.is_word

            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if search_recursive(child, index + 1):
                        return True
                return False
            else:
                if char in node.children:
                    return search_recursive(node.children[char], index + 1)
                else:
                    return False

        return search_recursive(self.root, 0)
