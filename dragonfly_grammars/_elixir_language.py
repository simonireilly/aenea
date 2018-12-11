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
}

class ElixirRule(MappingRule):
    mapping = {

            ## Definitions
            'death': Key('d,e,f'),
            'death mod': Key('d,e,f,m,o,d,enter'),

            ## Common commands
            'change set': Text('changeset'),
            'I oh <elixircommand>': Text("IO%(elixircommand)s"),
            'function': Text("fn "),

            ## Syntaxes
            'dagger': Text('|> '),
            'blade': Text(' -> '),
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
