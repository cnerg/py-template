# py-template
This repository serves as a template for new python projects and a way to express best practices

## Best Practices - Coding Practices

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
* Do not merge your own PR; there should always be at least one review by a
  non-author, and a non-author should merge

### Packaging and installation
* Introduce a `pyproject.toml` file ASAP

## Best Practices - Style

### Code formatting
* Follow PEP8 style guide, ideally with a tools like
  [`black`](https://pypi.org/project/black/) to help enforce it, especially via
  a plugin to your editor

### Variable naming
* Generally, choose nouns for variables and verbs for methods
* Clear variable and method names can reduce the need for comments

### Comments
* Include a docstring in every method
* Rely on clear variable and method names and add comments sparingly where the
  intent/approach is non-intuitive

### Modularity
* If you have cut & paste code in two different places, it probably should be a
  method
* Even very short methods can be valuable if the method name makes the code more
  readable
* Ideally, methods should be no longer than one screen worth of lines
