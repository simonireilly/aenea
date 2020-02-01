# A mapping syntax for applications command line

from aenea import *

class ShiftRule(MappingRule):
    mapping = {
            # Launching the application

            'shifty boot': Text('./bin/dev/boot') + Key('enter'),
            'shifty yawn': Text('./bin/dev/yarn '),
            'shifty post': Text('psql -p 5432 -h localhost -U postgres'),
            'shifty console': Text('./bin/dev/console') + Key('enter'),
            'shifty test': Text('./bin/dev/rspec '),
            'shifty rails': Text('./bin/dev/rails '),
            'shifty bundle': Text('./bin/dev/bundle '),
            'shifty break': Text('./bin/dev/rake '),
            'consultant (<text>)': Text("Tenant.switch('%(text)s') {binding.pry}")
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
