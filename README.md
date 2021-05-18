# flaskmarket

## Installation

Tested with Python 3.9.5 in Ubuntu 20.04

`sudo apt update`
`sudo apt install software-properties-common`
`sudo add-apt-repository ppa:deadsnakes/ppa`
`sudo apt install python3.9 python3.9-venv`

`python3.9 -m venv myenv`
`source myenv/bin/activate`
`pip install -r requirements.txt`


## Testing Flask

`export FLASK_APP = market`
`export FLASK_ENV = development`
`flask run --host <hostname or ip> --port <port, default 5000>`
