#! /usr/bin/env python
# -*- coding = utf-8 -*-

import urllib, urllib2
from weibo import APIClient

class Client:
    '''
        spider client
    '''
    APP_KEY      = '2661800363'
    APP_SECRET   = '49adf38e2a20d033ee2ddfc9397b7502' 
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
    AUTH_URL     = 'https://api.weibo.com/oauth2/authorize'
    USEID        = 'testweiboapp1@sina.cn'
    PASSWD       = '8306656'

    def __init__(self):

        self.client = APIClient(app_key=self.APP_KEY, 
                                app_secret=self.APP_SECRET, 
                                redirect_uri=self.CALLBACK_URL)

    def set_client(self):
        ref_url = self.client.get_authorize_url()

        cookies = urllib2.HTTPCookieProcessor()
        opener = urllib2.build_opener(cookies)
        urllib2.install_opener(opener)

        post_data = {
            "client_id": self.APP_KEY,
            "redirect_uri": self.CALLBACK_URL,
            "userId": self.USEID,
            "passwd": self.PASSWD,
            "isLogSina": "0",
            "action": "submit",
            "response_type": "code"
                    }

        headers = {
            "User-Agent": "Mozilla/17.0",
            "Host": "api.weibo.com",
            "Referer": ref_url
                  }

        request = urllib2.Request(url = self.AUTH_URL,
                                  data = urllib.urlencode(post_data),
                                  headers = headers)

        try:
            response = urllib2.urlopen(request)
            code = response.geturl()[-32:]

        except:
            raise Exception("error")

        r = self.client.request_access_token(code)
        access_token = r.access_token
        expires_in = r.expires_in 
 
        self.client.set_access_token(access_token, expires_in)

        return self.client
