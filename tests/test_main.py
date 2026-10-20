from tvsummary.main import main


def test_main_missing_config(capsys) -> None:
    exit_code = main(["--config", "missing.toml"])

    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Error:" in captured.err
    assert "Could not read settings file" in captured.err
    assert "Traceback" not in captured.err
