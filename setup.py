from setuptools import setup
from apijet.version import __version__
setup(
    name="apiJet",
    version=f"{__version__}",
    author="Alfonso Farruggia",
    author_email="alfonso.farruggia@gmail.com",
    description=("CLI tool to generate and deploy API"),
    license="BSD",
    keywords="api, cli",
    url="git.url",
    packages=['apijet', 'tests']
)
