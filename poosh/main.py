import argparse


parser = argparse.ArgumentParser(description="""
This small utility allows you sync a local Git repository with a remote Git
repository at an unspecified location on arbitrary server(s), *without git
commits. This allows you to, say, verify code works on a remote server with
heavyweight GPUs, before committing.
""")

parser.add_argument('server', nargs='+', help='Servers w. repos to update')

subparsers = parser.add_subparsers(help='Sub-command help')
go_parser = subparsers.add_parser('go', help='Go to location on server')
go_parser.add_argument('server', help='Server to go to')

poosh_parser = subparsers.add_parser('poosh',
    help='Poosh all files to specified server(s)')
poosh_parser.add_argument('server', nargs='+', help='Servers w. repos to update')


def main():
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
