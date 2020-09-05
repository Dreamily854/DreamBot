import logging
import colorlog
colored = True

LOG_LEVEL = logging.INFO
file_LOG_LEVEL = logging.DEBUG
logging.root.setLevel(LOG_LEVEL)

file = logging.FileHandler(filename="test.log",
                           encoding="utf-8",
                           mode="a"
                           )
file.setFormatter(logging.Formatter(
    fmt="[%(asctime)s] [%(filename)s(line:%(lineno)d)/%(levelname)s]: %(message)s",
    datefmt='%d %b %Y %H:%M:%S',
))
file.setLevel(file_LOG_LEVEL)
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
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(stream)
log.addHandler(file)


log.debug("Debug Log")
log.info("Info Log")
log.warning("Warning Log")
log.error("Error log")
log.critical("Critical LOG")
log.fatal("fatal")
