import requests
# an example layout of a module 
def x_frame_scan(domain):
    url = domain
    r = requests.get(url).headers
    print(r)
    if 'X-Frame-Options' in r :
        pass
    else:
        print('Clickjacking vulnerable')

x_frame_scan("https://dev.to.com")