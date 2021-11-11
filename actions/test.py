"""
Copyright (c) 2021 Philipp Scheer
"""


import time
from jarvis_sdk import Router


@Router.on("status")
def status():
    return { "status": "up", "timestamp": time.time() }

