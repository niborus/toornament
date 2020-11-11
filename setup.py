from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="toornament",
    version="0.0.1",
    author="niborus",
    author_email="niborus.management@gmail.com",
    description="A Python wrapper for the Toornament API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niborus/toornament",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6', install_requires = ['requests']
)
