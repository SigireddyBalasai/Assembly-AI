from distutils.core import setup

import setuptools


def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README

def reqs():
    with open("requirements.txt", "r") as f:
        reqs = [line.strip() for line in f]
        return reqs


setup(
    name="AssembleAI",
    packages=['AssembleAI'],
    version="0.0.0.0.20",
    license="MIT",
    description="Assemble AI",
    author="SigireddyBalasai",
    author_email="sigireddybalasai@gmail.com",
    install_requires=reqs(),
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
