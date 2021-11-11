import json
import signal
import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from actions import test

from jarvis_sdk import Router


PORT = 6666

logf = open("./template.log", "a+")
def log(msg):
	logf.write(f"{msg}\n")
	logf.flush()




log("Started test plugin")

running = True

@Router.on("stop")
def stop_program():
	global running
	running = False
	exit(0)

class PluginHandler(SimpleHTTPRequestHandler):
	def log_message(self, format, *args):
		log("%s %s %s" % (datetime.datetime.now(),
							self.client_address[0],
							format%args))

	def do_GET(self):
		self.send_response(405)
		self.send_header("Content-Type", "application/json")
		self.end_headers()
		self.wfile.write(json.dumps({"success": False, "error": "GET parameter not supported. Use POST instead"}).encode("utf-8"))
		self.wfile.flush()

	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-Type", "application/json")
		self.end_headers()

		res = Router.execute(self.path[1:], None)
		rsp = { "success": False }

		if res is None:				rsp = { "success": False }
		elif isinstance(res, bool):	rsp = { "success": res }
		else:						rsp = { "success": True, "result": res }

		self.wfile.write(json.dumps(rsp).encode("utf-8"))
		self.wfile.flush()


httpd = HTTPServer(("localhost", PORT), PluginHandler)
while running:
	httpd.handle_request()
print("Stopping plugin")
