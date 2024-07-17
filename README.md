# py-template
This repository serves as a template for new python projects and a way to express best practices

## Best Practices

### User input
* Always use [`argparse`](https://docs.python.org/3/library/argparse.html) for command-line arguments
* Assume the use of [`yaml`](https://python.land/data-processing/python-yaml) for structured input files unless there are compelling reasons for something else

### User output
* Always use `logger` for status output
* Carefully choose an output format for standard formats, considering the following in order of priority:
    * [CSV](https://docs.python.org/3/library/csv.html) with direct support in NumPy, Pandas, etc
    * [yaml](https://python.land/data-processing/python-yaml)
    * [json](https://docs.python.org/3/library/json.html)
    * [HDF5](https://www.h5py.org/)
    * SQL, for example [SQLite](https://docs.python.org/3/library/sqlite3.html)

### Modularity
* All runnable scripts [should include a block like](https://stackoverflow.com/questions/419163/what-does-if-name-main-do):

``` python
if __name__ == __main__():
    do_main_task()
```

### Testing
* Always use [`pytest`](https://docs.pytest.org/en/8.2.x/) for testing
* Introduce a simple continuous integration (CI) action ASAP

### Collaboration
* Generate pull requests (PRs) with as little code change as possible
* Include tests in all PRs

### Packaging and installation
* Introduce a `pyproject.toml` file ASAP
