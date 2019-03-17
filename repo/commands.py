#!/usr/local/bin/python3
import argparse

from repo.domain import list_projects, clone_project, update_projects


def ls_command(args):  # noqa
    projects = list_projects()
    print('\n'.join(projects))


def clone_project_command(args):
    clone_project(args.url)


def update_projects_commans(arg):  # noqa
    update_projects()


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=ls_command)

    parser_clone = subparsers.add_parser('clone')
    parser_clone.add_argument('url', help='git url to clone', type=str)
    parser_clone.set_defaults(func=clone_project)

    parser_ls = subparsers.add_parser('ls')
    parser_ls.set_defaults(func=ls_command)

    parser_update = subparsers.add_parser('pull')
    parser_update.set_defaults(func=update_projects)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
