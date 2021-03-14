from setuptools import setup

setup(
    name='opprelease',
    version='1.0',
    packages=['opprelease'],
    install_requires=['github3.py==1.2.0', 'click', 'pystache', 'requests'],
    entry_points={
        'console_scripts': ['opprelease = opprelease.__main__:main']
    },
)
