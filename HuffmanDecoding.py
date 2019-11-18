class HuffmanDecoding:
    def extractBinary(self, encodedString):
       
        # function :
        #   1. convert char to ascii
        #   2. ascii to binary
        #   3. remove padding
        #   4. concatenate into 1 string
        self.binaryString = ""
        self.extraZeroes = int(encodedString[0])
        for i in range(1, len(encodedString)):
            temp = bin(ord(encodedString[i]))
            print(temp)
            self.binaryString += temp[2:]

        self.binaryString = self.binaryString[0: len(self.binaryString)-self.extraZeroes]
        print(self.binaryString)



d = HuffmanDecoding()
with open("compressed.dat", "r") as file:
    text = file.read()
d.extractBinary(text)
