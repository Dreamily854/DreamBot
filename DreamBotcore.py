# DreamBot Core
import messagelib.send
import requests
import json


class DreamBot:
    def __init__(self, send, command):
        self.send = messagelib.send.send(send)
        self.command = command

    def core(self, message):
        if message["message_type"] == "private":
            for command in self.command:
                if message["raw_message"][0:len(command["prefix"])] == command["prefix"]:
                    if command["mode"] == "handle":
                        message_command = message["raw_message"][len(command["prefix"]):].split()[
                            0]
                        plugin_args = message["raw_message"][len(
                            command["prefix"]):].split()[1:]
                        try:
                            sender = {
                                "uid": message["sender"]["user_id"],
                                "nickname": message["sender"]["nickname"]
                            }
                            plugin = __import__("plugins.%s" %
                                                (message_command,))
                            mainclass = getattr(plugin, message_command)
                            pluginclass = mainclass.plugin(send = self.send,
                                args=plugin_args, send_type="private", sender=sender)
                            pluginclass.do()
                            return 0
                        except Exception as e:
                            print(e)
                            self.send.send_private_msg(
                                user_id=message["sender"]["user_id"],
                                msg="命令未找到"
                            )
                            return 1
                    elif command["mode"] == "proxy":
                        header = header = {
                            "Content-Type": "application/json",
                        }
                        data = json.dumps(message)
                        try:
                            requests.post(url="http://%s:%d" % (command["csend"]["server"], command["csend"]["port"]),
                                      headers=header,
                                      data=data
                                      )
                            return 0
                        except:
                            return 1
            return 0
        
        
        elif message["message_type"] == "group":
            for command in self.command:
                if message["raw_message"][0:len(command["prefix"])] == command["prefix"]:
                    if command["mode"] == "handle":
                        message_command = message["raw_message"][len(command["prefix"]):].split()[
                            0]
                        plugin_args = message["raw_message"][len(
                            command["prefix"]):].split()[1:]
                        try:
                            sender = {
                                "gid":message["group_id"],
                                "uid": message["sender"]["user_id"],
                                "nickname": message["sender"]["nickname"],
                                "card":message["sender"]["card"],
                                "role":message["sender"]["role"],
                                
                            }
                            plugin = __import__("plugins.%s" %
                                                (message_command,))
                            mainclass = getattr(plugin, message_command)
                            pluginclass = mainclass.plugin(send = self.send,
                                args=plugin_args, send_type="group", sender=sender)
                            pluginclass.do()
                            return 0
                        except:
                            print("command not found")
                            self.send.send_group_msg(
                                group_id=message["group_id"],
                                msg="命令未找到"
                            )
                            return 1
                    elif command["mode"] == "proxy":
                        header = header = {
                            "Content-Type": "application/json",
                        }
                        data = json.dumps(message)
                        try:
                            requests.post(url="http://%s:%d" % (command["csend"]["server"], command["csend"]["port"]),
                                      headers=header,
                                      data=data
                                      )
                            return 0
                        except:
                            return 1
            

            return 0
                    
