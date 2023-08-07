from setuptools import setup, find_packages
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
    name='pyrtlib',
    version='1.0.1',
    include_package_data=True,
    package_dir={'': 'pyrtlib'},
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=required,
    project_urls={
        'documentation': 'https://satclop.github.io/pyrtlib',
        'repository': 'https://github.com/SatCloP/pyrtlib'
    },
    url='',
    license='GPLv3',
    author='slarosa',
    author_email='salvatore-larosa@cnr.it',
    description='pyrtlib - Radiative Transfer library',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=find_packages('pyrtlib')
)
