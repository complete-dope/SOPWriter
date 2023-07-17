from bs4 import BeautifulSoup as bs


import requests
import time

class GetPDf():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    payload = {
        'json': 1
    }
    session = requests.Session()


    def __init__(self):
        self.response = None
        # self.session = session
        # here we will take the link and pass a request to the page 
        None
    
    
    def getvalues(self):
        prelink = 'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYN86KEAAAAJ&pagesize=100&citation_for_view=iYN86KEAAAAJ:5nxA0vEk-isC'

        self.response =  self.session.post(url= prelink , headers = self.headers , data = self.payload)


        if not self.response.ok:
            raise Exception('Gone :/')

        print("\n")
        print("\n")
        print("decoded response ")
        print("\n")
        print("\n")
        # print(self.response.content.decode())
        self.response = self.response.content.decode()
        self.articles = bs(self.response, 'html.parser')
        div1 = self.articles.find("div" , {"id" : "gsc_oci_title"})
        # print(div1)
        link = div1.find('a')

        # if link is a arxiv link ( call arxiv function )
        title = link.contents[0]
        link = link['href']
        # print("the title is , " , title , " the link  is " , link)

    def Arxivlink(self,link):
        # https://arxiv.org/search/?query=ian+goodfellow&searchtype=author&abstracts=show&order=-announced_date_first&size=200

        

        None

    def Neurips(self,link)
        


if __name__ == '__main__':
    print(
        "the values "
    )
    instn = GetPDf()
    instn.getvalues()


