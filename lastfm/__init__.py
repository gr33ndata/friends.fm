import sys
import json
import urllib

class LastFMParams(dict):
    
    def __init__(self, user, key):
        self['user'] = user
        self['api_key'] = key
        self['format'] = 'json'
        
        
class LastFM:

    def __init__(self, user, key):
        self.user = user
        self.key = key
    
    def pprint(self, data):
        json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))  
          
    def request(self, **kwargs):
        lfmparams = LastFMParams(self.user, self.key)
        for param in kwargs:
            lfmparams[param] = kwargs[param]
        params = urllib.urlencode(lfmparams)
        print "http://ws.audioscrobbler.com/2.0/?%s" % params
        f = urllib.urlopen("http://ws.audioscrobbler.com/2.0/?%s" % params)
        json_data = f.read()
        print json_data
        data = json.loads(json_data)
        return data
        
    def userTopArtists(self, user='', period='overall'):
        if not user:
            user = self.user
        return self.request(method='user.gettopartists', period=period)
        
