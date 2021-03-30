# DreamBot Core
# Event Process Lib
# self.operation = {
#   "Normal_Operation": {
#       "api":"blabla",
#       "Data":{"Parameter":"value" ......}
#   },
#   "Quick_Opeation": {"Parameter":"value" ......}
#   }


class Event:
    def __init__(self, log, rules):
        self.rules = rules
        self.mode = {
            'AddGroupRequestEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'AnonymousGroupMessageEvent': {
                'Plugin_Direct': True,
                'Command': True,
                'Proxy': True
            },
            'FriendAddNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'FriendPrivateMessageEvent': {
                'Plugin_Direct': True,
                'Command': True,
                'Proxy': True
            },
            'FriendRecallNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'FriendRequestEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupAdminNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupBanNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupDecreaseNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupIncreaseNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupPrivateMessageEvent': {
                'Plugin_Direct': True,
                'Command': True,
                'Proxy': True
            },
            'GroupRecallNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'GroupUploadNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'HeartBeatMetaEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'HonorNotifyNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'InviteGroupRequestEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'LifeCycleMetaEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'LuckyKingNotifyNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'NormalGroupMessageEvent': {
                'Plugin_Direct': True,
                'Command': True,
                'Proxy': True
            },
            'NoticeGroupMessageEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'OtherPrivateMessageEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            },
            'PokeNotifyNoticeEvent': {
                'Plugin_Direct': True,
                'Command': False,
                'Proxy': True
            }
        }

    def EventAlloter(self, data):
        Allot = {
            "message": self.MessageEventAlloter,
            "notice": self.NoticeEventAlloter,
            "request": self.RequestEventAlloter,
            "meta_event": self.MetaEventAlloter
        }
        try:
            if data["post_type"] in Allot:
                Event = Allot[data["post_type"]]
                return Event(data)
            else:
                return False
        except:
            return False

    def MessageEventAlloter(self, data):
        MeaasgeAllot = {
            "private": self.PrivateMessageEvent,
            "group": self.GroupMessageEvent
        }
        try:
            if data["message_type"] in MeaasgeAllot:
                MEvent = MeaasgeAllot[data["message_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def NoticeEventAlloter(self, data):
        NoticeAllot = {
            "group_upload": self.GroupUploadNoticeEvent,
            "group_admin": self.GroupAdminNoticeEvent,
            "group_decrease": self.GroupDecreaseNoticeEvent,
            "group_increase": self.GroupIncreaseNoticeEvent,
            "group_ban": self.GroupBanNoticeEvent,
            "friend_add": self.FriendAddNoticeEvent,
            "friend_recall": self.FriendRecallNoticeEvent,
            "group_recall": self.GroupRecallNoticeEvent,
            "notify": self.NoticeEventAlloter

        }
        try:
            if data["notice_type"] in NoticeAllot:
                MEvent = NoticeAllot[data["notice_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def RequestEventAlloter(self, data):
        RequestAllot = {
            "friend": self.FriendRequestEvent,
            "group": self.GroupRequestEventAlloter
        }
        try:
            if data["request_type"] in RequestAllot:
                MEvent = RequestAllot[data["request_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def MetaEventAlloter(self, data):
        MetaAllot = {
            "lifecycle": self.LifeCycleMetaEvent,
            "heartbeat": self.HeartBeatMetaEvent
        }
        try:
            if data["meta_event_type"] in MetaAllot:
                MEvent = MetaAllot[data["meta_event_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def NotifyNoticeEventAlloter(self, data):
        NotifyAllot = {
            "lucky_king": self.LuckyKingNotifyNoticeEvent,
            "honor": self.HonorNotifyNoticeEvent,
            "poke": self.PokeNotifyNoticeEvent
        }
        try:
            if data["sub_type"] in NotifyAllot:
                MEvent = NotifyAllot[data["sub_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def GroupRequestEventAlloter(self, data):
        GroupRequestAllot = {
            "add": self.AddGroupRequestEvent,
            "invite": self.InviteGroupRequestEvent
        }
        try:
            if data["sub_type"] in GroupRequestAllot:
                MEvent = GroupRequestAllot[data["sub_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def PrivateMessageEventAlloter(self, data):
        PrivateMessageAllot = {
            "friend": self.FriendPrivateMessageEvent,
            "group": self.GroupPrivateMessageEvent,
            "other": self.OtherPrivateMessageEvent
        }
        try:
            if data["sub_type"] in PrivateMessageAllot:
                MEvent = PrivateMessageAllot[data["sub_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def GroupMessageEventAlloter(self, data):
        GroupMessageAllot = {
            "normal": self.NormalGroupMessageEvent,
            "anonymous": self.AnonymousGroupMessageEvent,
            "notice": self.NoticeGroupMessageEvent
        }
        try:
            if data["sub_type"] in GroupMessageAllot:
                MEvent = GroupMessageAllot[data["sub_type"]]
                return MEvent(data)
            else:
                return False
        except:
            return False

    def FriendPrivateMessageEvent(self, data):
        # 消息事件 - 私聊消息 (好友)
        # 支持模式 插件直通 转发 命令
        # 字段名        数据类型         可能的值                 说明
        # time	        number (int64)	-                       事件发生的时间戳
        # self_id	    number (int64)	-                       收到事件的机器人 QQ 号
        # post_type	    string	        message	                上报类型
        # message_type	string	        private	                消息类型
        # sub_type	    string	        friend,group,other	    消息子类型，如果是好友则是 friend，如果是群临时会话则是 group
        # message_id	number (int32)	-	                    消息 ID
        # user_id	    number (int64)	-	                    发送者 QQ 号
        # message	    message	        -	                    消息内容
        # raw_message	string	        -	                    原始消息内容
        # font	        number (int32)	-	                    字体
        # sender	    object	        -	                    发送人信息

        # 其中 sender 字段的内容如下：
        # 字段名     数据类型         说明
        # user_id    number (int64)  发送者 QQ 号
        # nickname   string          昵称
        # sex        string          性别，male 或 female 或 unknown
        # age        number (int32)  年龄

        # 快速操作
        # 字段名	        数据类型	说明	                                                                    默认情况
        # reply	        message	    要回复的内容                                                               不回复
        # auto_escape	boolean	    消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效     不转义

        pass

    def GroupPrivateMessageEvent(self, data):
        # 消息事件 - 私聊消息 (群临时会话)
        # 支持模式 插件直通 转发 命令
        # 字段名        数据类型         可能的值                 说明
        # time	        number (int64)	-                       事件发生的时间戳
        # self_id	    number (int64)	-                       收到事件的机器人 QQ 号
        # post_type	    string	        message	                上报类型
        # message_type	string	        private	                消息类型
        # sub_type	    string	        group	                消息子类型
        # message_id	number (int32)	-	                    消息 ID
        # user_id	    number (int64)	-	                    发送者 QQ 号
        # message	    message	        -	                    消息内容
        # raw_message	string	        -	                    原始消息内容
        # font	        number (int32)	-	                    字体
        # sender	    object	        -	                    发送人信息

        # 其中 sender 字段的内容如下：
        # 字段名     数据类型         说明
        # user_id    number (int64)  发送者 QQ 号
        # nickname   string          昵称
        # sex        string          性别，male 或 female 或 unknown
        # age        number (int32)  年龄

        # 快速操作
        # 字段名	        数据类型	说明	                                                                    默认情况
        # reply	        message	    要回复的内容                                                               不回复
        # auto_escape	boolean	    消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效     不转义
        pass

    def OtherPrivateMessageEvent(self, data):
        # 消息事件 - 私聊消息 (其他)
        # 支持模式 插件直通 转发 命令
        # 字段名        数据类型         可能的值                 说明
        # time	        number (int64)	-                       事件发生的时间戳
        # self_id	    number (int64)	-                       收到事件的机器人 QQ 号
        # post_type	    string	        message	                上报类型
        # message_type	string	        private	                消息类型
        # sub_type	    string	        other	                消息子类型
        # message_id	number (int32)	-	                    消息 ID
        # user_id	    number (int64)	-	                    发送者 QQ 号
        # message	    message	        -	                    消息内容
        # raw_message	string	        -	                    原始消息内容
        # font	        number (int32)	-	                    字体
        # sender	    object	        -	                    发送人信息

        # 其中 sender 字段的内容如下：
        # 字段名     数据类型         说明
        # user_id    number (int64)  发送者 QQ 号
        # nickname   string          昵称
        # sex        string          性别，male 或 female 或 unknown
        # age        number (int32)  年龄

        # 快速操作
        # 字段名	        数据类型	说明	                                                                    默认情况
        # reply	        message	    要回复的内容                                                               不回复
        # auto_escape	boolean	    消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效     不转义
        pass

    def NormalGroupMessageEvent(self, data):
        # 消息事件 - 群消息 (正常消息)
        # 支持模式 插件直通 转发 命令
        # 字段名	        数据类型	        可能的值	                说明
        # time	        number (int64)	    -	                        事件发生的时间戳
        # self_id	    number (int64)	    -	                        收到事件的机器人 QQ 号
        # post_type	    string	            message	                    上报类型
        # message_type	string	            group	                    消息类型
        # sub_type	    string	            normal                  	消息子类型
        # message_id	    number (int32)	    -	                    消息 ID
        # group_id	    number (int64)	    -	                        群号
        # user_id	    number (int64)	    -	                        发送者 QQ 号
        # anonymous	    object	            -	                        匿名信息，如果不是匿名消息则为 null
        # message	    message	            -	                        消息内容
        # raw_message	string	            -	                        原始消息内容
        # font	        number (int32)	    -	                        字体
        # sender	        object	            -	                        发送人信息

        # 其中 anonymous 字段的内容如下：
        # 字段名	数据类型	        说明
        # id	    number (int64)	匿名用户 ID
        # name	string	        匿名用户名称
        # flag	string	        匿名用户 flag，在调用禁言 API 时需要传入

        # sender 字段的内容如下：
        # 字段名	    数据类型	        说明
        # user_id	number (int64)	发送者 QQ 号
        # nickname	string	        昵称
        # card	    string	        群名片／备注
        # sex	    string	        性别，male 或 female 或 unknown
        # age	    number (int32)	年龄
        # area	    string	        地区
        # level	    string	        成员等级
        # role	    string	        角色，owner 或 admin 或 member
        # title	    string	        专属头衔

        # 快速操作
        # 字段名	        数据类型	说明	                                                                        默认情况
        # reply	        message	要回复的内容	                                                                    不回复
        # auto_escape	boolean	消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效	             不转义
        # at_sender	    boolean	是否要在回复开头 at 发送者（自动添加），发送者是匿名用户时无效                          at 发送者
        # delete	        boolean	撤回该条消息	                                                                    不撤回
        # kick	        boolean	把发送者踢出群组（需要登录号权限足够），不拒绝此人后续加群请求，发送者是匿名用户时无效     不踢
        # ban	        boolean	把发送者禁言 ban_duration 指定时长，对匿名用户也有效                                   不禁言
        # ban_duration	number	禁言时长	                                                                        30 分钟
        pass

    def AnonymousGroupMessageEvent(self, data):
        # 消息事件 - 群消息 (匿名消息)
        # 支持模式 插件直通 转发 命令
        # 字段名	        数据类型	        可能的值	                说明
        # time	        number (int64)	    -	                        事件发生的时间戳
        # self_id	    number (int64)	    -	                        收到事件的机器人 QQ 号
        # post_type	    string	            message	                    上报类型
        # message_type	string	            group	                    消息类型
        # sub_type	    string	            anonymous	                消息子类型
        # message_id	    number (int32)	    -	                    消息 ID
        # group_id	    number (int64)	    -	                        群号
        # user_id	    number (int64)	    -	                        发送者 QQ 号
        # anonymous	    object	            -	                        匿名信息，如果不是匿名消息则为 null
        # message	    message	            -	                        消息内容
        # raw_message	string	            -	                        原始消息内容
        # font	        number (int32)	    -	                        字体
        # sender	        object	            -	                        发送人信息

        # 其中 anonymous 字段的内容如下：
        # 字段名	数据类型	        说明
        # id	    number (int64)	匿名用户 ID
        # name	string	        匿名用户名称
        # flag	string	        匿名用户 flag，在调用禁言 API 时需要传入

        # sender 字段的内容如下：
        # 字段名	    数据类型	        说明
        # user_id	number (int64)	发送者 QQ 号
        # nickname	string	        昵称
        # card	    string	        群名片／备注
        # sex	    string	        性别，male 或 female 或 unknown
        # age	    number (int32)	年龄
        # area	    string	        地区
        # level	    string	        成员等级
        # role	    string	        角色，owner 或 admin 或 member
        # title	    string	        专属头衔

        # 快速操作
        # 字段名	        数据类型	说明	                                                                        默认情况
        # reply	        message	要回复的内容	                                                                    不回复
        # auto_escape	boolean	消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效	             不转义
        # at_sender	    boolean	是否要在回复开头 at 发送者（自动添加），发送者是匿名用户时无效                          at 发送者
        # delete	        boolean	撤回该条消息	                                                                    不撤回
        # kick	        boolean	把发送者踢出群组（需要登录号权限足够），不拒绝此人后续加群请求，发送者是匿名用户时无效     不踢
        # ban	        boolean	把发送者禁言 ban_duration 指定时长，对匿名用户也有效                                   不禁言
        # ban_duration	number	禁言时长	                                                                        30 分钟
        pass

    def NoticeGroupMessageEvent(self, data):
        # 消息事件 - 群消息(系统提示)
        # 支持模式 插件直通 转发
        # 字段名	        数据类型	        可能的值	                说明
        # time	        number (int64)	    -	                        事件发生的时间戳
        # self_id	    number (int64)	    -	                        收到事件的机器人 QQ 号
        # post_type	    string	            message	                    上报类型
        # message_type	string	            group	                    消息类型
        # sub_type	    string	            notice	                    消息子类型
        # message_id	    number (int32)	    -	                        消息 ID
        # group_id	    number (int64)	    -	                        群号
        # user_id	    number (int64)	    -	                        发送者 QQ 号
        # anonymous	    object	            -	                        匿名信息，如果不是匿名消息则为 null
        # message	    message	            -	                        消息内容
        # raw_message	string	            -	                        原始消息内容
        # font	        number (int32)	    -	                        字体
        # sender	        object	            -	                        发送人信息

        # 其中 anonymous 字段的内容如下：
        # 字段名	数据类型	        说明
        # id	    number (int64)	匿名用户 ID
        # name	string	        匿名用户名称
        # flag	string	        匿名用户 flag，在调用禁言 API 时需要传入

        # sender 字段的内容如下：
        # 字段名	    数据类型	        说明
        # user_id	number (int64)	发送者 QQ 号
        # nickname	string	        昵称
        # card	    string	        群名片／备注
        # sex	    string	        性别，male 或 female 或 unknown
        # age	    number (int32)	年龄
        # area	    string	        地区
        # level	    string	        成员等级
        # role	    string	        角色，owner 或 admin 或 member
        # title	    string	        专属头衔

        # 快速操作
        # 字段名	        数据类型	说明	                                                                        默认情况
        # reply	        message	要回复的内容	                                                                    不回复
        # auto_escape	boolean	消息内容是否作为纯文本发送（即不解析 CQ 码），只在 reply 字段是字符串时有效	             不转义
        # at_sender	    boolean	是否要在回复开头 at 发送者（自动添加），发送者是匿名用户时无效                          at 发送者
        # delete	        boolean	撤回该条消息	                                                                    不撤回
        # kick	        boolean	把发送者踢出群组（需要登录号权限足够），不拒绝此人后续加群请求，发送者是匿名用户时无效     不踢
        # ban	        boolean	把发送者禁言 ban_duration 指定时长，对匿名用户也有效                                   不禁言
        # ban_duration	number	禁言时长	                                                                        30 分钟
        pass

    def GroupUploadNoticeEvent(self, data):
        # 通知事件 - 群文件上传
        #
        # 字段名	        数据类型	        可能的值	          说明
        # time	        number (int64)	    -	                事件发生的时间戳
        # self_id	    number (int64)	    -	                收到事件的机器人 QQ 号
        # post_type	    string	            notice	            上报类型
        # notice_type	string	            group_upload	    通知类型
        # group_id	    number (int64)	    -	                群号
        # user_id	    number (int64)	    -	                发送者 QQ 号
        # file	        object	            -	                文件信息

        # 其中 file 字段的内容如下：
        # 字段名	        数据类型	      说明
        # id	            string	        文件 ID
        # name	        string	        文件名
        # size	        number (int64)	文件大小（字节数）
        # busid	        number (int64)	busid（目前不清楚有什么作用）
        pass

    def GroupAdminNoticeEvent(self, data):
        # 通知事件 - 群管理员变动
        # 字段名	        数据类型	    可能的值	  说明
        # time	        number (int64)	-	        事件发生的时间戳
        # self_id	    number (int64)	-	        收到事件的机器人 QQ 号
        # post_type	    string	        notice	    上报类型
        # notice_type	string	        group_admin	通知类型
        # sub_type	    string	        set、unset	事件子类型，分别表示设置和取消管理员
        # group_id	    number (int64)	-	        群号
        # user_id	    number (int64)	-	        管理员 QQ 号
        pass

    def GroupDecreaseNoticeEvent(self, data):
        # 通知事件 - 群成员减少
        # 字段名         数据类型	    可能的值	                说明
        # time	        number (int64)	-	                    事件发生的时间戳
        # self_id	    number (int64)	-	                    收到事件的机器人 QQ 号
        # post_type	    string	        notice	                上报类型
        # notice_type	string	        group_decrease	        通知类型
        # sub_type	    string	        leave、kick、kick_me	事件子类型，分别表示主动退群、成员被踢、登录号被踢
        # group_id	    number (int64)	-	                    群号
        # operator_id	number (int64)	-	                    操作者 QQ 号（如果是主动退群，则和 user_id 相同）
        # user_id	    number (int64)	-	                    离开者 QQ 号
        pass

    def GroupIncreaseNoticeEvent(self, data):
        # 通知事件 - 群成员增加
        #    字段名         数据类型            可能的值            说明
        #    time           number (int64)    -                 事件发生的时间戳
        #    self_id        number (int64)    -                 收到事件的机器人 QQ 号
        #    post_type      string          notice              上报类型
        #    notice_type    string          group_increase      通知类型
        #    sub_type       string          approve、invite     事件子类型，分别表示管理员已同意入群、管理员邀请入群
        #    group_id       number (int64)    -                 群号
        #    operator_id    number (int64)    -                 操作者 QQ 号
        #    user_id        number (int64)    -                 加入者 QQ 号

        pass

    def GroupBanNoticeEvent(self, data):
        # 通知事件 - 群禁言
        #    字段名         数据类型          可能的值        说明
        #    time           number (int64)    -             事件发生的时间戳
        #    self_id        number (int64)    -             收到事件的机器人 QQ 号
        #    post_type      string          notice          上报类型
        #    notice_type    string          group_ban       通知类型
        #    sub_type       string          ban、lift_ban   事件子类型，分别表示禁言、解除禁言
        #    group_id       number (int64)    -             群号
        #    operator_id    number (int64)    -             操作者 QQ 号
        #    user_id        number (int64)    -             被禁言 QQ 号
        #    duration       number (int64)    -             禁言时长，单位秒

        pass

    def FriendAddNoticeEvent(self, data):
        # 通知事件 - 好友添加

        #    字段名         数据类型          可能的值        说明
        #    time           number (int64)    -             事件发生的时间戳
        #    self_id        number (int64)    -             收到事件的机器人 QQ 号
        #    post_type      string          notice          上报类型
        #    notice_type    string          friend_add      通知类型
        #    user_id        number (int64)    -             新添加好友 QQ 号

        pass

    def FriendRecallNoticeEvent(self, data):
        # 通知事件 - 好友消息撤回
        #    字段名         数据类型           可能的值            说明
        #    time           number (int64)    -                 事件发生的时间戳
        #    self_id        number (int64)    -                 收到事件的机器人 QQ 号
        #    post_type      string          notice              上报类型
        #    notice_type    string          friend_recall       通知类型
        #    user_id        number (int64)                      好友 QQ 号
        #    message_id     number (int64)                      被撤回的消息 ID

        pass

    def GroupRecallNoticeEvent(self, data):
        # 通知事件 - 群消息撤回

        #    字段名         数据类型          可能的值          说明
        #    time           number (int64)    -             事件发生的时间戳
        #    self_id        number (int64)    -             收到事件的机器人 QQ 号
        #    post_type      string          notice          上报类型
        #    notice_type    string          group_recall    通知类型
        #    group_id       number (int64)                  群号
        #    user_id        number (int64)                  消息发送者 QQ 号
        #    operator_id    number (int64)                  操作者 QQ 号
        #    message_id     number (int64)                  被撤回的消息 ID
        pass

    def PokeNotifyNoticeEvent(self, data):
        # 通知事件 - 群内戳一戳
        #    字段           类型       可能的值  说明
        #    post_type      string    notice    上报类型
        #    notice_type    string    notify    消息类型
        #    sub_type       string    poke      提示类型
        #    group_id       int64               群号
        #    user_id        int64               发送者 QQ 号
        #    target_id      int64               被戳者 QQ 号

        pass

    def LuckyKingNotifyNoticeEvent(self, data):
        # 通知事件 - 群红包运气王
        #    字段           类型      可能的值        说明
        #    post_type      string    notice        上报类型
        #    notice_type    string    notify        消息类型
        #    sub_type       string    lucky_king    提示类型
        #    group_id       int64                   群号
        #    user_id        int64                   红包发送者 QQ 号
        #    target_id      int64                   运气王 QQ 号

        pass

    def HonorNotifyNoticeEvent(self, data):
        # 通知事件 - 群成员荣誉变更
        #    字段           类型        可能的值                            说明
        #    post_type      string    notice                            上报类型
        #    notice_type    string    notify                            消息类型
        #    sub_type       string    honor                             提示类型
        #    group_id       int64                                       群号
        #    honor_type     string    talkative、performer、emotion     荣誉类型，分别表示龙王、群聊之火、快乐源泉
        #    user_id        int64                                       成员 QQ 号

        pass

    def FriendRequestEvent(self, data):
        # 请求事件 - 加好友请求
        #    字段名             数据类型            可能的值        说明
        #    time               number (int64)      -           事件发生的时间戳
        #    self_id            number (int64)      -           收到事件的机器人 QQ 号
        #    post_type          string              request     上报类型
        #    request_type       string              friend      请求类型
        #    user_id            number (int64)      -           发送请求的 QQ 号
        #    comment            string              -           验证信息
        #    flag               string              -           请求 flag，在调用处理请求的 API 时需要传入

        #   快速操作
        #    字段名    数据类型    说明    默认情况
        #    approve    boolean    是否同意请求    不处理
        #    remark    string    添加后的好友备注（仅在同意时有效）    无备注

        pass

    def AddGroupRequestEvent(self, data):
        # 请求事件 - 加群请求
        #    字段名             数据类型            可能的值            说明
        #    time               number (int64)      -               事件发生的时间戳
        #    self_id            number (int64)      -               收到事件的机器人 QQ 号
        #    post_type          string              request         上报类型
        #    request_type       string              group           请求类型
        #    sub_type           string              add             请求子类型，分别表示加群请求、邀请登录号入群
        #    group_id           number (int64)      -               群号
        #    user_id            number (int64)      -               发送请求的 QQ 号
        #    comment            string              -               验证信息
        #    flag               string              -               请求 flag，在调用处理请求的 API 时需要传入

        #   快速操作
        #    字段名     数据类型        说明                        默认情况
        #    approve    boolean     是否同意请求／邀请              不处理
        #    reason     string      拒绝理由（仅在拒绝时有效）      无理由

        pass

    def InviteGroupRequestEvent(self, data):
        # 请求事件 - 邀请登录号入群
        #    字段名             数据类型            可能的值            说明
        #    time               number (int64)      -               事件发生的时间戳
        #    self_id            number (int64)      -               收到事件的机器人 QQ 号
        #    post_type          string              request         上报类型
        #    request_type       string              group           请求类型
        #    sub_type           string              invite          请求子类型，分别表示加群请求、邀请登录号入群
        #    group_id           number (int64)      -               群号
        #    user_id            number (int64)      -               发送请求的 QQ 号
        #    comment            string              -               验证信息
        #    flag               string              -               请求 flag，在调用处理请求的 API 时需要传入

        #   快速操作
        #    字段名     数据类型        说明                        默认情况
        #    approve    boolean     是否同意请求／邀请              不处理
        #    reason     string      拒绝理由（仅在拒绝时有效）      无理由
        pass

    def LifeCycleMetaEvent(self, data):
        # 元事件 - 生命周期
        #    字段名             数据类型            可能的值                    说明
        #    time               number (int64)    -                         事件发生的时间戳
        #    self_id            number (int64)    -                         收到事件的机器人 QQ 号
        #    post_type          string          meta_event                  上报类型
        #    meta_event_type    string          lifecycle                   元事件类型
        #    sub_type           string          enable、disable、connect    事件子类型，分别表示 OneBot 启用、停用、WebSocket 连接成功

        pass

    def HeartBeatMetaEvent(self, data):
        # 元事件 - 心跳
        #    字段名             数据类型            可能的值            说明
        #    time               number (int64)      -               事件发生的时间戳
        #    self_id            number (int64)      -               收到事件的机器人 QQ 号
        #    post_type          string              meta_event      上报类型
        #    meta_event_type    string              heartbeat       元事件类型
        #    status             object              -               状态信息
        #    interval           number (int64)      -               到下次心跳的间隔，单位毫秒
        # 其中 status 字段的内容和 get_status 接口的快速操作相同。

        pass


rule = [
    {
        "enable": True,  # True False
        "RuleName": "AEMMM",
        "Terminate_processing":True,
        "Binding_Events": [
            'AddGroupRequestEvent',
            'AnonymousGroupMessageEvent',
            'FriendAddNoticeEvent',
            'FriendPrivateMessageEvent',
            'FriendRecallNoticeEvent',
            'FriendRequestEvent',
            'GroupAdminNoticeEvent',
            'GroupBanNoticeEvent',
            'GroupDecreaseNoticeEvent',
            'GroupIncreaseNoticeEvent',
            'GroupPrivateMessageEvent',
            'GroupRecallNoticeEvent',
            'GroupUploadNoticeEvent',
            'HeartBeatMetaEvent',
            'HonorNotifyNoticeEvent',
            'InviteGroupRequestEvent',
            'LifeCycleMetaEvent',
            'LuckyKingNotifyNoticeEvent',
            'NormalGroupMessageEvent',
            'NoticeGroupMessageEvent',
            'OtherPrivateMessageEvent',
            'PokeNotifyNoticeEvent'
        ],
        "conditions":{
            "mode":""# All Only_Groups Only_Privates,Except_Groups,Except_Privates,Except_GP , Appoint_Groups,Appoint_Privates,Appoint_GP
        },
        "RuleConf":{
            "Mode": "direct",  # command direct proxy
            "CommandMode_conf": {
                "match": "prefix",  # postfix
                "matchstr": "./d",
            },
            "DirectMode_Conf":
            {
                "plugin": "com.dreambot.record"
            },
            "ProxyMode_Conf": {
                "server": "server.dreambot.t"
            }
        }
    }
]
