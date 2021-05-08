import requests
from bs4 import BeautifulSoup
url = "https://id.wikipedia.org/wiki/Daftar_buah"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
source = requests.get(url, headers=headers)
soup = BeautifulSoup(source.text,"html.parser")
tex = soup.find_all("li")

lis = """
RAINUD
MLUAI
TAAGSNL
LKATEOC
TAEELK
KGENJLO
LPAE
HALBWE
MLDIAE
GBCNAA
CIAEPK
GGAAMN
KAALS
GRTNOE
KRIYAAS
GNNAAK
TMOAA
GGARNU
DIGNAAAR
SSIIMK
PRRJUUUKTE
TIPAE
MUNDAG
BAUMJ
TAAKPO
YEAAPP
BAANRUMT
GKAAMESN
MRKAU
GGASINM
MMNNIUET
TRRBSIOE
GAAAAKHNNTC
MKSRAAI
MLGBBNIIE
GGJNUA
DEEAKMCP
DDGNNOOEK
GGNNAUEKB
DKWAAATHMOE
ANGGAM
"""
lsx = lis.split("\n")
# print(lsx)
for y in lsx:
	for x in tex:
		if len(y)==len(x.text.strip().upper().replace(" ","")):
			# print("ok")
			temp = x.text.strip().upper().replace(" ","")
			asd = 0
			for z in y:
				if z in temp:
					temp = temp.replace(z,"",1)
					asd+=1
			if asd==len(y):
				print(f"{y} : {x.text.strip()}")