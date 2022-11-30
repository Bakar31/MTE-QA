import requests
from bs4 import BeautifulSoup

base_url = 'https://www.google.com/search'
params = {
    'q': 'mechatronics+engineering',
    'oq': 'mechatronics+engineering',
    'aqs' : 'chrome..69i57j46i20i175i199i263i512j0i512l4j69i61l2.9576j0j7',
    'sourceid' : 'chrome',
    'ie': "UTF-8"
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; HSID=AenmNVZxnoADsXz_x; SSID=AjbLhhwkjh8f3FOM8; APISID=IqkNtUA0V2DXlees/A0tA9iPSadMC2X6dt; SAPISID=8-N4B06I_D5N1mvR/AleccT6Zt0QllrukC; CONSENT=YES+UA.en+; OTZ=5204669_48_48_123900_44_436380; SID=rAd3UAFN_dCIGQ87HqDZZGiNyxdz0dL4dZKy_XquqSr_CHTzqSzfDdNTfLmA2xCMEZOZMA.; ANID=AHWqTUnDWUSHdvWhJiIoPxMAKYXmVtHCQIq7LBMYgiSlZZr3AMGTwY2aVUdjeY7z; NID=193=QImFbOa1vnKpflG8yJytqPXbJYJ9k8fWbIzQMGExsMa4g5oJwdnI56WNjgEVFAyAPJ1SEEOQ-zlW4HAUv-JLj0yAUImTgeT1syDIgFTMWAqxdz10lWRlzFC-3Fmjv6xJcqm2o6RKI50dmb7GetiheNdSAYPkAjng_c0lOHoXZLmtMwFOpkPTrQwVyUW8R2x4o1ux3OW3_kEbR_BREowRV8lVqrsnyo1ffC_Pm40zf81k7aS0cv9esYweGHF6Lxd532z4wA; 1P_JAR=2019-12-06-16; DV=k7BRh0-RaJtZsO9g7sjbrkcKoUjC7RYhxDh5AdfYgQAAAID1UoVsAVkvPgAAAFiry7niUB6qLgAAAGCQehpdCXeKnikKAA; SEARCH_SAMESITE=CgQIvI4B; SIDCC=AN0-TYv-lU3aPGmYLEYXlIiyKMnN1ONMCY6B0h_-owB-csTWTLX4_z2srpvyojjwlrwIi1nLdU4',
    'pragma': 'no-cache',
    'referer': 'https://www.google.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.142 Chrome/75.0.3770.142 Safari/537.36'
}

response = requests.get(base_url, params=params, headers=headers)
content = BeautifulSoup(response.text, 'lxml')
# next_pages = []

# for page in range(2, 10):
#     next_page = content.find('a', {'aria-label' : 'Page ' + str(page)}).get('href')
#     next_page = base_url + next_page
#     next_pages.append(next_page)
# print(next_pages)

results = []
links = [link.next_element['href'] for link in content.find_all(class_ = 'yuRUbf')]
for index in range(0, len(links)):
    results.append({'link': links[index]})

# for page_url in next_pages:
#     print(page_url)
#     response = requests.get(page_url)
#     content = BeautifulSoup(response.text, 'lxml')
#     links = [link.next_element['href'] for link in content.find_all(class_ = 'yuRUbf')]
#     print(content)
#     for index in range(0, len(links)):
#         results.append({'link': links[index]})
print(len(results))
print(results)

content = []
for link in results:
    url = link['link']
    print('Trying url: {}..'.format(url))
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        body = soup.find('body')
        paragraphs = body.find_all('p')
        texts = [text.text for text in paragraphs]
        for text in texts:
            content.append(text.strip())
        
    except:
        pass

# print(content)
with open('raw_text.txt', 'w') as f:
    for line in content:
        f.write(f"{line}\n")