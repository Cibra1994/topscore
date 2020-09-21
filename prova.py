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
                print(f"Error {r.status_code}")
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
