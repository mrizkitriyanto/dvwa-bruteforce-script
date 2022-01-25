# Intro
I use this script to complete the DVWA brute force high level challenge.

# Installation
```
git clone https://github.com/mrizkitriyanto/dvwa-bruteforce-script.git
```

Change directory to dvwa-bruteforce-script
```
cd dvwa-bruteforce-script
```

Install the python required dependencies for this tool using pip3

```
pip install -r requirements.txt
```

# Usage

Change the url and PHPSESSID, match your url and PHPSESSID
```
url = 'url to target login page'
cookie = {'security': 'high', 'PHPSESSID': 'your PHPSESSID'}
```


using python3
```
python ./path/to/wordlist.txt "success message on page"
```

example
```
python bruteforce.py ~/Desktop/wordlist.txt "Welcome to the password protected area admin"
```

For the explanatio tou can visit my blog on [My Blog](https://mastoto.my.id/blog/dvwa-series-brute-force/)