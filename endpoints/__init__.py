"""
Copyright (c) 2021 Philipp Scheer
"""


import time

from jarvis_sdk import Router


# The Router decorator is used to define API endpoints
# You can either return None, a boolean or a dict
# The endpoint "logs" and "stop" are already defined

@Router.on("status")
def status():
    return { "status": "up", "timestamp": time.time() }

