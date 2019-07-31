class TrieNode:
# Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    '''
    构建字典树，a->p->p->l->e  root.children = {a:TrieNode}
    '''

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)#get方法，如果不存在该键，则返回None，与defaultdict区别，
                                                  #只有在给dic赋予dic中不存在的键时，才会返回defaultdict中的默认值
            if current is None:                  #例如键1不存在，a[1]=默认值
                return False
        return current.is_word#如果是一模一样的两个词，则最后一个节点为True

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True