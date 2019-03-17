#!/usr/local/bin/python3
import argparse
import glob
import os

from parse import parse


REPO_HOME = os.environ.get('REPO_HOME', '~/code')


def list_projects(args):
    files = glob.glob(f'{REPO_HOME}/*/*/*')
    projects = [file for file in files if os.path.isdir(file)]
    for project in projects:
        print(project)


def clone_project(args):
    repo, user, project = parse_url(args.url)
    os.system(f'mkdir -p {REPO_HOME}/{repo}/{user}/{project}')
    os.system(f'git clone {args.url} {REPO_HOME}/{repo}/{user}/{project}')


def parse_url(url):
    if url.startswith("git@"):
        repo, user, project = parse('git@{}:{}/{}.git', url)
    elif url.startswith("https://"):
        repo, user, project = parse('https://{}/{}/{}.git', url)
        if '@' in repo:
            _, repo = parse('{}@{}', repo)
    else:
        raise ValueError("git url is not correct/not recognized")
    return repo, user, project


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser.set_defaults(func=list_projects)

    parser_clone = subparsers.add_parser('clone')
    parser_clone.add_argument('url', help='git url to clone', type=str)
    parser_clone.set_defaults(func=clone_project)

    parser_ls = subparsers.add_parser('ls')
    parser_ls.set_defaults(func=list_projects)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
