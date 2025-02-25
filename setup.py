import os
from setuptools import setup, find_packages


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

requirements = [
    "regex",
]

setup(
    name="tts-toolkits",
    version="0.1.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
    },
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/MetythornPenn/tts-toolkits.git',
    license='Apache Software License 2.0',
    author = 'Metythorn Penn',
    author_email = 'metythorn@gmail.com',
    keywords='tts-toolkits',
    description='tts-toolkits is a collection of functions to work with khmer text to speech',
    install_requires=requirements,
    long_description=(read('README.md')),
    long_description_content_type='text/markdown',
	classifiers= [
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
	],
)
