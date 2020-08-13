# 
# DreamBot 命令处理器 
# # 

import json
import DreamBotcore
import flask

conffile = open("config.json")
conf = json.loads(conffile.read())

Bot = DreamBotcore.DreamBot(send=conf["send"],command=conf["command"])


app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def serv():
    print(flask.request.get_json())
    Bot.core(flask.request.get_json())
    return ""


if __name__ == "__main__":
    app.run(host=conf["http"]["server"],port=conf["http"]["port"],debug = True)