import requests

try:
    requests.request('get', 'https://www.cursoemvideo.com/')
except:
    print('\033[31mO site cursoemvideo.com não está acessivel\033[m')
else:
    print('\033[32mO site cursoemvideo.com está acessivel\033[m')
