# from distutils.command.build import build
# from setuptools.command.install import install

import setuptools.command.install
import distutils.command.build

from distutils.core import setup, Extension
from glob import glob

class CustomBuild(distutils.command.build.build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)


class CustomInstall(setuptools.command.install.install):
    def run(self):
        self.run_command('build_ext')
        self.do_egg_install()

setup(name="pybgsched",
      version="0.1.5",
#      cmdclass={'build': CustomBuild,'install':CustomInstall},
      packages=[''],
#      package_dir={'': 'tools/pybgsched'},
      ext_modules=[Extension('_pybgsched', 
                    ['pybgsched.i'],
                    include_dirs=['/bgsys/drivers/ppcfloor/hlcs/include',
                                  '/bgsys/linux/ionfloor/usr/include',
                                  '/bgsys/drivers/ppcfloor/extlib/include'],
                    library_dirs=['/bgsys/linux/ionfloor/usr/lib64',
                                  '/bgsys/drivers/ppcfloor/hlcs/lib',
                                  '/bgsys/drivers/ppcfloor/extlib/lib'],
                    libraries=['bgsched'],
                    swig_opts=['-threads',
                               '-c++',
                               ],
                    extra_link_args=[ '-Wl,-rpath,/bgsys/drivers/ppcfloor/hlcs/lib',
                                      '-Wl,-rpath,/bgsys/drivers/ppcfloor/extlib/lib']
                               )],
      py_modules=['pybgsched']
      ) 
