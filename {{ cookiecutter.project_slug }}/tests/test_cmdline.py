"""Test cmdline"""
{%- if cookiecutter.use_src_layout|int < 3.9 %}
from __future__ import annotations  # PEP 585
{%- endif %}

import pytest
from click.testing import CliRunner

from {{cookiecutter.project_slug}} import __version__
from {{cookiecutter.project_slug}}.cmdline import main


@pytest.mark.parametrize(
    ['invoke_args', 'exit_code', 'output_keyword'],
    [
        ([], 0, 'help'),
        (['--help'], 0, 'help'),
        (['--version'], 0, __version__),
        (['-V'], 0, __version__),
        (['--debug', '--verbose', 'run'], 0, 'run'),
    ]
)
def test_main(
        clicker: CliRunner,
        invoke_args: list[str],
        exit_code: int,
        output_keyword: str,
):
    """Test main cmdline"""
    result = clicker.invoke(main, invoke_args)
    assert result.exit_code == exit_code
    assert output_keyword in result.output
