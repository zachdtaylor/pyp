import sys
import subprocess


def pip_install(package_names):
    p = subprocess.Popen(
        'pip install ' + ' '.join(package_names),
        shell=True
    )
    p.wait()


def pip_freeze(package_names):
    patterns = "'" + '==\|'.join(package_names) + "'"
    output = subprocess.check_output(
        'pip freeze | grep ' + patterns + '==',
        shell=True
    ).decode('ascii')
    return output


def write_requirements(packages):
    for pkg in packages.split('\n')[:-1]:  # Skip the '' at the end
        while True:
            try:
                with open('requirements.txt', 'r+') as f:
                    for line in f:
                        if pkg in line:
                            break
                    else:
                        f.write(pkg + '\n')
            except FileNotFoundError:
                open('requirements.txt', 'w').close()
            else:
                break


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
