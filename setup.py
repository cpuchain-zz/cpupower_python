from setuptools import setup, Extension

cpupower_module = Extension('cpupower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'cpupower',
       version = '1.0.1',
       author_email = 'minkcrypto@gmail.com',
       author = 'Min Khang Aung',
       url = 'https://github.com/cpuchain/cpupower_python',
       description = 'Bindings for CPUpower proof of work used by CPUchain',
       ext_modules = [cpupower_module])
