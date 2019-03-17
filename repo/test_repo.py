from repo.domain import _parse_url


def test_parse_url():
    repo, team, project = _parse_url('git@github.com:codespider/Dockerfiles.git')
    assert (repo, team, project) == ('github.com', 'codespider', 'Dockerfiles')


def test_parse_url_1():
    repo, team, project = _parse_url('https://github.com/codespider/Dockerfiles.git')
    assert (repo, team, project) == ('github.com', 'codespider', 'Dockerfiles')


def test_parse_url_2():
    repo, team, project = _parse_url('https://codespider@github.com/codespider/Dockerfiles.git')
    assert (repo, team, project) == ('github.com', 'codespider', 'Dockerfiles')
