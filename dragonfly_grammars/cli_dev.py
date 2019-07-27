# Dragonfly module for controlling the Linux terminal
# The context of this file will be strictly for terminal use

from aenea import *

command = {
    'up': 'up',
    'console': 'console',
    'tail': 'tail',
    'test': 'test',
    'stop': 'stop',
    'restart': 'restart',
    'kill': 'down',
    'rake': 'rake',
    'bundle': 'bundle',
    'bundle-install': 'bundle-install',
}

project = {
    'platform': 'platform',
    'gift-cards': 'gift-cards',
    'oms': 'oms',
    'dev': 'dev',
    'webhook-dispatcher': 'webhook-dispatcher',
}

args = {
    'db migrate': 'db:migrate',
    'db setup': 'db:setup',
}

class DevRule(MappingRule):
    mapping = {
        # Git
        "dev directory": Text("cd ~/work/shift-dev") + Key("enter"),
        "voice directory": Text("cd ~/aenea") + Key("enter"),
        "<project> <command>": Text("%(project)s-%(command)s"),
        "<project> <command> <args>": Text("%(project)s-%(command)s args='%(args)s'"),
        "make <command>": Text("make %(command)s"),
        "make <project> <command>": Text("make %(project)s-%(command)s"),
        "make <project> <command> <args>": Text("make %(project)s-%(command)s args='%(args)s'"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('command', command),
        Choice('project', project),
        Choice('args', args),
    ]
    defaults = {
        "n": 1,
    }
