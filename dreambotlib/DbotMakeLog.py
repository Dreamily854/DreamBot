import colorlog
import logging


conf_loglevel = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}

conf = {
    "Console_Enable": True,
    "Console_Log_Level": "debug",
    "Color": True,
    "File_Enable": True,
    "logfile": "main.log",
    "File_Log_Level": "debug"
}


def MakeLog(conf=conf):
    colored = conf["Color"]
    file = None
    # LOG_LEVEL = conf_loglevel[conf["log"]["stream"]["level"]]
    # file_LOG_LEVEL = conf_loglevel[conf["log"]["file"]["level"]]
    logging.root.setLevel(conf_loglevel[conf["Console_Log_Level"]])
    if conf["File_Enable"] == True:
        file = logging.FileHandler(filename="log/%s"%(conf["logfile"],),
                                   encoding="utf-8",
                                   mode="a"
                                   )
        file.setFormatter(logging.Formatter(
            fmt="[%(asctime)s] [%(filename)s(line:%(lineno)d)/%(levelname)s]: %(message)s",
            datefmt='%d %b %Y %H:%M:%S',
        ))
        file.setLevel(conf_loglevel[conf["File_Log_Level"]])

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
    stream.setLevel(conf_loglevel[conf["Console_Log_Level"]])
    stream.setFormatter(formatter)

    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(stream)
    if conf["File_Enable"] == True:
        log.addHandler(file)
    
    return log


# log.debug("Debug Log")
# log.info("Info Log")
# log.warning("Warning Log")
# log.error("Error log")
# log.critical("Critical LOG"
