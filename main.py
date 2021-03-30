#
# DreamBot
# #
import flask
import dreambotlib
import json
import yaml
import psutil
import time
import hmac
import uuid


print(" Loading Module.... \n DreamBot Project By Dreamily854")

ConfFile = open("config/conf.yml", "r", encoding="UTF-8")
MAIN_CONF = yaml.load(ConfFile.read(), Loader=yaml.FullLoader)
ConfFile.close()

log = dreambotlib.DbotMakeLog.MakeLog(MAIN_CONF["log"])

#log.debug("Debug Log")
#log.info("Info Log")
#log.warning("Warning Log")
#log.error("Error log")
#log.critical("Critical LOG")

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False


#@app.route('/', methods=['POST'])
#def receive():
#    sig = hmac.new(b'<your-key>', flask.request.get_data(), 'sha1').hexdigest()
#    received_sig = flask.request.headers['X-Signature'][len('sha1='):]
#    if sig == received_sig:
        # 请求确实来自于 OneBot
#        pass
#    else:
#        # 假的上报
#        pass



#Bot = DreamBotcore.DreamBot(
#    log=log,
#    send=conf["send"],
#    prefixs=conf["prefixs"],
#    plugins_permission=conf["plugins_permission"]
#)
#app = flask.Flask(__name__)
#app = flask.Flask(__name__)
#app.config['JSON_AS_ASCII'] = False

#@app.route('/', methods=['POST'])
#def serv():
#    print(flask.request.get_json())
#    Bot.core(flask.request.get_json())
#    return ""


if __name__ == "__main__":
    log.info("Start Http Server")
    app.run(host=MAIN_CONF["http"]["server"],
            port=MAIN_CONF["http"]["port"],
            debug=True)
