from setuptools import setup, find_namespace_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='jaxa-earth',
    version='0.1.2',
    license='TBD',
    description='JAXA Earth API for Python',
    author='JAXA/EORC',
    author_email='Z-ASIST@ml.jaxa.jp',
    url='www.eorc.jaxa.jp',

    include_package_data=True,
    namespace_packages=["jaxa"],
    packages=find_namespace_packages(),

    install_requires = _requires_from_file('requirements.txt'),
)