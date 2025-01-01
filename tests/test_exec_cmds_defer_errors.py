import subprocess


def run_with(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            "uv",
            "run",
            "src/exec_cmds_defer_errors.py",
            *args,
        ],
        capture_output=True,
        shell=False,
        check=False,
        text=True,
    )


def test_get_version() -> None:
    """
    Tests that the script returns a version.
    """

    result = run_with("--version")
    assert result.returncode == 0


def test_empty_cmd() -> None:
    """
    Tests that the script errors out when given an empty command.
    """

    result = run_with("echo lol", "")
    assert result.returncode != 0
    assert "All given commands must be non-empty strings." in result.stderr


def test_first_cmd_error() -> None:
    """
    Tests that subsequent commands are executed even if the first command fails.
    """

    result = run_with("exit 1", "echo lol")
    assert result.returncode != 0
    assert "1 out of 2 command(s) failed." in result.stdout
    assert "Executed command 1 failed with exit code 1" in result.stdout
    assert "Executed command 2 successfully" in result.stdout


def test_multiple_cmd_error() -> None:
    """
    Tests that the script correctly handles multiple commands failing.
    """

    result = run_with("exit 1", "exit 2")
    assert result.returncode != 0
    assert "2 out of 2 command(s) failed." in result.stdout
    assert "Executed command 1 failed with exit code 1" in result.stdout
    assert "Executed command 2 failed with exit code 2" in result.stdout


def test_multiple_cmd_no_error() -> None:
    """
    Tests that the script correctly handles multiple commands succeeding.
    """

    result = run_with("echo lol", "echo lol")
    assert result.returncode == 0
    assert "All 2 commands executed successfully." in result.stdout
    assert "Executed command 1 successfully" in result.stdout
    assert "Executed command 2 successfully" in result.stdout
