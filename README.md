# `exec_cmds_defer_errors.py`

Small Python script that executes given commands commands and defers errors.

The standalone script is called `exec_cmds_defer_errors.py` and can be found
[here](src/exec_cmds_defer_errors.py). The license is included in the file.

Here is how it can be used:

```sh
python exec_cmds_defer_errors.py \
  'whoami | grep goatse' \
  'echo "hello world"' \
  'make love'
```

The output will look like this:

![screenshot.png](assets/screenshot.png)

## Versioning

The project follows [Semantic Versioning](https://semver.org/).

## Contributing

Contributions are welcome. Please refer to [`CONTRIBUTE.md`](CONTRIBUTE.md).

## Licensing

This work is licensed under the
[ISC license](https://en.wikipedia.org/wiki/ISC_license). See
[`LICENSE`](LICENSE) for the license text.

The license is also included in the script
[`src/exec_cmds_defer_errors.py`](src/exec_cmds_defer_errors.py) itself.

## Template

This project is based on the following
[Copier](https://copier.readthedocs.io/en/stable/) template:
<https://github.com/trallnag/copier-template-python-script>.
