import requests
import re
import base64
import json
import playwright.sync_api as sync_playwright

sitekey = "a9b5fb07-92ff-493f-86fe-352a2803b3df"
headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    # 'content-length': '0',
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
print(f"version: {version}")
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
# print(response.json())
req = response.json()[
    "c"
][
    "req"
]  # so we get the middle value which is payload , btw there there three parts in that req first one header , middle one is payload and last one is signature
print(req)
payload = req.split(".")[1]
payload += "=" * (4 - len(payload) % 4)

decoded = json.loads(base64.b64decode(payload))
print(f"Decoded the payload{decoded}")
c = response.json()["c"]
l = decoded["l"]
# print(l)
print(c)
hsw_url = "https://newassets.hcaptcha.com" + l + "/hsw.js"
print(hsw_url)
hsw = requests.get(hsw_url).text
print("got hsw js length:", len(hsw))  # print the length of hsw.js


# hsw stuff


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.evaluate(hsw)  # we store the loaded hsw function
    n_val = page.evaluate(f'hsw("{req}")')  # get n value
    print(f"result {n_val}")  # print n value
# get cap

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
#print(getcap.headers.get("content-type")) keep it for debugging purposes
print(getcap.json())
