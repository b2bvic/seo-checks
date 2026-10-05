from unittest.mock import Mock


def test_loop_stops_without_extra_request(tool, monkeypatch):
    responses = [Mock(status_code=302, is_redirect=True, headers={"Location": "/b"}), Mock(status_code=302, is_redirect=True, headers={"Location": "/a"})]
    head = Mock(side_effect=responses)
    monkeypatch.setattr(tool.requests, "head", head)
    chain = tool.trace("https://example.com/a")
    assert chain[-1]["status"] == "LOOP"
    assert head.call_count == 2


def test_path_relative_redirect(tool, monkeypatch):
    responses = iter([Mock(status_code=302, is_redirect=True, headers={"Location": "../end?x=1"}), Mock(status_code=200, is_redirect=False, headers={})])
    monkeypatch.setattr(tool.requests, "head", lambda *args, **kwargs: next(responses))
    chain = tool.trace("https://example.com/path/start")
    assert chain[-1]["url"] == "https://example.com/end?x=1"


def test_cli_help(tool):
    from click.testing import CliRunner
    result = CliRunner().invoke(tool.main, ["--help"])
    assert result.exit_code == 0, result.output
    assert "Usage:" in result.output
