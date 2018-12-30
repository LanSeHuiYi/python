#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@Author  :   Liuyk
@Software:   sap hr
@File    :   URLUtil.py
@Time    :   2018/10/26 13:54
@Desc    :
"""

from urllib.request import urlopen
from urllib.request import Request
from urllib import parse
...

class URLUtil:

    def getContent(url):
        request = Request(url)

        #request.add_header('Authorization', 'Basic dGVzdDAxQGhhbmd6aG91bGlEOmxoODg4ODg4')
        request.add_header('Authorization', 'Basic em1AaGFuZ3pob3VsaVQxOmNkY3NAcA==')
        request.add_header('Content-Type', 'application/json')

        response = urlopen(request)

        return response.read()

    def getContent01(url):
        request = Request(url)
        response = urlopen(request)
        return response.read()

    def getContentXml(url):
        request = Request(url)

        response = urlopen(request)
        return response.read()

    #提取URL中的参数
    def geturlparam(path):
        query = parse.urlparse(path).query
        item = parse.parse_qs(query).items()
        return dict([(k, v[0]) for k, v in item])

