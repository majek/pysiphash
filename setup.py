import os
import sys
import setuptools

# Some filesystems don't support hard links. Using the power of
# monkeypatching to fix the problem.
import os, shutil
os.link = shutil.copy

setuptools.setup(
    name = 'siphash',
    version = '0.0.1',
    description = 'siphash - python siphash implementation',
    author = 'Marek Majkowski',
    author_email = 'marek@popcount.org',
    url = 'http://github.com/majek/pysiphash#readme',
    packages = ['siphash'],
    platforms = ['any'],
    license = 'MIT',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.2",
                   ],
    zip_safe = True,
    )
