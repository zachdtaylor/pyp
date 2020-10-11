import subprocess
from unittest.mock import patch
from pyp.pyp import pip_freeze, sort_entries


@patch('subprocess.check_output')
def test_pip_freeze_search_patterns(mock_check_output):
    pip_freeze(['plain', 'with-hyphen', 'with_underscore', 'this-has_both'])
    mock_check_output.assert_called_once()
    mock_check_output.call_args[0][0] == "pip freeze | grep -i 'plain==\\|with[-_]hyphen==\\|with[-_]underscore==\\|this[-_]has[-_]both=='"

def test_package_name_sorting_handles_irregular_names():
    packages = ['Django-7.5', 'abc-33', 'rANndom_44', 'pip']
    expected_output = ['abc-33', 'django-7.5', 'pip', 'ranndom_44']
    sorted_packages = sort_entries(packages)
    ''.join(sorted_packages) == ''.join(expected_output)