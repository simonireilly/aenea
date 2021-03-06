# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from natlink import setMicState
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Mimic,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')


release = Key("shift:up, ctrl:up, alt:up")


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")


# For repeating of characters.
specialCharMap = {
    "(bar|vertical bar|pipe)": "|",
    "(dash|minus|hyphen)": "-",
    "dit": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk)": "*",
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equal": "=",
    "plus": "+",
    "space": " ",
    "tilde": "~",
    "bang": "!",
    "question": "?",
    "caret": "^",
}

# Modifiers for the press-command.
modifierMap = {
    "alt": "a",
    "control": "c",
    "shift": "s",
    "super": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt": "alt",
    "control": "ctrl",
    "super": "win",
}

letterMap = {
    "(alpha)": "a",
    "(bravo) ": "b",
    "(charlie) ": "c",
    "(delta) ": "d",
    "(echo) ": "e",
    "(foxtrot) ": "f",
    "(golf) ": "g",
    "(hotel) ": "h",
    "(indigo) ": "i",
    "(juliet) ": "j",
    "(kilo) ": "k",
    "(lima) ": "l",
    "(mike) ": "m",
    "(november) ": "n",
    "(Oscar) ": "o",
    "(papa | Papa) ": "p",
    "(quebec) ": "q",
    "(romeo) ": "r",
    "(sierra) ": "s",
    "(tango) ": "t",
    "(uniform) ": "u",
    "(victor) ": "v",
    "(whiskey) ": "w",
    "(x-ray) ": "x",
    "(yankee) ": "y",
    "(zulu) ": "z",
}

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}

# F1 to F12. (do these actually work?)
functionKeyMap = {
    'F one': 'f1',
    'F two': 'f2',
    'F three': 'f3',
    'F four': 'f4',
    'F five': 'f5',
    'F six': 'f6',
    'F seven': 'f7',
    'F eight': 'f8',
    'F nine': 'f9',
    'F ten': 'f10',
    'F eleven': 'f11',
    'F twelve': 'f12',
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(functionKeyMap)


def handle_word(text):
    #words = map(list, text)
    #print text
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
    {
        # Navigation keys.
        "up [<n>]": Key("up:%(n)d"),
        "down [<n>]": Key("down:%(n)d"),
        "left [<n>]": Key("left:%(n)d"),
        "right [<n>]": Key("right:%(n)d"),
        "page up [<n>]": Key("pgup:%(n)d"),
        "page down [<n>]": Key("pgdown:%(n)d"),
        "home": Key("home"),
        "doc home": Key("c-home/3"),
        "doc end": Key("c-end/3"),

        # Functional keys.
        "space": release + Key("space"),
        "space [<n>]": release + Key("space:%(n)d"),
        "(enter|slap|slop) [<n>]": release + Key("enter:%(n)d"),
        "tab [<n>]": Key("tab:%(n)d"),
        "delete [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "backspace [<n>]": release + Key("backspace:%(n)d"),
        "application key": release + Key("apps/3"),
        "win key": release + Key("win/3"),
        # Global command words.
        'plop [<n>]': release + Key('c-v:%(n)d'),
        "cop [that]":release + Key("c-c/3"),
        "cut [that]": release + Key("c-x/3"),
        "undo [<n>] ": release + Key("ctrl:down, z:%(n)d, ctrl:up"),
        "redo [<n>] ": release + Key("ctrl:down, shift:down, z:%(n)d, shift:down, ctrl:up"),
        "blanket": release + Key("c-a/3"),

        "[(hold|press)] alt": Key("alt:down/3"),
        "release alt": Key("alt:up"),
        "[(hold|press)] shift": Key("shift:down/3"),
        "release shift": Key("shift:up"),
        "[(hold|press)] control": Key("ctrl:down/3"),
        "release control": Key("ctrl:up"),
        "release [all]": release,
        "press key <pressKey>": Key("%(pressKey)s"),

        ## Closures.

        "rockets": Key("langle, rangle, left/3"),
        "sprockets": Key("langle, slash, rangle, left/3"),
        "dockets": Key("langle, space, slash, rangle, left:3/3"),
        "[square] brackets": Key("lbracket, rbracket, left/3"),
        "[curly] braces": Key("lbrace, rbrace, left/3"),
        "(para)": Key("lparen, rparen, left/3"),
        "quotes": Key("dquote/3, dquote/3, left/3"),
        "backtick": Key("backtick:1"),
        "backticks": Key("backtick:2, left"),
        "Quinn": Key("squote, squote, left/3"),
        "pillars": Text("||") + Key("left/3"),

        # Shorthand multiple characters.
        "double <char>": Text("%(char)s%(char)s"),
        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape": Key("escape, escape"),  # Exiting menus.

        # Punctuation and separation characters, for quick editing.
        "colon [<n>]": Key("colon/2:%(n)d"),
        "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
        "comma [<n>]": Key("comma/2:%(n)d"),
        "period": Key("dot"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
        "underscore [<n>]": Key("underscore/2:%(n)d"),
        "<letters>": Text("%(letters)s"),
        "<char>": Text("%(char)s"),

        'langle [<n>]': Key('langle:%(n)d'),
        'lace [<n>]':   Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':   Key('lbracket:%(n)d'),
        'len [<n>]':    Key('lparen:%(n)d'),
        'rangle [<n>]': Key('rangle:%(n)d'),
        'race [<n>]':   Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':   Key('rbracket:%(n)d'),
        '(ren|wren) [<n>]':   Key('rparen:%(n)d'),

        "act [<n>]": Key("escape:%(n)d"),
        'care':        Key('home'),
        '(doll|dole)': Key('end'),
        'chuck [<n>]':       Key('del:%(n)d'),
        'tail [<n>]':     Key('backspace:%(n)d'),
        "sieve": Key("c-s"),
        "arrow": Text(" => "),

        #### Lines
        'line down [<n>]': Key('home:2, shift:down, end:2, shift:up, c-x, del, down:%(n)d, home:2, enter, up, c-v'),
        'lineup [<n>]':    Key('home:2, shift:down, end:2, shift:up, c-x, del, up:%(n)d, home:2, enter, up, c-v'),
        'nab [<n>]':       Key('home:1, shift:down, down:%(n)d, up, end:2, shift:up, c-c, end:2'),
        'squishy [<n>]':   Key('end:2, space') + Text('_') + Key('down, home, c-backspace'),
        'bumper':           Key('s-end:2, del'),
        'wacky':            Key('s-home:2, del'),
        'trance [<n>]':    Key('home:1, shift:down, down:%(n)d, up, end:2, shift:up, c-c, end:1, enter, c-v'),
        'wipe [<n>]':      Key('home:2, shift:down, down:%(n)d, up, end:2, del, shift:up, backspace'),
        # Go to row
        'leap [<n>]':      Key('c-g') + Text('%(n)s') + Key('enter'),

        #### Words
        'bump [<n>]':      Key('cs-right:%(n)d, del'),
        'whack [<n>]':     Key('cs-left:%(n)d, del'),

        'gope [<n>]':  Key('pgup:%(n)d'),
        'drop [<n>]':  Key('pgdown:%(n)d'),

        'lope [<n>]':  Key('c-left:%(n)d'),
        'rope [<n>]':  Key('c-right:%(n)d'),

        'hexadecimal': Text("0x"),
        'suspend': Key('c-z'),

        'word <text>': Function(handle_word),
        'number <num>': Text("%(num)d"),
        'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Text corrections.
        "(add|fix) missing space": Key("c-left/3, space, c-right/3"),
        "(delete|remove) (double|extra) (space|whitespace)": Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),  # @IgnorePep8
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)


class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000000),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }
