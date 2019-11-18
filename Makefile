.DEFAULT_GOAL := check

init:
	pip3 install -r requirements.txt
	pip3 install -r test_requirements.txt

update: check
	python3 progress.py
	git diff README.md

style:
	pycodestyle .

test:
	pytest --cov=./

check: style test
