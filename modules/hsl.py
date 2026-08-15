import requests
import re
import base64
import json 
def hsl():
    motiondata=''
    sitekey='4c672d35-0701-42b2-88c3-78380b0db560'
    def check_config(sitekey):
        headers = {
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "text/plain",
                "origin": "https://newassets.hcaptcha.com",
                "priority": "u=1, i",
                "referer": "https://newassets.hcaptcha.com/",
                "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "sec-fetch-storage-access": "active",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
            }
        r = requests.get("https://hcaptcha.com/1/api.js")
        version = re.search(r"v=([a-f0-9]+)", r.text).group(1)
        params = {
                "v": version,
                "host": "discord.com",
                "sitekey": sitekey,
                "sc": "1",
                "swa": "1",
                "spst": "1",
            }

        response = requests.post(
                "https://api.hcaptcha.com/checksiteconfig", params=params, headers=headers
            )
        req = response.json()[
                "c"
            ][
                "req"
            ]  
        payload = req.split(".")[1]
        payload += "=" * (4 - len(payload) % 4)

        decoded = json.loads(base64.b64decode(payload))
        c = response.json()["c"]
        l = decoded["l"]
        return l,req,version,c

    l,o_req,version,c=check_config("4c672d35-0701-42b2-88c3-78380b0db560")
    def hsj_req():
        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://newassets.hcaptcha.com",
            "priority": "u=1, i",
            "referer": "https://newassets.hcaptcha.com/",
            "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-fetch-storage-access": "active",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        }

        data = {
        '$v': version,
        'sitekey': sitekey,
        'host': 'accounts.hcaptcha.com',
        'hl': 'en',
        'motionData': motiondata,
        'n': 'fail',
        'c': json.dumps({
                    "type":"hsw",
                    "req": o_req
            }),

        }

        response = requests.post('https://api.hcaptcha.com/getcaptcha/4c672d35-0701-42b2-88c3-78380b0db560', headers=headers, data=data)
        req = response.json()[
                "c"
            ][
                "req"
            ]  
        payload = req.split(".")[1]
        payload += "=" * (4 - len(payload) % 4)

        decoded = json.loads(base64.b64decode(payload))
        c = response.json()["c"]
        l = decoded["l"]
        return l,req,version,c
    hsj_l,hsj_req,hsj_version,hsj_c=hsj_req()
    print(hsj_l,hsj_req,hsj_c)
    def hsl_req():
        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://newassets.hcaptcha.com",
            "priority": "u=1, i",
            "referer": "https://newassets.hcaptcha.com/",
            "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-fetch-storage-access": "active",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
        }

        data = {
        '$v': hsj_version,
        'sitekey': sitekey,
        'host': 'accounts.hcaptcha.com',
        'hl': 'en',
        'motionData': motiondata,
        'n': 'fail',
        'c': json.dumps({
                    "type":"hsj",
                    "req": hsj_req
            }),

        }

        response = requests.post('https://api.hcaptcha.com/getcaptcha/4c672d35-0701-42b2-88c3-78380b0db560', headers=headers, data=data)
        req = response.json()[
                "c"
            ][
                "req"
            ]  
        payload = req.split(".")[1]
        payload += "=" * (4 - len(payload) % 4)

        decoded = json.loads(base64.b64decode(payload))
        c = response.json()["c"]
        l = decoded["l"]
        return l,req,version,c
    l,req,version,c=hsl_req()


    def js_link(js:str):
        url = f"https://newassets.hcaptcha.com" + l + "/"+ str(js)
        print(url)
        url_t = requests.get(url).text
        #print("got hsl js length:", len(url_t))  # print the length of hsl.js
        return url_t

    url_t=js_link("hsl.js")

    def js_execute(url_t):



        from camoufox.sync_api import Camoufox

        with Camoufox(headless=True) as browser:
            page = browser.new_page()
            page.evaluate(url_t)
            n_val = page.evaluate(f'hsl("{req}")')
            print(f"result {n_val}")
            return(n_val)
    # get cap

    n_val=js_execute(url_t)

    h = {
        "accept": "application/json",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://newassets.hcaptcha.com",
        "referer": "https://newassets.hcaptcha.com/",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
    }

    data = {
        "v": version,
        "sitekey": sitekey,
        "host": "discord.com",
        "hl": "en-US",
        "n": n_val,
        "c": json.dumps(c),
    }


    getcap = requests.post(
        f"https://api.hcaptcha.com/getcaptcha/{sitekey}",
        headers=h,
        params={
            "v": version,
            "host": "discord.com",
            "sitekey": sitekey,
        },
        data=data,
    )

    print(getcap.status_code)
    print(getcap.json())

    import os

    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    res_path = os.path.join(root_dir, 'res.json')

    with open(res_path, 'w') as f:
        json.dump(getcap.json(), f, indent=4)
