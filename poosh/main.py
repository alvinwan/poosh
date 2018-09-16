"""
Automatically find, navigate to, and update server copy of local git repository

Usage:
poosh to <server> [<server> <server> ...]
poosh go <server>
"""

import argparse
import subprocess


parser = argparse.ArgumentParser(description="""
This small utility allows you sync a local Git repository with a remote Git
repository at an unspecified location on arbitrary server(s), *without git
commits. This allows you to, say, verify code works on a remote server with
heavyweight GPUs, before committing.
""")

parser.add_argument('--path', help='Path to search in', default='~')

subparsers = parser.add_subparsers(help='Sub-command help', dest='command')
go_parser = subparsers.add_parser('go',
    help='Go to location on server')
go_parser.add_argument('server', help='Server to go to')

poosh_parser = subparsers.add_parser('to',
    help='Push all files to specified server(s)')
poosh_parser.add_argument('server', nargs='+', help='Servers w. repos to update')


def main():
    args = parser.parse_args()
    if args.command == 'go':
        subprocess.check_call(["./go.sh", args.server, args.path])
    else:
        for server in args.server:
            subprocess.check_call(["./poo.sh", server, args.path])


if __name__ == '__main__':
    main()
