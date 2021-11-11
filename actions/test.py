"""
Copyright (c) 2021 Philipp Scheer
"""


from jarvis_sdk import Router


@Router.on("status")
def status():
    return "up"
