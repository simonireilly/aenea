# A mapping syntax for elixir command line

from aenea import *

phoenixcommand = {
    "new": ".new",
    "server": ".server",
    "Jane context": ".gen.context",
    "Jane html": ".gen.html",
}

mixedcommand = {
    "depth get": "deps.get",
    "ecto setup": "ecto.setup",
    "compile": "compile",
    "new": "new",
    "test": "test",
    "local hex": "local.hex",
    "archive install": "archive.install",
    "phoenix new": "phx.new",
    "phoenix server": "phx.server",
    "ecto create": "ecto.create"
}

iexcommand = {
    "mix": "-S mix",
}

class ElixirRule(MappingRule):
    mapping = {
            ## Commands
            'licks': Text("elixir "),
            'mix <mixedcommand> [<text>]': Text("mix %(mixedcommand)s %(text)s"),
            'ecto': Text("ecto"),
            'Ickes <iexcommand>': Text("iex %(iexcommand)s"),
            'phoenix <phoenixcommand>': Text("phx%(phoenixcommand)s"),
            ## File affixes
            'ex file': Text('.ex'),
            'ex script': Text('.exs'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('phoenixcommand', phoenixcommand),
        Choice('mixedcommand', mixedcommand),
        Choice('iexcommand', iexcommand),
    ]
    defaults = {
        "n": 1,
        "text": "",
    }
