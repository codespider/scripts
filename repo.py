#!/usr/local/bin/python3
import argparse
import glob
import os
import subprocess

from parse import parse

REPO_HOME = os.environ.get('REPO_HOME', '~/code')

TRED = '\033[31m'  # Red Text
TGREEN = '\033[32m'  # Green Text
TYELLOW = '\033[33m'  # Green Text
ENDC = '\033[m'  # reset to the defaults


def is_git_folder(folder):
    return any(filter(lambda name: name.endswith('.git'), os.listdir(folder)))


def ls_command(args):  # noqa
    projects = list_projects()
    print('\n'.join(projects))
    return projects


def list_projects():
    files = glob.glob(f'{REPO_HOME}/*/*/*')
    projects = [file for file in files if os.path.isdir(file) and is_git_folder(file)]
    return projects


def update_projects(args):  # noqa
    projects = list_projects()
    for project in projects:
        os.chdir(project)
        print(TYELLOW + f' Updating project {project}: ' + ENDC)
        result = subprocess.check_output('git branch', shell=True)
        result = result.decode('unicode_escape').strip()
        if result != '* master':
            print(TRED + ' Not on Master. Skipping... ' + ENDC)
            continue
        result = subprocess.check_output('git diff-index --name-status HEAD', shell=True)
        if result:
            print(TRED + ' There are un-committed changes. Skipping... ' + ENDC)
            continue
        result = subprocess.check_output('git pull', shell=True)
        print(TGREEN + result.decode('unicode_escape') + ENDC)


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
