from requests_html import HTMLSession

sessie = HTMLSession()

stad = 'Las Vegas'
url = f'https://www.google.com/search?q=weather+{stad}'

r = sessie.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first=True).text
eenheid = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
beschrijving = r.html.find('span#wob_dc', first=True).text.lower()

print(f'In {stad} is het {temp}{eenheid} en {beschrijving}!')