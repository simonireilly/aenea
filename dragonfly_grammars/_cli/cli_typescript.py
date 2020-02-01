# The rules for the typescript command line

from aenea import *

tsccommand = {
    "version": "-v ",
    "watch": "-w ",
    "initialize": "--init",
}

modifiercommand = {
    "all": "*.ts",
}

class TypescriptRule(MappingRule):
    mapping = {
            'typescript <tsccommand> [<modifiercommand>]': Text('tsc %(tsccommand)s %(modifiercommand)s'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('tsccommand', tsccommand),
        Choice('modifiercommand', modifiercommand)
    ]
    defaults = {
        "n": 1,
        "modifiercommand": ""
    }
