import requests
class send:
    def __init__(self,send):
        self.server = send['server']
        self.port = send['port']
        self.token = send['token']

    def send_group_msg(self,group_id,msg):
        data = {
            'access_token' : self.token,
            'message_type' : 'group',
            'group_id' : group_id,
            'message': msg
            }
        return requests.post(url = "http://%s:%d/send_msg"%(self.server,self.port),params=data)
    def send_private_msg(self,user_id,msg):
        data = {
            'access_token' : self.token,
            'message_type' : 'private',
            'user_id' : user_id,
            'message': msg
            }
        return requests.post(url = "http://%s:%d/send_msg"%(self.server,self.port),params=data)