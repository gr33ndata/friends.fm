import sys
import json
import urllib

class LastFMParams(dict):
    
    def __init__(self, user, key):
        self['user'] = user
        self['api_key'] = key
        self['format'] = 'json'
        self['limit'] = '20'
        
        
class LastFM:

    def __init__(self, user, key):
        self.user = user
        self.key = key
    
    def pprint(self, data):
        json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))  
          
    def request(self, user='', **kwargs):
        if not user:
            user = self.user
        lfmparams = LastFMParams(user, self.key)
        for param in kwargs:
            lfmparams[param] = kwargs[param]
        params = urllib.urlencode(lfmparams)
        f = urllib.urlopen("http://ws.audioscrobbler.com/2.0/?%s" % params)
        json_data = f.read()
        data = json.loads(json_data)
        if 'error' in data:
            raise Exception
        return data
        
    def userTopArtists(self, user='', period='overall', limit='20'):
        return self.request(method='user.gettopartists', user=user, period=period, limit=limit)
        
    def userFriends(self, user='', limit='100'):
        return self.request(method='user.getfriends', user=user, limit=limit)