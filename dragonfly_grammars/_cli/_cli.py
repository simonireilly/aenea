# Dragonfly module for controlling the Linux terminal
# The context of this file will be strictly for terminal use

from aenea import *

import cli_application
import cli_buffalo
import cli_dev
import cli_elixir
import cli_git
import cli_heroku
import cli_node
import cli_shift
import cli_terminator
import cli_typescript
import cli_yarn

terminal_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match="regex", title="(?i).*simon@simon.*"),
    AppContext(executable="Terminal"),
)


class TerminalRule(MappingRule):
    mapping = {
        ## Global Commands
        # Open folder
        "open folder": Text("nautilus .") + Key("enter"),
        # The pseudo command
        "master": Text("sudo "),
        # Managing folders and files.
        "folders": Text("ls") + Key("enter"),
        # Add a folder
        "Add folder": Text("mkdir "),
        "touch": Text("touch "),
        "navigate": Text("cd "),
        "historian": Key("c-r"),
        # Managing terminal windows.
        "Tony [<n>]": Key("a-%(n)s"),
        "Exeter": Key("c-d"),
        "newer": Key("c-t"),
        "clearer": Key("c-l"),
        "cleaner": Key("c-u"),
        # Clearing and cancelling actions.
        "squash": Key("ca-c"),
        "crush": Key("cs-d"),
        # Killing all programs on a port
        "desiccate": Text("kill -9 $(lsof -ti :)"),
        # Killing all programs on a port
        "reveal": Text("lsof -i :"),
        # Scroll up in the terminal
        "decline": Key("s-pgdown"),
        # Scroll down in the terminal
        "incline": Key("s-pgup"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }


grammar = Grammar("terminal", context=terminal_context)

# Command line interfaces
grammar.add_rule(cli_application.ApplicationRule())
grammar.add_rule(cli_buffalo.BuffaloRule())
grammar.add_rule(cli_dev.DevRule())
grammar.add_rule(cli_elixir.ElixirRule())
grammar.add_rule(cli_git.GitRule())
grammar.add_rule(cli_heroku.HerokuRule())
grammar.add_rule(cli_node.NodeRule())
grammar.add_rule(cli_typescript.TypescriptRule())
grammar.add_rule(cli_shift.ShiftRule())
grammar.add_rule(cli_terminator.TerminatorRule())
grammar.add_rule(cli_yarn.YarnRule())

# Master rule
grammar.add_rule(TerminalRule())

grammar.load()


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
