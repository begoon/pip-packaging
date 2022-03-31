# pip package

An example how to build your own simple package, which can be installed by pip.

## Useful videos about pip packages creation

https://www.youtube.com/watch?v=GIF3LaRqgXo
https://www.youtube.com/watch?v=4fzAMdLKC5k

## Prerequisites

    pip install wheel

## Build a wheel

    python setup.py bdist_wheel

### Test install the local package to a test location

#### 100% local, `pypi.org` is disabled

    pip install --no-index --find-links ./dist --target packages cool_lib_x

#### Using `pypi.org` for dependencies

    pip install --find-links ./dist --target packages cool_lib_x

## Test locally from the test location

    PYTHONPATH=packages python

    import lib_x
    lib_x.func_x(1)

## Build a source packages

    python setup.py sdist
