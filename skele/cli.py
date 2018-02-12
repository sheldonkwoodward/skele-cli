from inspect import getmembers, isclass
from docopt import docopt

from . import __version__ as version


def main():
    import skele.commands
    options = docopt(__doc__, version=version)

    for (k, v) in options.items():
        if hasattr(skele.commands, k) and v:
            module = getattr(skele.commands, k)
            skele.commands = getmembers(module, isclass)
            command = [command[1] for command in skele.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
