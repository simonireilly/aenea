# A mapping syntax for heroku command line

from aenea import *

command = {
    'run': 'run',
    'accounts': 'accounts',
    'help': 'help',
    'create': 'create',
    'container': 'container:',
    'stack': 'stack:',
}

actions = {
    'login': 'login',
    'set': 'set',
}

arguments = {
    'container': 'container',
}

class HerokuRule(MappingRule):
    mapping = {
        "heroku <command>": Text("heroku %(command)s"),
        "heroku <command> <actions>": Text("heroku %(command)s%(actions)s"),
        "heroku <command> <actions> <arguments>": Text("heroku %(command)s%(actions)s %(arguments)s"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('command', command),
        Choice('actions', actions),
        Choice('arguments', arguments),
    ]
    defaults = {
        "n": 1,
    }
