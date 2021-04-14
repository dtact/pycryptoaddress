from setuptools import setup, find_packages

setup(
    name='pycryptoaddress',
    version='0.1.0',
    description='Crypto addresses from text',
    author='Remco Verhoef',
    author_email='remco.verhoef@dtact.com',
    packages=find_packages(where='src'),  # Required
    package_dir={'': 'src'},  # Optional
    install_requires=[
    ]
)
