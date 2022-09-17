from setuptools import find_packages, setup
from apijet.version import __version__
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="apijet",
    version=f"{__version__}",
    author="Alfonso Farruggia",
    author_email="alfarruggia@gmail.com",
    description=("A command line tool to deploy python Rest APIS in 20 secs"),
    license="MIT",
    keywords="api, mongodb, rest-api, cli-app, fastapi",
    url="https://github.com/Arfius/apijet",
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    entry_points={
        'console_scripts': ['apijet=apijet.main:main']
    },
    license_files=('LICENSE',),
    python_requires='>=3.8',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
