#!/usr/bin/env python

from distutils.core import setup, Extension
from glob import glob

setup(name="Subblock-Cobalt",
      version="0.99.7-sb",
      description="Cobalt Resource Manager for Sublocks",
      author="Cobalt Team",
      author_email="cobalt@mcs.anl.gov",
      packages=["Cobalt", "Cobalt.Components", "Cobalt.DataTypes", "Cobalt.Components.DBWriter"],
      package_dir = {'Cobalt': 'src/lib'},
      scripts = glob('src/clients/*.py') + glob('src/clients/POSIX/*.py') \
      + glob('src/components/*.py') + glob('tools/subblock/*.sh') + glob('tools/subblock/*.py'),
      data_files=[('share/man/man1', glob('man/*.1')),
                  ('share/man/man1', glob('man/POSIX/*.1')),
                  ('share/man/man5', glob('man/*.5')),
                  ('share/man/man8', glob('man/*.8')),
                  ('share/cobalt/etc', glob('tools/subblock/*.conf.tmpl'))]
            )


