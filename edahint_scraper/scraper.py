import gzip
import urllib.request


def get_page(url):
    # TODO переделать
    request = urllib.request.Request(url, headers={
            "Accept-Encoding": "gzip",
            "User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11",
        })
    response = urllib.request.urlopen(request)
    gzipFile = gzip.GzipFile(fileobj=response)
    data = gzipFile.read()
    str_data = str(data, encoding='unicode')
    with open('test2.http', 'w') as file:
        file.write(str_data)
    return str_data


def get_local_page(path):
    f = open(path, 'r')
    strw = ''.join(f.read())
    return strw

