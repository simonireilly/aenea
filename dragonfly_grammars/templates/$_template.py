# This is a template.
# Please replace this with your own documentation.

LEADER = 'comma'

from aenea import *

terminal_context = aenea.wrappers.AeneaContext(
    ProxyAppContext(match='regex', title='(?i).*simon@simon.*'),
    AppContext(executable='Terminal')
    )
