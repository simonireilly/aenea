# The rules for the node command line

from aenea import *

npmcommand = {
    "start": "start",
    "test": "test",
    "install": "install",
    "run demo": "run demo",
    "run test services": "run test-services",
    "run test integration": "run test-integration",
}

class NodeRule(MappingRule):
    mapping = {
            'npm <npmcommand>': Text('npm %(npmcommand)s'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('npmcommand', npmcommand)
    ]
    defaults = {
        "n": 1,
    }