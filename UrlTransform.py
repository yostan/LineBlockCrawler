# coding: utf-8

import codecs
import sys


class FileHandle:
    def __init__(self, f):
        self.file = f

    def extractUrl(self):
        for ids in open(self.file).readlines():
            arr = ids.split(" ")
            phone = arr[0]
            html = arr[1]
            fp = codecs.open('phone\\'+phone, mode = 'ab+', encoding= 'utf-8')
            fp.write(html)



if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    fh = FileHandle('E:\\shmai\\url\\urlextract\\res-01\\part-00000')
    fh.extractUrl()
    print 'done..............'
