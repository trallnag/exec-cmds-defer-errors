# Maintain!

This document is targeted at project maintainers. It describes various
maintenance tasks and processes.

## Raise lowest supported Python version

Check here: <https://devguide.python.org/versions/>.

Consider raising the lowest supported Python version. Adjustments must be made
in the following files:

- [`pyproject.toml`](pyproject.toml)
- [`src/exec_cmds_defer_errors.py`](src/exec_cmds_defer_errors.py)

Afterwards, update the dependencies of the script.

## Bump dependency versions in `pyproject.toml`

Raise the lowest supported versions of the dependencies in the file
[`pyproject.toml`](pyproject.toml). The versions should be compatible with each
other.

One approach is to simply set the version in the config file to the ones
specified in the lock file.

## Update upstream Copier template

This project is based on the following
[Copier](https://copier.readthedocs.io/en/stable/) template:
<https://github.com/trallnag/copier-template-python-script>. Consider updating
things in the template repository as well.