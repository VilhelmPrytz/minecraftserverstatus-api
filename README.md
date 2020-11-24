# minecraftserverstatus-api

Simple web-based API for retrieving server status of any Minecraft Server in JSON format.

Built using Python 3 and Flask.

## How To Use

To get started, make sure you have Python 3 and pip3 installed on your system.

Once you have pip3 and python 3, install required dependencies (packages) using pip3 and the requirements file (preferably in a virtual environment).

```bash
pip3 install -r requirements.txt
```

It is recommended hosting the application using something like [gunicorn](https://gunicorn.org/) and [supervisor](http://supervisord.org/) behind Nginx.

To retrieve the status of a Minecraft Server, send a `GET` request to the URI `/server/<address>`. Replace `<address>` with specified hostname or IP of Minecraft Server (see the example result below). This endpoint will always return a JSON blob.

```json
{
    "code": 200,
    "description": "success",
    "name": "OK",
    "response": {
        "address": "awesomeserver.example.com",
        "online": true,
        "description": {
            "text": "A Minecraft Server"
        },
        "favicon": "data:image/png;base64.... big blob of bytes...",
        "version": {
            "name": "1.14.4",
            "protocol": 498
        },
        "players": {
            "online": 1,
            "max": 20,
            "sample": [
                {"name": "lordprytz", "uuid": "3db416e9-02c0-461b-9bf2-e8d7b64aa1d2"}
            ],
        }
    }
}
```

You can also send a `GET` request to `/favicon/<address>`, which will then return the server icon as PNG for the specified server.

## Contributing

Feel free to send a pull request!

## Author

Copyright (c) 2019-2020 Vilhelm Prytz
