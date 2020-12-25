lint:
	autopep8 --in-place --recursive --exclude venv python

tests:
	pytest -rf -v python
