class Browser:
    def __init__(self):
        self.history = []  
        self.index_skr = -1  
    
    def go(self, url):
        self.history = self.history[:self.index_skr+1] + [url]
        self.index_skr += 1
    
    def back(self):
        if self.index_skr > 0:
            self.index_skr -= 1
    
    def forward(self):
        if self.index_skr < len(self.history) - 1:
            self.index_skr += 1
    
    def printAll(self):
        for url in self.history:
            print(url)
browser = Browser()

browser.go("https://google.com")

browser.go("https://ukdw.ac.id")

browser.go("https://facebook.com")

browser.back() #output: https://ukdw.ac.id

browser.back() #output: https://google.com

browser.forward() #output: https://ukdw.ac.id

browser.go("https://twitter.com") 

browser.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com
