# Release!

This document describes the release process and is targeted at maintainers.

## Preparation

Check the existing tags:

```sh
git tag --list --sort=taggerdate 'v*' | tail --lines=5
```

Pick a name for the new release. It must follow
[Semantic Versioning](https://semver.org):

```sh
VERSION=1.0.1
```

Bump the version constants in [`pyproject.toml`](./pyproject.toml) and
[`src/exec_cmds_defer_errors/exec_cmds_defer_errors.py`](./src/exec_cmds_defer_errors/exec_cmds_defer_errors.py):

```sh
sed --in-place "s/^version = \".*\"/version = \"$VERSION\"/" \
  pyproject.toml
sed --in-place "s/^VERSION = \".*\"/VERSION = \"$VERSION\"/" \
  src/exec_cmds_defer_errors/exec_cmds_defer_errors.py
uv sync
```

Make sure that [`CHANGELOG.md`](./CHANGELOG.md) is up-to-date.

Adjust entries in the changelog for example by adding additional examples or
highlighting breaking changes.

Move the content of the "Unreleased" section that will be included in the new
release to a new section with an appropriate title for the release. Should the
"Unreleased" section now be empty, add "Nothing." to it.

## Trigger

Commit the changes. Make sure to sign the commit:

```sh
git add .
git commit --gpg-sign --message="chore: Prepare release v$VERSION"
git log --show-signature --max-count=1
```

Push changes:

```sh
git push origin master
```

Check
[workflow runs](https://github.com/trallnag/exec-cmds-defer-errors/actions?query=branch%3Amaster)
in GitHub Actions and ensure everything is fine.

Tag the latest commit with an annotated and signed tag:

```sh
git tag --sign --message="" v$VERSION
git show v$VERSION
```

Make sure that the tree looks good:

```sh
git log --graph --oneline --all --max-count=5
```

Push the tag itself:

```sh
git push origin v$VERSION
```

This triggers the release workflow which will build package distributions,
publish them to PyPI, and draft a GitHub release. Monitor the
[release workflow](https://github.com/trallnag/exec-cmds-defer-errors/actions/workflows/release.yaml)
run and check the
[project on PyPI](https://pypi.org/project/exec-cmds-defer-errors/).

## Wrap up

If everything is fine, go to the release page of this project on GitHub
[here](https://github.com/trallnag/exec-cmds-defer-errors/releases) and review
the automatically created release draft.

Publish the draft.

## Miscellaneous

### Handling of pre-releases

To publish a version for testing purposes pick a version with the suffix `.devN` where the `N` is an incrementing number starting at 1. Format the changelog entry accordingly. In PyPI, the package version will show up as a pre-release automatically. The release in GitHub must be marked as a pre-release before publishing. Skip the GitHub release entirely depending on the target group of the dev release.
