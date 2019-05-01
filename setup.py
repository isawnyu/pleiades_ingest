import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pleiades_ingest",
    version="0.0.1",
    author="Tom Elliott",
    author_email="tom.elliott@nyu.edu",
    description="'specifications, tools, and tests for ingesting external data into pleiades'",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pleiades.stoa.org",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['airtight', 'better_exceptions'],
    python_requires='>=3.7.3'
)
