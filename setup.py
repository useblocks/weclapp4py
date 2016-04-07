from setuptools import setup

version = '0.0.1'

setup(
    name='weclapp4py',
    description="Abstracts the weclapp api as python lib",
    version=version,
    long_description='weclapp4py provides a wrapper for python projects around the most common weclapp api calls.',
    packages="weclapp4py",
    include_package_data=True,
    author='Daniel Woste',
    author_email='daniel.woste@useblocks.com',
    url='https://github.com/useblocks/weclapp4py',
    license='MIT',
    install_requires=[
        'requests'
    ]
)
