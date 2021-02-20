try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='python_programming_demo_app',
    version='0.0.1',
    packages=['roboter', 'roboter.models', 'roboter.controller', 'roboter.views'],
    package_data={ 'roboter': ['template/*.txt']},
)