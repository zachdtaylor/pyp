#!/usr/bin/env python

import sys
import subprocess

if __name__ == '__main__':
  package_names = sys.argv[2:]
  p = subprocess.Popen(
    'pip install ' + ' '.join(package_names),
    shell=True
  )
  p.wait()
  patterns = "'" + '==\|'.join(package_names) + "'"
  output = subprocess.check_output(
    'pip freeze | grep ' + patterns + '==',
    shell=True
  )
  with open('requirements.txt', 'ab') as f:
    f.write(output)