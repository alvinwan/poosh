import sys
from setuptools import setup


tests_require = []
install_requires = ['appdirs==1.4.3']


VERSION = '0.0.1'


setup(
    name="Poosh",
    version=VERSION,
    author="Alvin Wan",
    author_email='hi@alvinwan.com',
    description="Automatically find, navigate to, and update server copy of local git repository",
    license="BSD",
    url="https://github.com/alvinwan/poosh",
    packages=['poosh'],
    tests_require=tests_require,
    install_requires=install_requires + tests_require,
    download_url='https://github.com/alvinwan/poosh/archive/%s.zip' % VERSION,
    classifiers=[
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={'console_scripts': [
        'poosh = poosh.main:main'
    ]}
)
