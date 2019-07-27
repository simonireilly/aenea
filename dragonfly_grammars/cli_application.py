# A mapping syntax for applications command line

from aenea import *

class ApplicationRule(MappingRule):
    mapping = {
            # Basic root applications.
            'post': Text('psql '),
            'really': Text('rails '),
            'doctor': Text('docker '),
            'doctor compose': Text('docker-compose '),
            'subtle': Text('subl .') + Key('enter'),
            # Rails commands
            'bundle install': Text('bundle install'),
            'bundle update': Text('bundle update'),
            'bundle exec': Text('bundle exec '),
            'really my':  Text('rails db:migrate'),
        }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
