install:
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
uninstall:
	virtualenv --clear .venv