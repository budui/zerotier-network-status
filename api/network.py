from http.server import BaseHTTPRequestHandler
from http.server import socketserver
import urllib3
import os
import json

def access_token():
    try:
        token = os.environ["TOKEN"]
        data = {}
        for name, zt, network in map(lambda x: x.split("@"), token.split(";")):
            data[name] = dict(id=network, token=zt)
        return data
    except KeyError:
        raise ValueError("can not read the token:[TOKEN] for api proxy")


def list_members(newtork_id, token) -> urllib3.response.HTTPResponse:
    http = urllib3.PoolManager()
    r = http.request(
        "GET",
        f"https://my.zerotier.com/api/v1/network/{newtork_id}/member",
        headers={"Authorization": f"bearer {token}"},
    )
    return r


class handler(BaseHTTPRequestHandler):
    def _set_json(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        zt_data = access_token()
        network_name = self.path.split("/")[-1]
        if network_name not in zt_data:
            self._set_json(404)
            self.wfile.write(json.dumps({"error": "NOT FOUND"}))
            return

        r = list_members(zt_data[network_name]["id"], zt_data[network_name]["token"])
        self._set_json(r.status)
        self.wfile.write(r.data)
        return
