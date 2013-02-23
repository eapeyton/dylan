# Dylan


import random
import RhymeFinder

class Dylan():
    def __init__(self):
        self.lyricsLines = open('files/lyrics.txt','r').readlines()
        self.lastWordDict = self.mapLinesToLastWord(self.lyricsLines)
        self.rhymer = RhymeFinder.RhymeFinder()
    def removePunct(self,word):
        for punct in ['\x92','\x93','\x94',',','.','!','?','"']:
                word = word.replace(punct,'')
        return word
    def mapLinesToLastWord(self,lyricsLines):
        lastWords = {}
        for line in lyricsLines:
            last = self.removePunct(line.split()[-1])
            lastWords[last] = line
        return lastWords
    def findRhymingLine(self,line):
        lastWord = self.removePunct(line.split()[-1])
        try:
            rhymes = self.rhymer.findRhymes(lastWord)
        except KeyError:
            return "No rhymes found..."
        for word in rhymes:
            if word.lower() in self.lastWordDict:
                if self.lastWordDict[word.lower()] is not line:
                    return self.lastWordDict[word.lower()]
        return "No rhymes found..."
    def findRandomLine(self):
        return random.choice(self.lyricsLines)
    def generateLyrics(self,numLines):
        lyrics = ''
        pairs = numLines / 2
        leftover = numLines % 2
        for pair in range(pairs):
            randomLine = self.findRandomLine()
            rhymingLine = self.findRhymingLine(randomLine)
            lyrics += randomLine
            lyrics += rhymingLine
        for line in range(leftover):
            lyrics += self.findRandomLine()
        return lyrics


dylan = Dylan()
numLines = raw_input('How many lines? ')
while(numLines != 'exit'):
    print ''
    print dylan.generateLyrics(int(numLines))
    numLines = raw_input('How many more? ')


