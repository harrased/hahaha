import phonenumbers, requests, os
from phonenumbers import geocoder, carrier, timezone, prefix
from colorama import Fore, init
init()
_countrycode = input(f"{Fore.WHITE}[{Fore.YELLOW}^{Fore.WHITE}] Enter Country Code > ")
number = input(f"{Fore.WHITE}[{Fore.YELLOW}^{Fore.WHITE}] Enter Number > ")
target = _countrycode+number
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Commencing Phonenumbers API Scan")
try:
  _number = phonenumbers.parse(target)
except:
  print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Invalid Number")
  input()
print(f"{Fore.WHITE}[*{Fore.WHITE}] Finished Phonenumbers API Scan")
_location = geocoder.description_for_number(_number, "en")
_carrier = carrier.name_for_number(_number, "en")
_timezone = timezone.time_zones_for_number(_number)
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Location: {_location}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Carrier: {_carrier}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Timezone: {_timezone}")
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Creating Google Dork Links")
query1 = target.replace("+", "%2B")
query2 = target.replace("+", "")
_dork_general = f'https://www.google.com/search?q=intext:"{query1}"+OR+intext:"{query2}"'
_dork_facebook = f'https://www.google.com/search?q=site:facebook.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_youtube = f'https://www.google.com/search?q=site:youtube.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_tiktok = f'https://www.google.com/search?q=site:tiktok.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_twitter = f'https://www.google.com/search?q=site:twitter.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_vk = f'https://www.google.com/search?q=site:vk.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_linkedin = f'https://www.google.com/search?q=site:linkedin.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_insta = f'https://www.google.com/search?q=site:instagram.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_snap = f'https://www.google.com/search?q=site:snapchat.com+intext:"{query1}"+OR+intext:"{query2}"'
_dork_whatsapp = f'https://www.google.com/search?q=site:whatsapp.com+intext:"{query1}"+OR+intext:"{query2}"'
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Finished Creating Google Dork Links")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] General Dork: {Fore.GREEN}{_dork_general}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Facebook Dork: {Fore.GREEN}{_dork_facebook}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Youtube Dork: {Fore.GREEN}{_dork_youtube}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Tiktok Dork: {Fore.GREEN}{_dork_tiktok}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Twitter Dork: {Fore.GREEN}{_dork_twitter}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] VK Dork: {Fore.GREEN}{_dork_vk}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Linkedin Dork: {Fore.GREEN}{_dork_linkedin}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Insta Dork: {Fore.GREEN}{_dork_insta}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Snapchat Dork: {Fore.GREEN}{_dork_snap}")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Whatsapp Dork: {Fore.GREEN}{_dork_whatsapp}")
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Checking For Number On Account APIs")
requests.session()
head = {
  'accept': '*/*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  'content-length': '55',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'ig_did=C85526B3-D56D-4C62-9955-A0FEDCEEF1B2; mid=XtRWJAALAAGDUx-1-NNLph8FvNQS; shbid=13522; shbts=1593969544.8718596; rur=FRC; csrftoken=92L3g6joMsjBqf61UOsQmjpoHf3reSFv; urlgen="{\"2001:16a2:1339:aa00:4c09:f79e:5aa3:bca3\": 25019}:1jsLuJ:SeoqLoKY8TPu7D3BCIcgfDXOm7Q"',
  'dnt': '1',
  'origin': 'https://www.instagram.com',
  'referer': 'https://www.instagram.com/accounts/password/reset/',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
  'x-csrftoken': '92L3g6joMsjBqf61UOsQmjpoHf3reSFv',
  'x-ig-app-id': '936619743392459',
  'x-ig-www-claim': 'hmac.AR20oU9cC9AGn6Sd8PyDrHogb3ZFG9fAWLqSuqNBSRHpj0Ll',
  'x-instagram-ajax': 'fc31028544fb',
  'x-requested-with': 'XMLHttpRequest'
}
url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"
data = {
  'email_or_username': target
}
res = requests.post(url, data=data, headers=head).text
if '{"message":"No users found","status":"fail"}' == res:
  _insta = f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Instagram: {Fore.RED}Number Not Found"
else:
  _insta = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Instagram: {Fore.GREEN}Number Found"


url = "https://accounts.snapchat.com/accounts/validate_phone_number"
headers = {
  "Host": "accounts.snapchat.com",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
  "Accept": "*/*",
  "Accept-Language": "ar,en-US;q=0.7,en;q=0.3",
  "Accept-Encoding": "gzip, deflate",
  "Referer": "https://accounts.snapchat.com/",
  "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
  "Origin": "https://accounts.snapchat.com",
  "Content-Length": "79",
  "Connection": "close",
  "Cookie": "xsrf_token=v6zFgDFj8T7ofkai_gggDQ"
}
data = 'phone_country_code=' + _countrycode + '&phone_number=' + number + '&xsrf_token=v6zFgDFj8T7ofkai_gggDQ'
res = requests.request("POST", url, data=data, headers=headers).text
if ('"error_message":"Phone number is taken."') in res:
  _snap = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Snapchat: {Fore.GREEN}Number Found"
elif ('"error_message":"Phone number is invalid."') in res:
  _snap = f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Snapchat: {Fore.RED}Number Not Found"
else:
  _snap = f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Snapchat: {Fore.YELLOW}Error"


url = 'https://twitter.com/account/begin_password_reset'
hdtiwit={
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': '_sl=1; personalization_id="v1_8HR67vKTQ8FVjONj2mmA1g=="; guest_id=v1%3A160719378482004005; at_check=true; mbox=session#ea647a3cb75243d08272db60d50ed2b9#1607303352|PC#ea647a3cb75243d08272db60d50ed2b9.38_0#1670546293; ct0=45e20553d29d34b447fa835d48979bfc; gt=1339043747477270528; att=1-TGEnll9aQohZv842f7vHhakxTtvDWXe0NTgbXx74; _twitter_sess=BAh7CiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCJhZNzR2AToMY3NyZl9p%250AZCIlZWJiZDEyOWY5MjM5NmQyNjQzYWYwOGQ2ZWFiZmM2ZmY6B2lkIiUwYmM3%250AZjNiNzk3OWM0NWNkMTRmZDkzN2Q5ZDE1YTI5ZiIJcHJycCIA--0a7350c997dffea474dd6738ac5b77ca41add0e2; fm=V2UgZm91bmQgbW9yZSB0aGFuIG9uZSBhY2NvdW50IHdpdGggdGhhdCBwaG9u%250AZSBudW1iZXIuIFBsZWFzZSB0cnkgYWdhaW4gd2l0aCB5b3VyIHVzZXJuYW1l%250AIG9yIGVtYWlsLg%253D%253D--6bf96c51ecbe639da7edb8388c25ed8f705ec556',
  'referer': url,
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'sec-gpc': '1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'
}
dttwit={
  'authenticity_token': '560d4242d28e65b0e9a00788e5f6a93502d519fe',
  'account_identifier': target
}
tiwt = requests.post(url, data=dttwit, headers=hdtiwit).text
if ('We found more than one account with that phone number') in tiwt:
  _twitter = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Twitter: {Fore.GREEN}Number Found"
elif ("We couldn't find your account with that information") in tiwt:
  _twitter = f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Twitter: {Fore.RED}Number Not Found"
else:
  _twitter =f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] Twitter: {Fore.YELLOW}Error"
print(f"{Fore.WHITE}[{Fore.YELLOW}*{Fore.WHITE}] Finished Checking Number On Account APIs")
print(_snap)
print(_insta)
print(_twitter)
