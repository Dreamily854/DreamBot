# DreamBot Core
import messagelib.send
import requests
import json
import importlib
import inspect
import pkgutil


class Plugin:
    # 该基类每个插件都需要继承，插件需要实现基类定义的方法
    def __init__(self):
        self.description = None
        self.command_name = None

    def perform_operation(self):
        # 实际执行插件所执行的方法，该方法所有插件类都需要实现
        raise NotImplementedError


class DreamBot:
    def __init__(self, log, send, prefixs, plugins_permission):
        log.info("[core] Initializing the core ....")
        self.send = messagelib.send.send(send)
        self.prefixs = prefixs
        self.plugins_permission = plugins_permission
        self.log = log
        self.plugins = {}
        #self.seen_paths = []

    def loadall_plugins(self):
        # code
        for LAP_prefix in self.prefixs:
            if LAP_prefix["module"] == "handle":
                if LAP_prefix["handlemode"] == "command":
                    if not str(LAP_prefix["plugins_folder"]) == "":
                        lap_prefix_plugin_folder = LAP_prefix["plugins_folder"]
                        self.log.info(
                            "[core] Try Load Plugin with {lap_prefix_plugin_folder}")
                        self.load_package(LAP_prefix["plugins_folder"])
                    else:
                        LAP_prefix_prefixname = LAP_prefix["pr"]
                        self.log.warn(
                            "[core] Prefix: {LAP_prefix_prefixname} 'plugins_folder' IS EMPTY s!!")

        self.log.info("[core] Load Plugins")

    def reload_plugin(self, pluginname):
        self.log.info("[core] Try Reload plugin {pluginname}")
        # self.plugins = {}
        # self.seen_paths = []
        # print()
        # print(f"在 {self.plugin_package} 包里查找插件")
        # self.walk_package(self.plugin_package)

    def load_package(self, pluginpath):
        imported_package = importlib.import_module("msgplugins.{pluginpath}")
        for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                plugin_module = importlib.import_module(pluginname)
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # 仅加入Plugin类的子类，忽略掉Plugin本身
                    if issubclass(c, Plugin) and (c is not Plugin):
                        #print(f'    找到插件类: {c.__module__}.{c.__name__}')
                        loadplug = c()
                        if not loadplug.command_name == None:
                            self.log.info(
                                "[core] Load Plugin: {loadplug.command_name} -> {c.__module__}.{c.__name__}")
                            # self.plugins.append(c())
                            self.plugins[pluginpath] = {
                                "command_name": loadplug.command_name,
                                "module_name": c.__module__,
                                "plugin": c
                            }

                        else:
                            self.log.warn(
                                "[core] Load Plugin: Unknown -> {c.__module__}.{c.__name__}  FAILED! SKIP")
                            return None

        # self.log.info("[core] msgplugins.{pluginpath} Loaded")

    def Message_Permission_check(self, command, message):
        self.log.debug("[core] check Permission ")
        permission = command["permission"]
        if permission["enable"] == True:# 判断是否启用权限认证
            self.log.debug("[core] Permission check is enable. CHECKING! ")
            # 1 .检查是否来自不允许的消息类型
            message_type = message['message_type']
            if not permission["allow_%s"%(message_type,)] == True:
                # 检查不通过
                return False
            if message_type == "private":# 2.判断消息来源是否是允许的来源
                if not message["user_id"] in permission["allow_privates"]:
                    # 用户qq号未在列表
                    return False
            elif message_type == "group":
                if not message["group_id"] in permission["allow_groups"]:
                    # QQ群号未在列表
                    return False
        else:
            self.log.debug("[core] Permission check is not enable. SKIP! ")
            #默认通过
            return True

    # -------------------------------------------------------------------------------------
    # - 消息处理 --------------------------------
    # Handle Command
    # 命令处理部分

    def handle_command(self, message, command, send):
        message_l = message["raw_message"][len(command["prefix"]):].split()
        message_command = message_l[0]
        plugin_args = message_l[1:]
        try:
            if message["message_type"] == "private":
                sender = {
                    "uid": message["sender"]["user_id"],
                    "nickname": message["sender"]["nickname"]
                }
            elif message["message_type"] == "group":
                sender = {
                    "gid": message["group_id"],
                    "uid": message["sender"]["user_id"],
                    "nickname": message["sender"]["nickname"],
                    "card": message["sender"]["card"],
                    "role": message["sender"]["role"],
                }

            plugin = __import__("plugins.%s" % (message_command,))
            mainclass = getattr(plugin, message_command)
            pluginclass = mainclass.plugin(send=send,
                                           args=plugin_args,
                                           send_type=message["message_type"],
                                           sender=sender)
            pluginclass.do()
            return 0
        except Exception as e:
            print(e)
            send.send_private_msg(
                user_id=message["sender"]["user_id"],
                msg="命令未找到"
            )
            return 1

    # 直接处理消息
    def handle_direct(self):
        print("handle Direct")

    # 转发消息
    def proxy_msg(self, command, message):
        print("Proxy")
        header = header = {
            "Content-Type": "application/json",
        }
        data = json.dumps(message)
        try:
            requests.post(url="http://%s:%d" % (command["report"]["server"], command["report"]["port"]),
                          headers=header,
                          params=data
                          )
            return 0
        except:
            return 1

    def core(self, message):
        try:
            for command in self.commands:
                prefix_length = len(command["prefix"])
                message_prefix = message["raw_message"][0:prefix_length]
                if message_prefix == command["prefix"]:
                    # Check Permission
                    if command["mode"] == "handle":
                        if command["handlemode"] == "command":
                            # 使用自带命令处理器处理消息
                            print("handle Command")
                        elif command["handlemode"] == "direct":
                            # 使用自带消息处理器 处理消息
                            print("handle direct")
                    elif command["mode"] == "proxy":
                        # 转发消息
                        proxy_msg()
            return 0
        except:
            print("Core Error")
