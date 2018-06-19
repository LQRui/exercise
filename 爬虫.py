import urllib
import chardet
from urllib import request

if __name__ == '__main__':

    url = "http://jobs.zhaopin.com/CC577092783J00115272807.htm?ssidkey=y&ss=201&ff=03&sg=267e45b707e74cc590998621658c86f6&so=6"

    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))

    html = html.decode()
    print(html)
