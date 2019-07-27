# A mapping syntax for buffalo command line

from aenea import *

command = {
  'db': 'db',
  'destroy': 'destroy',
  'dev': 'dev',
  'fix': 'fix',
  'generate': 'generate',
  'help': 'help',
  'info': 'info',
  'new': 'new',
  'plugins': 'plugins',
  'pop': 'pop',
  'routes': 'routes',
  'setup': 'setup',
  'task': 'task',
  'test': 'test',
}

actions = {
    'help': 'help',
    'migrate': 'migrate',
    'create': 'create',
    'destroy': 'destroy',
    'resource': 'resource',
}

arguments = {
  'up': 'up',
  'down': 'down',
}

class BuffaloRule(MappingRule):
    mapping = {
        "buffalo <command>": Text("buffalo %(command)s"),
        "buffalo <command> <actions>": Text("buffalo %(command)s %(actions)s"),
        "buffalo <command> <actions> <arguments>": Text("buffalo %(command)s %(actions)s %(arguments)s"),
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
