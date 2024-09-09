#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    readme = f.read()

setup(
    name="click-pendulum",
    version="0.1",
    description="Pendulum datetime support for click.",
    long_description=readme,
    author="Dawson Reid",
    author_email="dreid93@gmail.com",
    url="https://github.com/ddaws/click-datetime",
    license="MIT",
    packages=["click_pendulum"],
    package_data={"click-pendulum": ["README.md"]},
    include_package_data=True,
    install_requires=[
        "click",
    ],
    extras_require={
        "dev": [
            "wheel",
        ]
    },
)
