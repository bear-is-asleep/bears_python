from setuptools import find_packages, setup

setup(
    name='format',
    version='0.1',
    package_dir={"": "src"},
    #packages=find_packages(where="src")  # will return a list ['spam', 'spam.fizz']
    packages=['format','arr_stuff']

)
