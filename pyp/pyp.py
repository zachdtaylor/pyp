import sys
import subprocess
import re
from collections import OrderedDict

REQUIREMENTS_FILE_NAME = 'requirements.txt'

def pip_install(package_names):
    p = subprocess.Popen(
        'pip install ' + ' '.join(package_names),
        shell=True
    )
    p.wait()

def sort_entries(entries):
    lowercase_list = [entry.lower() for entry in entries]
    return sorted(lowercase_list)

def pip_freeze(package_names):
    patterns = "'" + '==\|'.join(package_names) + "=='"
    patterns = re.sub(r'[-_]', '[-_]', patterns)
    output = subprocess.check_output(
        'pip freeze | grep -i ' + patterns,
        shell=True
    ).decode('ascii')
    return output

def get_existing_entries():
    entries = []
    try:
        with open(REQUIREMENTS_FILE_NAME, 'r') as file:
            entries = [entry.rstrip('\n') for entry in file]
    except FileNotFoundError:
        open(REQUIREMENTS_FILE_NAME, 'w').close()
    
    return entries

def write_requirements(packages):
    existing_entries = get_existing_entries()
    new_entries = packages.split('\n')[:-1] # Skip the '' at the end
    combined_entries = list(OrderedDict.fromkeys (existing_entries + new_entries))
    sorted_entries = sort_entries(combined_entries)

    file_contents = '\n'.join(sorted_entries) + '\n' # For the last entry
    with open(REQUIREMENTS_FILE_NAME, 'w') as file:
        file.write(file_contents)

def main():
    if sys.argv[1] == 'install':
        package_names = sys.argv[2:]
        pip_install(package_names)
        installed_packages = pip_freeze(package_names)
        write_requirements(installed_packages)
    else:
        print(
            """
            pyp currently only supports install.
            If you want to contribute, visit https://github.com/zachtylr21/pyp
            """
        )
