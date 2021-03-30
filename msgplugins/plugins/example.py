# DreamBot Plugins Example

# import blablabla 
# 这里可按需引用模块


class plugin:
    def __init__(self,send,args,send_type,sender):
        self.args = args
        self.send_type = send_type
        self.sender = sender
        self.send = send

    def do(self):

        # 这里是处理逻辑 #
        # Code ....
        # 
        
        # 发送部分 ...
        if self.send_type == "group":
            self.send.send_group_msg(group_id = self.sender["gid"],msg = "BlaBla")
        elif self.send_type == "private":
            self.send.send_private_msg(user_id = self.sender["uid"],msg ="BlaBla")



