import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ontotools",
    version="0.7.0-post1",
    author="Edmond Chuc",
    author_email="e.chuc@uq.edu.au",
    description="Python ontology tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["ontotools = ontotools.cli:app"]},
    install_requires=[
        "rdflib>=6.1.1,<7.0.0",
        "typer>=0.4.0,<1.0.0",
        "httpx>=0.23.0,<0.24.0",
        "jinja2>=3.1.2,<3.2.0",
        "rich>=12.6.0,<12.7.0",
    ],
)
