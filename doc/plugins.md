### DreamBot 插件开发指南

---

让我们来看一个例子: `example.py`

``` python
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

```

---
接下来, 只需要再聊天中输入: `前缀` + `example` 机器人就会发送 `BlaBla`
`self.send_type` 是消息类型: 当 `self.send_type = group` 时, 代表处理的是群消息. 反之, `self.send_type = private` 即为私聊消息.

`self.args` 为传入的参数 类型为`列表`
为了方便说明，这里我假定`前缀`是 `/` 程序是 `example` 那么我发送 `/example main 123`
此时

``` python
self.args = ['main','123']
```

`self.sender` 是发送人信息 类型为`字典`
以下是它的定义
``` python
#
# 私聊消息  sender共有两个参数  
# uid为发送人QQ号
# nickname为发送人昵称
#
self.sender = {
"uid"       : message["sender"]["user_id"],
"nickname"  : message["sender"]["nickname"]
}

#
#群组消息 sender共有五个参数
# uid和nickname和私聊消息定义相同
# card为群名片 
# role为群成员身份 (它可以是  群成员 管理员 群主 )#
#
self.sender = {
"gid"       : message["group_id"],
"uid"       : message["sender"]["user_id"],
"nickname"  : message["sender"]["nickname"],
"card"      : message["sender"]["card"],
"role"      : message["sender"]["role"],
}

```
 **此代码来自 DreamCore.py**