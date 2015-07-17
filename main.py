# -*- coding: utf-8 -*-

from TextCrawler import ContentExtractor
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
ext = ContentExtractor()
# ext.test()
ext.test_file(sys.argv[1])






