import requests
import json
from bs4 import BeautifulSoup
import time



class Main():

    def __init__(self):

        self.s = requests.Session()
        self.url = 'http://www.topscore90.net/Holder.bet?page=sport'
        self.quote_topscore= "http://www.topscore90.net/res/Client/wbe/proxybetting.aspx?method=WIDGET_LIST&type=json&st=mm&wts=BS,NE&ts=1600696795291"
        self.quote_betn1='https://oddsfeed2.betn1.com/oddsfeed/lite/loadData/highlightDataJSON.jsp?langtag=it-IT-bn1'
        self.caricoquote_betn1()
        self.parser_betn1()
        self.stampa_betn1()
       


      
        
  

    def caricoquote_topscore(self):

        try:

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'it',
                'Connection': 'keep-alive',
                'Host': 'www.topscore90.net',
                'Origin': 'http://www.topscore90.net',
                'Referer': 'http://www.topscore90.net/Holder.bet?page=sport',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            }

            r = self.s.get(self.quote_topscore, headers = headers)

            if r.status_code == 200:
                
                self.formato_json_topscore=json.loads(r.text)
            
                print(json.dumps(self.formato_json_topscore, indent=4, sort_keys=True))

            else:
                print(f"Error {r.status_code}")
                time.sleep(10)

        except Exception as e :
            print(e)
            
    def caricoquote_betn1(self):

        try:

            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'it',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            }

            r = self.s.get(self.quote_betn1, headers = headers)

            if r.status_code == 200:
                
                self.formato_json_betn1=json.loads(r.text)
            
                print(json.dumps(self.formato_json_betn1, indent=4))

            else:
                print(f"Error {r.status_code}")
                time.sleep(10)

        except Exception as e :
            print(e)
   
    def parser_betn1(self):
      
        try:
            self.uno=[]
            self.x=[]
            self.due=[]
            self.nome=[]
            self.codice=[]
            self.quote=[]
            
            for element in self.formato_json_betn1:
                if 'avvenimenti'in element:
                    h=element['avvenimenti']
                    for elementiii in range(len(h)):
                        l=h[elementiii]['desc']
                        self.nome.append(l)
                        
                    
                   
                if 'scommesse' in element:
                    a=element['scommesse']
                    for elementi in a:
                        if 'quote'in elementi:
                            b=elementi['quote']
                            c=elementi['quoteOrdinate']
                            for elementii in range(len(c)):
                                f='{}'.format(c[elementii])
                                if b[f]["descE"]=='1':
                                    d=b[f]['vt']
                                    self.uno.append(d)
                                if b[f]["descE"]=='X':
                                    d=b[f]['vt']
                                    self.x.append(d)
                                if b[f]["descE"]=='2':
                                    d=b[f]['vt']
                                    self.due.append(d)
                quote=zip(self.uno,self.x,self.due)
                quote_list=list(quote)
                partita=zip(self.nome,quote_list)
                self.partita_list=list(partita)
 
                
        except Exception as e :
            
            print(e)



   
    def parser_topscore(self):
        self.quote_topscore=[]
      

     








            
    def stampa_topscore(self):
        
         
        try:
              for x in range(len(self.formato_json_topscore['ListData_BS'])):
                  print (json.dumps(self.nome_evento[x],indent=3))
                  print ("1:",json.dumps(self.quote_uno[x],indent=3),"X:",json.dumps(self.quote_X[x],indent=3),"2:",json.dumps(self.quote_due[x],indent=3),'Cagnotta:',(100/float(self.quote_uno[x])+100/float(self.quote_X[x])+100/float(self.quote_due[x])))
            

        except Exception as e :
                    
                        print(e)
    def stampa_betn1(self):
         
        try:
            
                print(self.partita_list)
                
          
            
        except Exception as e :
                    
                        print(e)



   
if __name__ == "__main__":
    Main()
