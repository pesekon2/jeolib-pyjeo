# pyJEO

## Description

pyJEO is a library for image processing for geospatial data implemented in
JRC Ispra.

## License

pyJEO is released under an
[EUPL](https://joinup.ec.europa.eu/collection/eupl) license (see
[LICENSE.txt](LICENSE.txt))

## Dependencies

* mialib
* jiplib
* numpy

## Install

From the directory of the repository, run:

```
sudo python setup.py install
```

To install without sudo right, you can install with the --user

```
python setup.py install --user
```

## Test the installation

From the directory of the repository, run:

```
python -W ignore -m unittest -v tests
```

To run tests only for one module:

```
python -W ignore -m unittest -v tests/test_classify.py
```

## Build documentation

Dependencies for the documentation build:

* python3-sphinx
* sphinx-rtd-theme
* sphinxcontrib-bibtex

Go to directory `doc` and run `make html`.

```
cd doc
make html
```

## Versions

### Getting the right version

`master` branch is the development branch of `pyJEO`. It contains the newest
features, but it can also contain some API changes against previous versions.
Therefore, it is recommended to use more stable releases: To get them, please
see our [tags](tags).

### Development

All development should be done in the development branch (`master`). If
a commit fixes also an issue present in some of the releases, it should be
cherry-picked to the corresponding branch. Later, a patch version will be
released from these cherry-picked fixes.

An example showing how to cherry-pick commit `commit_hash` into branch
`0.5.x` (to fix an issue in release `0.5.0`):

```
git checkout 0.5.x
git cherry-pick commit_hash
git push
git checkout master
```

## See the code coverage

```
python -W ignore -m coverage run --source=pyjeo -m unittest tests
python -m coverage report -m
```
