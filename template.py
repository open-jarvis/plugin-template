import json

from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing.connection import Listener


PORT = 6666


logf = open("./template.log", "a+")
def log(msg):
	logf.write(f"{msg}\n")
	logf.flush()


log("Started test plugin")


class PluginHandler(SimpleHTTPRequestHandler):
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
		self.wfile.write(json.dumps({"success": True, "hi": "world!"}).encode("utf-8"))

httpd = HTTPServer(("localhost", PORT), PluginHandler)
httpd.serve_forever()
