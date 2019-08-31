# minecraftserverstatus-api

Simple web-based API for retrieving server status of any Minecraft Server in JSON format.

Built using Python 3 and Flask.

# How To Use

To get started, make sure you have Python 3 and pip3 installed on your system.

Once you have pip3 and python 3, install required dependencies (packages) using pip3 and the requirements file (preferably in a virtual environment).

```bash
pip3 install -r requirements.txt
```

We recommend to host the application using something like `gunicorn` and `supvervisor` behind a `nginx` installation (proxy).

To retrieve the status of a Minecraft Server, send a `GET` request to the URI `/server/<address>`. Replace `<address>` with specified hostname or IP of Minecraft Server (see example result).

```json
{
    "address": "awesomeserver.example.com",
    "online": true,
    "description": {
        "text": "A Minecraft Server"
    },
    "version": {
        "name": "1.14.4",
        "protocol": 498
    },
    "players": {
        "online": 1,
        "max": 20,
        "sample": [
            {"name": "MrKaKisen", "uuid": "3db416e9-02c0-461b-9bf2-e8d7b64aa1d2"}
        ],
    }
}
```

# Contributing

Feel free to send a pull request!

# Author

Written by Vilhelm Prytz 2019.