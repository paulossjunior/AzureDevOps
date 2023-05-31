rm -rf dist build
python setup.py bdist_wheel
python -m twine upload dist/*
