import requests

class HMrequest:
    def nekosGet(name):
        blacklist = ['', '', '', '']
        json = requests.get(f"https://nekos.life/api/v2/img/{name}").json()
        if json["url"] in blacklist:
            return HMrequest.nekosGet(name)
        return json

    def nekoloveGet(name):
        return requests.get(f"https://nekos.life/api/v2/img/{name}").json()

    def nekobotGet(name):
        blacklist = ['', '', '', '', '', '']
        req = requests.get(f"https://nekobot.xyz/api/image?type={name}")
        if not req.status_code == 200:
            return print('This endpoint don\'t work, or you got a Rate Limit')
        if req.json()["message"] in blacklist:
            return HMrequest.nekobotGet(name)
        return {"url": req.json()["message"]}

    def freakerGet(name):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
        }
        return requests.get(f"https://api.computerfreaker.cf/v2/{name}", headers=headers).json()

        
