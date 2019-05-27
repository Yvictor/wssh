from setuptools import setup


setup(
    name='wssh',
    version='0.1.1',
    author='Andrea Luzzardi <aluzzardi@gmail.com>, Yvictor',
    packages=[
        'wssh'
        ],
    scripts=[
        'bin/wssh',
        'bin/wsshd'
        ],
    install_requires=[
        'gevent', 
        'flask', 
        'paramiko', 
        'gevent-websocket',
        ],
    package_data={'': ['static/*', 'templates/*']},
    include_package_data=True,
    zip_safe=False
)
