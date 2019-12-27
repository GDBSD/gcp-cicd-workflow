from distutils.core import setup

setup(
    name='gcp',
    version='0.1.0',
    author='Gary Biggs',
    author_email='gary_biggs@ultimatesoftware.com',
    packages=['src', 'tests'],
    description='POC for setting up a GCP CI/CD pipeline.',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest==5.3.2",
        "pytest-cov==2.8.1",
    ],
)