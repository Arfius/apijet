from setuptools import find_packages, setup
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
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    entry_points={
        'console_scripts': ['apijet=apijet.main:main']
    }
)
