#!/usr/bin/env python3

###########################################################################
#                                                                         #
# vilhelmprytz/minecraftserverstatus-api                                  #
# Copyright (C) 2019 - 2020, Vilhelm Prytz, <vilhelm@prytznet.se>, et al. #
#                                                                         #
# Licensed under the terms of the MIT license, see LICENSE.               #
# https://github.com/vilhelmprytz/minecraftserverstatus-api               #
#                                                                         #
###########################################################################

from flask import Flask, jsonify, abort, make_response, send_file
from werkzeug.exceptions import HTTPException
from mcstatus import MinecraftServer
from json import dumps
from base64 import decodebytes
from io import BytesIO

app = Flask(__name__)

# error handlers
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )

    response.content_type = "application/json"
    return response, e.code


# main routes
@app.route("/server/<address>")
def server_info(address):
    BASE = {"code": 200, "name": "OK", "description": "success"}

    server = MinecraftServer.lookup(address)

    try:
        status = server.status()
    except Exception:
        data = {"address": address, "online": False}

        return jsonify({**BASE, **{"response": data}})

    online_players = []
    if status.players.sample != None:
        for player in status.players.sample:
            online_players.append({"name": player.name, "uuid": player.id})

    data = {
        "address": address,
        "online": True,
        "description": status.description,
        "version": {"name": status.version.name, "protocol": status.version.protocol},
        "players": {
            "online": status.players.online,
            "max": status.players.max,
            "sample": online_players,
        },
        "favicon": status.favicon,
    }

    return jsonify({**BASE, **{"response": data}})


@app.route("/favicon/<address>")
def server_icon(address):
    server = MinecraftServer.lookup(address)

    try:
        status = server.status()
    except Exception:
        abort(400, "Server not running")

    image_bytes = status.favicon.split(",")[1]
    img_io = BytesIO(decodebytes(image_bytes.encode()))

    return send_file(img_io, mimetype="image/png")


# debug run
if __name__ == "__main__":
    app.run(host="0.0.0.0")
