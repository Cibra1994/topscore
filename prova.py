import requests
import json
from bs4 import BeautifulSoup
import time



class Main():

    def __init__(self):

        self.s = requests.Session()

        self.url = 'http://www.topscore90.net/Holder.bet?page=sport'
        self.quote = "http://www.topscore90.net/res/Client/wbe/proxybetting.aspx?method=WIDGET_LIST&type=json&st=mm&wts=BS,NE&ts=1600696795291"

        self.get_page()



    def get_page(self):

        try:

            print("Getting product page...")

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'it',
                'Connection': 'keep-alive',
                'Host': 'www.topscore90.net',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
            }

            r = self.s.get(self.url, headers = headers)

            if r.status_code == 200:

                print("Got product page")
                self.caricoquote()

            else:
                print(f"Error {r.status_code}")import requests
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
            
                print(json.dumps(self.formato_json_betn1, indent=4, sort_keys=True))

            else:
                print(f"Error {r.status_code}")
                time.sleep(10)

        except Exception as e :
            print(e)

    def parser_betn1(self):
        self.nome_partita_betn1=[]
        self.nome_betn1=[]
        self.quote_betn1=[]
        self.quote_uno_betn1=[]
        try:
            
            
            for self.eventi_betn1 in range(len(self.formato_json_betn1)):
                
                if self.formato_json_betn1[self.eventi_betn1]['_bsolType']=='avv':
                    
                    self.nome_partita_betn1.append(self.formato_json_betn1[self.eventi_betn1]['avvenimenti'][0]['desc'])
            for self.quote in range(len(self.formato_json_betn1)):
                  if self.formato_json_betn1[self.quote]['_bsolType']=='scomm':
                       self.quote_betn1.append(self.formato_json_betn1[self.quote]['scommesse'][0]['quoteOrdinate'][0])
                       float i = self.quote_betn1[0]
                       
                       self.quote_uno_betn1.append(self.formato_json_betn1[self.quote]['scommesse'][0]['quote'][i])
                                           
  

        except Exception as e :
            
            print(e)



   
    def parser_topscore(self):
        self.nome_evento=[]
        self.dettagli_evento=[]
        self.dettagli_singolo_evento=[]
        self.quote_uno=[]
        self.quote_due=[]
        self.quote_X=[]

        try:
            
            
            for self.eventi in range(len(self.formato_json_topscore['ListData_BS'])):
                self.nome_evento.append(self.formato_json_topscore['ListData_BS'][self.eventi]['EventName'])
                self.dettagli_evento.append(self.formato_json_topscore['ListData_BS'][self.eventi]['GameDetails'])
                self.elementi=0;
                for self.elementi in range(len( self.dettagli_evento[self.eventi])):
                    if self.dettagli_evento[self.eventi][self.elementi]['GameAlias']=='Finale 1X2':
                        if self.dettagli_evento[self.eventi][self.elementi]['GameName'] == '1':
                            self.quote_uno.append(self.dettagli_evento[self.eventi][self.elementi]['GameOdd'])
                            
                        if self.dettagli_evento[self.eventi][self.elementi]['GameName'] == 'X':
                            self.quote_X.append(self.dettagli_evento[self.eventi][self.elementi]['GameOdd'])
                        if self.dettagli_evento[self.eventi][self.elementi]['GameName'] == '2':
                            self.quote_due.append(self.dettagli_evento[self.eventi][self.elementi]['GameOdd'])        
                    
                                    
                

        except Exception as e :
            
            print(e)
            








            
    def stampa_topscore(self):
         
        try:
              for x in range(len(self.formato_json_topscore['ListData_BS'])):
                  print (json.dumps(self.nome_evento[x],indent=3))
                  print ("1:",json.dumps(self.quote_uno[x],indent=3),"X:",json.dumps(self.quote_X[x],indent=3),"2:",json.dumps(self.quote_due[x],indent=3),'Cagnotta:',(100/float(self.quote_uno[x])+100/float(self.quote_X[x])+100/float(self.quote_due[x])))
            

        except Exception as e :
                    
                        print(e)
    def stampa_betn1(self):
         
        try:
            print(json.dumps(self.quote_betn1,indent=3))
            print(json.dumps(self.quote_uno_betn1,indent=3))
        except Exception as e :
                    
                        print(e)



   
if __name__ == "__main__":
    Main()

                time.sleep(10)

        except Exception as e :
            print(e)


    def caricoquote(self):

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

            r = self.s.post(self.quote, headers = headers)

            if r.status_code == 200:

                print(r.text)
                self.covertitore_json()
            else:
                print(f"Error {r.status_code}")
                time.sleep(10)

        except Exception as e :
            print(e)



    def covertitore_json(self):
            
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
            r = self.s.post(self.quote, headers = headers)
                
            formato_json=json.loads(r.text)
                
            print(json.dumps(formato_json, indent=4, sort_keys=True))

        except Exception as e :
                 print(e)


if __name__ == "__main__":
    Main()
