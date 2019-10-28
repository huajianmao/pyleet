init:
	pip3 install -r requirements.txt
	pip3 install -r test_requirements.txt

test:
	pytest
