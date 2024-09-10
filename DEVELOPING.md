# Contributing Guide

Thank you for considering contributing to this project! Here are some guidelines to help you get started.

## Installing Dependencies

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install the dependencies, follow these steps:

1. Install Poetry if you haven't already:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install the project dependencies:

```bash
poetry install
```

## Building the Package

To build the package, run the following command:

```bash
poetry build
```

This will create a source distribution and a wheel in the `dist` directory.

## Publishing to PyPI

To publish the package to PyPI, follow these steps:

1. Ensure you have a valid PyPI account and have configured your credentials using Poetry:

```bash
poetry config pypi-token.pypi <your-token>
```

2. Publish the package:

```bash
poetry publish --build
```

This will upload the package to PyPI, making it available for others to install.
