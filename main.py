class node:
    # This is just a structure
    def __init__(self):
        self.data = ""
        self.freq = 0
        self.left = None
        self.right = None
# End of class

class HuffmanEncoding:
    def getKey(self, n):
        return n.freq


    def printDict(self, root, s):
        # This function will print the char, freq, corresponding code
        if root.left == None and root.right == None and root.data != '-':
            print(root.data, ": ", root.freq, "->", s)
            return
        print(root.data)
        self.printDict(root.left, s + "0")
        self.printDict(root.right, s + "1")


    def createTree(self, charDict):
        node_list = []
        # Creating a list of nodes
        for data in charDict:
            freq = charDict[data]
            n = node()
            n.data = data
            n.freq = freq
            node_list.append(n)
        # End of for loop
        node_list = sorted(node_list, key = self.getKey)

        # Start creating the tree
        self.root = node()
        
        while len(node_list) > 1:
            a = node_list[0]
            b = node_list[1]

            node_list.pop(0)    # Remove a 
            node_list.pop(0)    # Remove b

            temp = node()
            temp.data = '-'
            temp.freq = a.freq + b.freq
            temp.left = a
            temp.right = b

            self.root = temp

            node_list.append(temp)
            node_list = sorted(node_list,  key = self.getKey)
            


def main():
    temp = {
        "b" : 9,
        "a" : 5,
        "f" : 45,
        "c" : 12,
        "d" : 13,
        "e" : 16
    }
    h = HuffmanEncoding()
    h.createTree(temp)
    h.printDict(h.root, "")

if __name__ == '__main__':
    main()
