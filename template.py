import os

from jarvis_sdk import PluginServer
from jarvis_sdk import Logger

from actions import test


CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
PORT = 6666

logger = Logger(f"{CURRENT_WORKING_DIRECTORY}/template.log")
ps     = PluginServer(PORT, logger.info)

logger.info("Started test plugin")

try:                        ps.handle_requests()
except KeyboardInterrupt:   pass

logger.info("Stopping plugin")
