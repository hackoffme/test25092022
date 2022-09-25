from http.client import HTTPException
import requests
import xmltodict
def get_rate_usd():
    q = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if q.status_code != 200:
        raise HTTPException
    
    for item in xmltodict.parse(q.text)['ValCurs']['Valute']:
        if item['NumCode']=='840':
            return float(item['Value'].replace(',', '.'))
    
    raise HTTPException