from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='duckpy',
    version='3.0.0-dev',

    packages=['duckpy', 'duckpy.aio'],
    install_requires=['beautifulsoup4>=4.9.1', 'httpx==0.14.*', 'httpcore>=0.10.2,<0.11'],

    url='https://github.com/AmanoTeam/duckpy',
    python_requires='>=3.6',

    author='Amano Team',
    author_email='contact@amanoteam.com',

    license='MIT',

    description='A simple module for searching on DuckDuckGo',
    long_description=readme,
    long_description_content_type='text/markdown'
)
