.PHONY: update test clean clean-pyc lint

test:
	pytest

lint:
	flake8

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean: clean-pyc
	rm -f MANIFEST
	rm -rf build dist

update:
	pipenv update

install:
	ln -s ${CURDIR}/repo.py /usr/local/bin/repo
