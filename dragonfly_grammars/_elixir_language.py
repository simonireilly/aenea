# This is a dragonfly module for Elixir

from aenea import *

elixir_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*(.ex).*'),
    AppContext(executable='Elixir')
    )

elixircommand = {
    "gets": ".gets",
    "puts": ".puts",
    "inspect": ".inspect",
    "reduce": ".reduce",
    "count": ".count",
    "zip": ".zip",
    "into": ".into",
    "each": ".each",
    "trim": ".trim",
    "map": ".map",
    "downcase": ".downcase",
    "upcase": ".upcase",
    "reverse": ".reverse",
    "await": ".await",
    "async": ".async",
}

class ElixirRule(MappingRule):
    mapping = {

            ## Definitions
            'define function': Text('def') + Pause("20") + Key('tab'),
            'define module': Text('defmo') + Pause("20") + Key('tab'),

            ## Compound commands
            'I oh <elixircommand>': Text("IO%(elixircommand)s"),
            'Enum <elixircommand>': Text("Enum%(elixircommand)s"),
            'String <elixircommand>': Text("String%(elixircommand)s"),
            'Task <elixircommand>': Text("Task%(elixircommand)s"),

            ## Common commands
            'change set': Text('changeset'),
            'function': Text("fn "),

            ## Syntaxes
            'dagger': Text('|> '),
            'blade': Text(' -> '),
            'sigal': Text('~s'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 1000),
        Choice('elixircommand', elixircommand)
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("Elixir", context=elixir_context) # Create grammar
grammar.add_rule(ElixirRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
