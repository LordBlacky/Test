SHELL := /bin/zsh
venv:
	python3 -m venv venv

install-requirements: venv
	venv/bin/pip install -r requirements-dev.txt

test: install-requirements
	venv/bin/pytest --cov=src --cov-fail-under=80 --maxfail=1

clean:
	rm -rf **/venv
	rm -rf **/.coverage
	rm -rf **/.pytest_cache
	rm -rf **/__pycache__

ci: test clean
