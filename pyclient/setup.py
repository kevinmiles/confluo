#!/usr/bin/env python

from setuptools import setup
from setuptools import Command
import sys
import os

class DialogShell(Command):
    """ Run DiaLog shell
    """
    
    description = "Run interactive DiaLog shell"
    
    user_options = [('hostname', 'h', 'Server hostname'), 
                    ('port', 'p', 'Server port')]
    
    def initialize_options(self):
        self.hostname = "localhost"
        self.port = "9090"
        
    def finalize_options(self):
        if self.hostname is None:
            raise Exception("Parameter --port is missing")
        if self.port is None:
            raise Exception("Parameter --port is missing")
    
    def run(self):
        python_ex = sys.executable
        os.execv(python_ex, [ python_ex, "-i", "preamble.py"])

setup(name='dialog',
      version='0.1.0',
      description='Python Client for DiaLog',
      author='Anurag Khandelwal',
      author_email='anuragk@berkley.edu',
      url='https://www.github.com/ucbrise/dialog',
      package_dir={'dialog': 'dialog'},
      packages=['dialog'],
      setup_requires=['pytest-runner', 'thrift>=0.10.0'],
      tests_require=['pytest-cov', 'pytest', 'thrift>=0.10.0', ],
      install_requires=['thrift>=0.10.0', ],
      cmdclass={'shell' : DialogShell,}
      )
