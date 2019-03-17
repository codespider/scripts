#!/usr/local/bin/python3
import glob
import os
import subprocess

from parse import parse

REPO_HOME = os.environ.get('REPO_HOME', '~/code')

TRED = '\033[31m'  # Red Text
TGREEN = '\033[32m'  # Green Text
TYELLOW = '\033[33m'  # Green Text
ENDC = '\033[m'  # reset to the defaults


def _is_git_folder(folder):
    return any(filter(lambda name: name.endswith('.git'), os.listdir(folder)))


def list_projects():
    files = glob.glob(f'{REPO_HOME}/*/*/*')
    projects = [file for file in files if os.path.isdir(file) and _is_git_folder(file)]
    return projects


def update_projects():
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


def clone_project(url):
    repo, user, project = _parse_url(url)
    os.system(f'mkdir -p {REPO_HOME}/{repo}/{user}/{project}')
    os.system(f'git clone {url} {REPO_HOME}/{repo}/{user}/{project}')


def _parse_url(url):
    if url.startswith("git@"):
        repo, user, project = parse('git@{}:{}/{}.git', url)
    elif url.startswith("https://"):
        repo, user, project = parse('https://{}/{}/{}.git', url)
        if '@' in repo:
            _, repo = parse('{}@{}', repo)
    else:
        raise ValueError("git url is not correct/not recognized")
    return repo, user, project
