# Dylan

class LyricParser():
    def __init__(self):
        self.START_MARK = '<div class="field-items">'
        self.END_MARK = '<div class="copyright">'
    
    def parse(self, html):
        htmlLyrics = self.findHtmlLyics(html)
        htmlLyrics = self.removeStartingSpace(htmlLyrics)
        lyrics = self.removeHtmlTags(htmlLyrics)
        return lyrics
        
    
    def findHtmlLyics(self,html):
        start = rainyDayHTML.find(self.START_MARK)
        end = rainyDayHTML.find(self.END_MARK)
        return html[start+len(self.START_MARK):end]
    
    def removeStartingSpace(self, html):
        html = html.replace('\t','')
        return html
    
    def removeHtmlTags(self, html):
        html = html.replace('<p>','')
        html = html.replace('</p>','')
        html = html.replace('<br>','')
        return html

rainyDayHTML = open('songs/RainyDay.htm','r').read()
parser = LyricParser()
rainyDay = parser.parse(rainyDayHTML)
print rainyDay
