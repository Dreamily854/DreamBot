# Onebot
#
#
# #
# import hmac
import requests


class Onebot:
    def __init__(self, server, port, other="",token="", method="POST"):
        #self.key = key
        self.token = None
        self.method = method
        self.server = server
        self.port = port
        self.other = other
        self.token=token
        self.headers = {
            'Content-Type': 'application/json',
        }

    def make_request(self, api, data):
        send_data={'access_token': self.token}
        for i in list(data.keys()):
            send_data[i]=data[i]
        r = requests.request(method=self.method, url="http://%s:%d/%s%s" %
                             (self.server, self.port, self.other, api), params=send_data)
 
        if r.status_code == 200:
            r_json = r.json()
            if not r_json["data"] == None:
                return r_json["data"]
            else:
                return None
        else:
            return None


    def send_private_msg(self, user_id, message, auto_escape=False):
        data = {
            'auto_escape': auto_escape,
            'user_id': user_id,
            'message': message
        }
        return self.make_request(api="send_private_msg", data=data)

    def send_group_msg(self, group_id, message, auto_escape=False):
        data = {
            'auto_escape': auto_escape,
            'group_id': group_id,
            'message': message
        }
        return self.make_request(api="send_group_msg", data=data)

    def send_msg(self, message_type, message, user_id=None, group_id=None,  auto_escape=False):
        data = {
            'auto_escape': auto_escape,
            'message_type':message_type,
            'user_id': user_id,
            'group_id': group_id,
            'message': message
        }
        return self.make_request(api="send_msg", data=data)

    def delete_msg(self, message_id):
        data = {
            "message_id": message_id
        }
        return self.make_request(api="delete_msg", data=data)

    def get_msg(self, message_id):
        data = {
            "message_id": message_id
        }
        return self.make_request(api="get_msg", data=data)

    def get_forward_msg(self, id):
        data = {
            "id": id
        }
        return self.make_request(api="get_forward_msg", data=data)

    def send_like(self, user_id, times=1):
        data = {
            "user_id": user_id,
            "times": times
        }
        return self.make_request(api="send_like", data=data)

    def set_group_kick(self, group_id, user_id, reject_add_request=False):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "reject_add_request": reject_add_request
        }
        return self.make_request(api="set_group_kick", data=data)

    def set_group_ban(self, group_id, user_id, duration=1800):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "duration": duration
        }
        return self.make_request(api="set_group_ban", data=data)
# Example self.set_group_ban(group_id=700080009,user_id = 2725480141,duration = 30*60*60*24)

    def set_group_anonymous_ban(self, group_id, anonymous, anonymous_flag, flag, duration=1800):
        if anonymous_flag == None:
            data = {
                "group_id": group_id,
                "anonymous": anonymous,
                "flag": flag,
                "duration": duration
            }
        else:
            data = {
                "group_id": group_id,
                "anonymous": anonymous,
                "anonymous_flag": anonymous_flag,
                "duration": duration
            }
        return self.make_request(api="set_group_anonymous_ban", data=data)

    def set_group_whole_ban(self, group_id, enable=True):
        data = {
            "group_id": group_id,
            "enable": enable
        }
        return self.make_request(api="set_group_whole_ban", data=data)

    def set_group_admin(self, group_id, user_id, enable=True):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "enable": enable
        }
        return self.make_request(api="set_group_admin", data=data)

    def set_group_anonymous(self, group_id, enable=True):
        data = {
            "group_id": group_id,
            "enable": enable
        }
        return self.make_request(api="set_group_anonymous", data=data)

    def set_group_card(self, group_id, user_id, card=None):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "card": card
        }
        return self.make_request(api="set_group_card", data=data)

    def set_group_leave(self, group_id, is_dismiss=False):
        data = {
            "group_id": group_id,
            "is_dismiss": is_dismiss
        }
        return self.make_request(api="set_group_leave", data=data)

    def set_group_special_title(self, group_id, user_id, duration=-1, special_title=None):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "special_title": special_title,
            "duration": duration
        }
        return self.make_request(api="set_group_special_title", data=data)

    def set_group_add_request(self, flag, remark, approve=True):
        data = {
            "flag": flag,
            "remark": remark,
            "approve": approve
        }
        return self.make_request(api="set_group_add_request", data=data)

    def get_login_info(self):
        data = {}
        return self.make_request(api="get_login_info", data=data)

    def get_stranger_info(self, user_id, no_cache=False):
        data = {
            "user_id": user_id,
            "no_cache": no_cache
        }
        return self.make_request(api="get_stranger_info", data=data)

    def get_friend_list(self):
        data = {}
        return self.make_request(api="get_friend_list", data=data)

    def get_group_info(self, group_id, no_cache=False):
        data = {
            "group_id": group_id,
            "no_cache": no_cache
        }
        return self.make_request(api="get_group_info", data=data)

    def get_group_list(self):
        data = {}
        return self.make_request(api="get_group_list", data=data)

    def get_group_member_info(self, group_id, user_id, no_cache=False):
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "no_cache": no_cache
        }
        return self.make_request(api="get_group_member_info", data=data)

    def get_group_member_list(self, group_id):
        data = {
            "group_id": group_id
        }
        return self.make_request(api="get_group_member_list", data=data)

    def get_group_honor_info(self, group_id, type):
        data = {
            "group_id": group_id,
            "type": type
        }
        return self.make_request(api="get_group_honor_info", data=data)

    def get_cookies(self, domain):
        data = {
            "domain": domain
        }
        return self.make_request(api="get_cookies", data=data)

    def get_csrf_token(self):
        data = {}
        return self.make_request(api="get_csrf_token", data=data)

    def get_credentials(self, domain):
        data = {
            "domain": domain
        }
        return self.make_request(api="get_cookies", data=data)

    def get_record(self, file, out_format):
        data = {
            "file": file,
            "out_format": out_format
        }
        return self.make_request(api="get_record", data=data)

    def get_image(self, file):
        data = {
            "file": file
        }
        return self.make_request(api="get_image", data=data)

    def can_send_image(self):
        data = {}
        return self.make_request(api="can_send_image", data=data)

    def can_send_record(self):
        data = {}
        return self.make_request(api="can_send_record", data=data)

    def get_status(self):
        data = {}
        return self.make_request(api="get_status", data=data)

    def get_version_info(self):
        data = {}
        return self.make_request(api="get_version_info", data=data)

    def set_restart(self, delay):
        data = {"delay": delay}
        return self.make_request(api="set_restart", data=data)

    def clean_cache(self):
        data = {}
        return self.make_request(api="clean_cache", data=data)


