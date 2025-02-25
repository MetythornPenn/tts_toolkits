install:
	rm -rf *.egg-info/ dist/ tts_toolkits.egg-info
	pip install -e .

remove:
	pip uninstall tts_toolkits -y

build-docs:
	mkdocs build

deploy-docs:
	mkdocs gh-deploy

serve-docs:
	mkdocs serve

build:
	rm -rf build dist
	# python setup.py sdist bdist_wheel

push:
	twine upload dist/*
