# The rules for the yarn command line

from aenea import *

yarncommand = {
    "version": "-v",
    "test": "test",
    "help": "-h ",
    "add": "add",
    "initialize": "--init",
}

modifiercommand = {
    "all": "*.ts",
}


class YarnRule(MappingRule):
    mapping = {
        "yarn <yarncommand> [<text>] [<modifiercommand>]": Text(
            "yarn %(yarncommand)s %(text)s %(modifiercommand)s"
        ),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice("yarncommand", yarncommand),
        Choice("modifiercommand", modifiercommand),
    ]
    defaults = {"n": 1, "text": "", "modifiercommand": ""}
