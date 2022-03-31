from setuptools import setup

setup(
    name='cool_lib_x',
    version='0.0.1',
    description='Demo lib_x library',
    py_modules=['lib_x'],
    package_dir={'': 'src'},
    install_requires = ["requests==2.7.0"],
)

