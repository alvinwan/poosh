"""
Automatically find, navigate to, and update server copy of local git repository

Usage:
poosh to <server> [<server> <server> ...]
poosh go <server>
"""

import argparse
import subprocess
import os

from .utils.usersettings import Settings

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


parser = argparse.ArgumentParser(description="""
This small utility allows you sync a local Git repository with a remote Git
repository at an unspecified location on arbitrary server(s), *without git
commits. This allows you to, say, verify code works on a remote server with
heavyweight GPUs, before committing.
""")

parser.add_argument('--path', help='Path to search in')

subparsers = parser.add_subparsers(help='Sub-command help', dest='command')
go_parser = subparsers.add_parser('go',
    help='Go to location on server')
go_parser.add_argument('server', help='Server to go to')

poosh_parser = subparsers.add_parser('to',
    help='Push all files to specified server(s)')
poosh_parser.add_argument('server', nargs='*',
    help='Servers with repos to update. If no servers are listed, push to all '
         'servers listed in the configuration, `poosh list-servers`')

set_parser = subparsers.add_parser('set',
    help='Add default server or set value for existing server')
set_parser.add_argument('server',
    help='Server to add to configuration or edit configuration for')
set_parser.add_argument('--path', help='Path to search over, for server')

unset_parser = subparsers.add_parser('unset', help='Remove server')
unset_parser.add_argument('server',
    help='Server to remove from default configuration')

list_parser = subparsers.add_parser('list', help='List default servers')

config_parser = subparsers.add_parser('config', help='Edit configuration file')
config_parser.add_argument('--path', help='View path of configuration file',
    action='store_true')


def get_script_path(script):
    return os.path.join(CURRENT_PATH, script)


def main():
    args = parser.parse_args()

    settings = Settings('com.alvinwan.apps.Poosh')
    settings.load_settings()

    # Configuration options
    if args.command == 'set':
        settings.add_setting(args.server, str, '')
        settings[args.server] = args.path or ''
        settings.save_settings()
    elif args.command == 'unset':
        settings.remove_setting(args.server)
        settings.save_settings()
    elif args.command == 'list':
        for server, path in settings.items():
            print(' * [{}] {}'.format(server, path or '(no path)'))
    elif args.command == 'config':
        if args.path:
            print(settings.settings_file)
            return
        subprocess.check_call(["nano", settings.settings_file])

    # Poosh utility functions
    elif args.command == 'go':
        subprocess.check_call([get_script_path("go.sh"), args.server, args.path])
    elif args.command == 'to':
        servers = args.server or list(settings.keys())
        for server in servers:
            command = [get_script_path("poo.sh"), server]
            path = args.path or settings.get(server, None)
            if path:
                command.append(path)
            subprocess.check_call(command)
    else:
        # TODO: do what?
        pass


if __name__ == '__main__':
    main()
