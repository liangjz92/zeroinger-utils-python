cd ..
python3 setup.py sdist bdist_wheel
sudo twine upload dist/*