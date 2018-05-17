from setuptools import setup

setup(
    name='gndrv',
    version='0.1',
    description='The biological package manager',
    url='http://github.com/gndrv/gndrv',
    author='Isaac Ellmen',
    author_email='isaac@gndrv.com',
    packages=['gndrv'],
    entry_points={
        'console_scripts': ['gndrv=gndrv.command_line:main'],
    }
)
