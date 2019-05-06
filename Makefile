
SHELL=/bin/bash

.DEFAULT_GOAL := help

python_pkg = bgapi

ifeq ($(OS),Windows_NT)
	python3 = python
	pip3 = pip
	sudo =
else
	python3 = python3
	pip3 = pip3
	sudo = sudo
endif

# Install python package referencing locally
install_python_pkg_locally:
	$(pip3) install -e .

# Install python package system-wide
install_python_pkg:
	$(sudo) $(pip3) install .

# Uninstall python package
uninstall_python_pgk:
	$(sudo) $(pip3) uninstall -y $(python_pkg)

# Remove python install-related stuff
clean_python_crap:
	$(sudo) rm -rf dist
	$(sudo) rm -rf build
	$(sudo) rm -rf src/*egg*

# Create python wheel
python_wheel:
	$(python3) setup.py sdist bdist_wheel

# Upload python wheel to pypiserver@monster
upload_wheel:
	twine upload --repository-url http://monster:8080/ dist/*.whl

# Shows a help message using the comment above each target
help:
	@ paste -s -d",\n" <(egrep -w "^[_a-zA-Z0-9]+:" -B1 Makefile | sed "/--/d") \
		| sed "s/:.*$$//g" \
		| sed "s/\(.*\),\(.*\)/\2 \1/g" \
		| column -t -s \# | tr ":" " " \
		| sed "s/ \([ ]\+\) /@\1@/g" \
		| sed "s/  /--/g" \
		| tr "@" " " \
		| nl
