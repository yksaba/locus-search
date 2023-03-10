from setuptools import setup, find_packages

setup(
    name='locus_search',
    version='1.1.0',
    install_requires=['numpy', 'pandas', 'beautifulsoup4', 'requests'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)