# aa-simple-wanderer-acls

This is a plugin that will manage ACLs in Wanderer, ensuring that they stay synchronized with states, groups, factions, et cetera in Alliance Auth.

[![CI/CD Pipeline](https://github.com/GoosefleetEO/aa-simple-wanderer-acls/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/GoosefleetEO/aa-simple-wanderer-acls/actions/workflows/ci-cd.yaml)
[![license](https://img.shields.io/badge/license-MIT-green)](https://github.com/GoosefleetEO/aa-simple-wanderer-acls#MIT-1-ov-file)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![chat](https://img.shields.io/discord/790364535294132234)](https://discord.goosegoo.se)

## Features

- Manages Wanderer ACLs with a swagger client using the built-in wanderer APIs
- Adds and removes characters from ACLs as needed using signals on relevant model updates without user interaction
- Regularly verifies ACL integrity with a periodic task

## How to use it

TODO: Instructions

`INSTALLED_APPS += ['wanderer_acls']`

## Running the test suite

This app comes with a pre-configured test suite based on [tox](https://tox.wiki/en/).

First you need to install tox into your local Python environment:

```sh
pip install tox
```

Then you can run the test suite for a specific environment with:

```sh
tox -e py311-django40
```

You can use this command to see all configured test environments:

```sh
tox -l
```

## Pylint linter

The [pylint](https://pylint.readthedocs.io/en/stable/) linter is also pre-configured. Pylint is a popular linter that checks your app for common bugs, unidiomatic python code and makes suggestions for refactoring.

You can run the linter manually with:

```sh
tox -e pylint
```

To enable the linter to run as part of your CI pipeline you must uncomment the respective lines in `.gitlab-ci.yml`.
