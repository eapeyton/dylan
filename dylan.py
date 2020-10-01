# Dylan


import random
import RhymeFinder

class Dylan:
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
            return "No rhymes found...\n"
        random.shuffle(rhymes)
        for word in rhymes:
            if word.lower() in self.lastWordDict:
                rhymingLine = self.lastWordDict[word.lower()]
                if rhymingLine != line:
                    return rhymingLine
        return "No rhymes found...\n"
    def findRandomLine(self):
        return random.choice(self.lyricsLines)
    def generateRhymeScheme(self,rhymeScheme):
        rhymeScheme = rhymeScheme.upper()
        output = []
        scheme = {}
        for letter in rhymeScheme:
            if letter == 'X':
                output.append(self.findRandomLine())
            elif letter == ' ':
                output.append('\n')
            elif letter not in scheme:
                scheme[letter] = self.findRandomLine()
                output.append(scheme[letter])
            else:
                rhyming = self.findRhymingLine(scheme[letter])
                if rhyming in output:
                    rhyming = self.findRhymingLine(scheme[letter])
                output.append(rhyming)
        return ''.join(output)
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

def generateLines():
    dylan = Dylan()
    numLines = input('How many lines? ')
    while(numLines != 'exit'):
        print('')
        print(dylan.generateLyrics(int(numLines)))
        numLines = input('How many more? ')


if __name__ == "__main__":
    dylan = Dylan()
    print(dylan.generateRhymeScheme('AA BB CC DD'))
    # generateLines()