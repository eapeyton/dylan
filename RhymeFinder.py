

class RhymeFinder():
    def makeRhymeDict(self):
        dictText = open('files/rhymingdict.txt','r')
        rhymes = {}
        for line in dictText.readlines():
            tokens = line.split()
            word = tokens.pop(0)
            rhymes[word] = self.findTrialingKey(tokens)
        return rhymes
    
    def __init__(self):
        self.rhymeDict = self.makeRhymeDict()
    
    def findRhymes(self,word):
        rhymeKey = self.rhymeDict[word.upper()]
        matchingWords = self.findMatchingWords(rhymeKey)
        return matchingWords

    def findTrialingKey(self, rhymeKey):
        for key in reversed(rhymeKey):
            if self.isAVowel(key):
                return self.trimKey(rhymeKey,key)

    def trimKey(self, rhymeKey, key):
        return rhymeKey[(len(rhymeKey)-rhymeKey[::-1].index(key))-1:]

    def findMatchingWords(self, rhymeKey):
        matching = []
        for word in self.rhymeDict:
            if self.rhymeDict[word] == rhymeKey:
                matching.append(word)
        return matching
                
    def isAVowel(self,key):
        if len(key) > 0:
            if key[0] in ['A','E','I','O','U']:
                return True
        return False
    
        