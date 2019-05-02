from yapsy.IPlugin import IPlugin
import requests

class RestPlugin(IPlugin):
    def print_name(self):
        print("REST Plugin")
    
    def retry(self, **kwargs):
        dictget = lambda d, *k: [d.get(i) for i in k]
        method, url, message, headers = dictget(kwargs, 'method', 'url', 'message', 'headers')
        r = getattr(requests, method)(url, data=message, headers=headers)
        print(r.text)