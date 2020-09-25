import subprocess
from unittest.mock import patch
from pyp.pyp import pip_freeze


@patch('subprocess.check_output')
def test_pip_freeze_search_patterns(mock_check_output):
    pip_freeze(['plain', 'with-hyphen', 'with_underscore', 'this-has_both'])
    mock_check_output.assert_called_once()
    mock_check_output.call_args[0][0] == "pip freeze | grep -i 'plain==\\|with[-_]hyphen==\\|with[-_]underscore==\\|this[-_]has[-_]both=='"
