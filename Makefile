# Create python wheel
python_wheel:
	python3 setup.py sdist bdist_wheel

# Upload python wheel to pypiserver@monster
upload_wheel:
	twine upload --repository-url http://monster:8080/ dist/*.whl

