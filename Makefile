.DEFAULT_GOAL := check

init:
	pip3 install -r requirements.txt
	pip3 install -r test_requirements.txt

update:
	python3 progress.py

style:
	pycodestyle .

test:
	pytest --cov=./

check: update style test
