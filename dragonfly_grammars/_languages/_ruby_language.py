# This is a dragonfly module for Ruby

from aenea import *

ruby_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*(.rb).*'),
    AppContext(executable='Ruby')
    )

class RubyRule(MappingRule):
    mapping = {
            ## Global commands

            'Yardie': Text("# -> Add a documentation \n# \n# @param \n# @return \n"),
            'death': Key("d, e, f, tab"),
            'it <text>': Text("it \"%(text)s\" do \n \n end")
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 1000),
    ]
    defaults = {
        "n": 1,
    }

grammar = Grammar("Ruby", context=ruby_context) # Create grammar
grammar.add_rule(RubyRule()) # Add the rule
grammar.load()  # Load the grammar.

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
