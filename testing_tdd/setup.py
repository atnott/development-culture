from setuptools import setup, find_packages

setup(
    name='atnott-ndfl-test-123',
    version='0.0.2',
    long_description="Tax calculator",
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)
