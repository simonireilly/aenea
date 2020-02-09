# Dragonfly module for controlling the Linux terminal
# The context of this file will be strictly for terminal use

from aenea import *

command = {
    "up": "up",
    "console": "console",
    "tail": "tail",
    "test": "test",
    "stop": "stop",
    "restart": "restart",
    "kill": "down",
    "rake": "rake",
    "bundle": "bundle",
    "bundle-install": "bundle-install",
    "db migrate": "db-migrate",
    "db setup": "db-setup",
}

project = {
    "platform": "platform-",
    "gift-cards": "gift-cards-",
    "oms": "oms-",
    "dev": "dev-",
    "webhook-dispatcher": "webhook-dispatcher-",
}

args = {"test": "args='RAILS_ENV=test'"}


class DevRule(MappingRule):
    mapping = {
        # Git
        "dev directory": Text("cd ~/work/shift-dev") + Key("enter"),
        "voice directory": Text("cd ~/aenea") + Key("enter"),
        "[<project>] [<command>] [<args>]": Text("%(project)s%(command)s %(args)s"),
        "make [<project>] [<command>] [<args>]": Text(
            "make %(project)s%(command)s %(args)s"
        ),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice("command", command),
        Choice("project", project),
        Choice("args", args),
    ]
    defaults = {
        "n": 1,
        "command": "",
        "project": "",
        "args": "",
    }
