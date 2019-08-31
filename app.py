#!/usr/bin/env python3
# minecraftserverstatus-api
# https://github.com/VilhelmPrytz/minecraftserverstatus-api
# (c) Vilhelm Prytz 2019

from flask import Flask, jsonify
from mcstatus import MinecraftServer

app = Flask(__name__)

# error handlers
@app.errorhandler(400)
def error_400(e):
    return jsonify({"code": 400, "message": "bad request"})

@app.errorhandler(404)
def error_404(e):
    return jsonify({"code": 404, "message": "page not found"})

@app.errorhandler(500)
def error_500(e):
    return jsonify({"code": 500, "message": "an internal server error occurred"})

# main routes
@app.route("/server/<address>")
def server_info(address):
    server = MinecraftServer.lookup(address)

    try:
        status = server.status()
    except Exception:
        data = {"address": address, "online": False}

        return jsonify(data)

    online_players = []
    if status.players.sample != None:
        for player in status.players.sample:
            online_players.append({"name": player.name, "uuid": player.id})

    data = {
        "address": address,
        "online": True,
        "description": status.description,
        "version": {
            "name": status.version.name,
            "protocol": status.version.protocol
        },
        "players": {
            "online": status.players.online,
            "max": status.players.max,
            "sample": online_players
        }
    }

    return jsonify(data)

# debug run
if __name__ == "__main__":
    app.run(host="0.0.0.0")