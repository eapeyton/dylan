import os.path

class LyricParser():
    def __init__(self):
        self.START_MARK = '<div class="field-items">'
        self.END_MARK = '<div class="copyright">'
    
    def parse(self, html):
        htmlLyrics = self.findHtmlLyics(html)
        htmlLyrics = self.removeStartingSpace(htmlLyrics)
        lyrics = self.removeHtmlTags(htmlLyrics)
        lyrics = self.removePunctuation(lyrics)
        lyrics = lyrics.lower()
        return lyrics
    
    def findHtmlLyics(self,html):
        start = html.find(self.START_MARK)
        end = html.find(self.END_MARK)
        return html[start+len(self.START_MARK):end]
    
    def removeStartingSpace(self, html):
        while(html[0] in [' ','\t','\n']):
            html = html[1:]
        return html
    
    def removeHtmlTags(self, html):
        for tag in ['<p>','</p>','<br>','<br />']:
            html = html.replace(tag,'')
        return html

    def removePunctuation(self, lyrics):
        for punct in ['\x92','\x93','\x94',',','.','!','?','"']:
            lyrics = lyrics.replace(punct,'')
        return lyrics
    
def parseAndWrite():
    output = open('test.txt','w')
    parser = LyricParser()

    for root, _, files in os.walk('songs'):
        for file in files:
            print file
            filePath = os.path.join(root,file)
            fileHTML = open(filePath,'r').read().decode('utf-8')
            lyrics = parser.parse(fileHTML)
            output.write(lyrics)
            
    output.close()

def wordCount():
    allLyrics = open('files/alllyrics.txt','r').read().lower().split()
    
    wordCount = {}
    
    for word in allLyrics:
        if word in wordCount:
            wordCount[word] +=1
        else:
            wordCount[word] = 1
    
    output = open('files/output.txt','w')
    
    for word in sorted(wordCount,key=wordCount.get, reverse=True):
        output.write(word + ': ' +str(wordCount[word]) + '\n') 
