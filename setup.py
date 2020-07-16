from setuptools import setup


setup(
  name = 'pyp',
  packages = ['pyp'],
  entry_points = {
    "console_scripts": ['pyp=pyp.pyp:main']
  },
  scripts=['./pyp-runner.py'],
  version = '0.1',
  license='MIT',
  description = 'A pip wrapper that writes requirements.txt automatically',
  author = 'Zach Taylor',
  author_email = 'zachdtaylor.b@gmail.com',
  url = 'https://github.com/zachtylr21/pyp',
  download_url = 'https://github.com/zachtylr21/pyp/archive/v0.0.1.tar.gz',    # I explain this later on
  keywords = ['pip', 'python', 'package', 'requirements', 'dependency'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)