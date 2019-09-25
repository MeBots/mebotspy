# mebots [![PyPI version](https://badge.fury.io/py/mebots.svg)](https://badge.fury.io/py/mebots)

> Python library for interfacing with the MeBots API.

[API documentation](http://mebots.co/documentation)

## Setup
First, install the module:

```sh
pip3 install mebots
```

Then, to use these functions, you must import the module:

```py
import mebots
```

To create a new bot object:

```py
bot = mebots.Bot('your_bot_shortname', 'bot token (from edit page)')
# You may wish to store your token in a config file or environment variable
```

You can obtain your API key as described [here]().

## Retrieval Functions
`Bot.instance(group_id)` will get information on the instance of your bot that is in a given group. It returns an `Instance` object, which has the property `id`. That string can be passed to the GroupMe API when sending a message as described [here](https://dev.groupme.com/docs/v3#bots_post).

See `example.py` for a complete usage example.

See [this repository](https://github.com/ErikBoesen/mebots-example-python) for an example of a fully-functioning bot in Python using MeBots.

## Author
[Erik Boesen](https://github.com/ErikBoesen)

## License
[GPL](LICENSE)
