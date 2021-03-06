import urllib2
from gzip import GzipFile
from StringIO import StringIO
import zlib
 
def loadData(url):
    request = urllib2.Request(url)
    #request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib2.urlopen(request)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    #if encoding == 'gzip':
    #    content = gzipx(content)
    #elif encoding == 'deflate':
    #    content = deflate(content)
    return content
 
def gzipx(data):
    buf = StringIO(data)
    f = GzipFile(fileobj=buf)
    return f.read()
 
def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)
 
def main():
    url = "http://www.post163.com/"
    content = loadData(url)
    print content
 
if __name__ == '__main__':
    main()