from setuptools import setup, find_packages


setup(
    name='pyp-manager',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['pyp=pyp.pyp:main']
    },
    scripts=['./pyp-runner.py'],
    version='0.0.2',
    license='MIT',
    description='A pip wrapper that writes requirements.txt automatically',
    author='Zach Taylor',
    author_email='zachdtaylor.b@gmail.com',
    url='https://github.com/zachtylr21/pyp',
    download_url='https://github.com/zachtylr21/pyp/archive/v0.0.3.tar.gz',
    keywords=['pip', 'python', 'package', 'requirements', 'dependency'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
