#
# DreamBot
# #
import colorlog
import logging
import flask
import DreamBotcore
import json
print("Loading .... \n DreamBot Project By Dreamily854")

conffile = open("conf/config.json")
conf = json.loads(conffile.read())
conffile.close()
conf_loglevel = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}
colored = conf["log"]["colorful"]
# LOG_LEVEL = conf_loglevel[conf["log"]["stream"]["level"]]
# file_LOG_LEVEL = conf_loglevel[conf["log"]["file"]["level"]]
logging.root.setLevel(conf_loglevel[conf["log"]["stream"]["level"]])
if conf["log"]["logfile"]["enable"] == True:
    file = logging.FileHandler(filename="log/main.log",
                               encoding="utf-8",
                               mode="a"
                               )
    file.setFormatter(logging.Formatter(
        fmt="[%(asctime)s] [%(filename)s(line:%(lineno)d)/%(levelname)s]: %(message)s",
        datefmt='%d %b %Y %H:%M:%S',
    ))
    file.setLevel(conf_loglevel[conf["log"]["file"]["level"]])


if colored == True:
    formatter = colorlog.ColoredFormatter("[%(time_log_color)s%(asctime)s%(reset)s] [%(filename_log_color)s%(filename)s%(reset)s/%(log_color)s%(levelname)s%(reset)s]: %(message_log_color)s%(message)s%(reset)s",
                                          datefmt='%d %b %Y %H:%M:%S',
                                          reset=True,
                                          log_colors={
                                              'DEBUG':    'cyan',
                                              'INFO':     'green',
                                              'WARNING':  'yellow',
                                              'ERROR':    'red',
                                              'CRITICAL': 'red,bg_white',
                                          },
                                          secondary_log_colors={
                                              'message': {
                                                  'ERROR':    'red',
                                                  'CRITICAL': 'red'
                                              },
                                              'time': {
                                                  'DEBUG':    'cyan',
                                                  'INFO':     'cyan',
                                                  'WARNING':  'cyan',
                                                  'ERROR':    'yellow',
                                                  'CRITICAL': 'yellow'
                                              },
                                              'filename': {
                                                  'DEBUG':    'cyan',
                                                  'INFO':     'cyan',
                                                  'WARNING':  'yellow',
                                                  'ERROR':    'yellow',
                                                  'CRITICAL': 'red,bg_white'
                                              }
                                          },
                                          style='%'
                                          )
else:
    formatter = logging.Formatter("[%(asctime)s] [%(filename)s/%(levelname)s]: %(message)s",
                                  datefmt='%d %b %Y %H:%M:%S')
stream = logging.StreamHandler()
stream.setLevel(conf_loglevel[conf["log"]["stream"]["level"]])
stream.setFormatter(formatter)

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(stream)
if conf["log"]["logfile"]["enable"] == True:
    log.addHandler(file)


# log.debug("Debug Log")
# log.info("Info Log")
# log.warning("Warning Log")
# log.error("Error log")
# log.critical("Critical LOG")


Bot = DreamBotcore.DreamBot(
    log=log,
    send=conf["send"],
    prefixs=conf["prefixs"],
    plugins_permission=conf["plugins_permission"]
)
app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def serv():
    print(flask.request.get_json())
    Bot.core(flask.request.get_json())
    return ""


if __name__ == "__main__":
    log.info("Start Http Server")
    app.run(host=conf["http"]["server"],
            port=conf["http"]["port"],
            debug=True)
