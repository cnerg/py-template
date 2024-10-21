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
if __name__ == "__main__":
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
* The most common approach to multi-word variables is "snake case": variables
  are in lower case with words separated by underscore
* Clear variable and method names can reduce the need for comments
* Carefully determine whether temporary variables are helpful. If you only use
  it once, consider if that line of code can be combined with the place it is
  used.
* Avoid **Magic Numbers** - numerical constants without a clear purpose
    * provide numerical constants with a variable to describe their purpose
    * these can be physical constants (`AVOGADRO = 6.02e23`), unit conversions
      (`EV2MEV = 1e-6`), or vector indices (`z = 2`), among others
    * they are not generally needed for things like squaring a quantity or
      dividing by some integer that arises from algebra

### Data structure design
* Take advantage of python's rich data structures and related methods
* `dictionaries` are a preferred way to bind data together in a way that is
  clear, rather than parallel lists that are indexed in parallel
* `numpy` arrays are frequently better choices than python lists for numerical
  data
* when looping over iterables (e.g. lists, dictionaries, numpy arrays, etc), 
  avoid an indexing variable if possible
    * `zip()` may be useful for iterating through multiple iterables with parallel
      indexing
    * `enumerate()` allows you to autogenerate an indexing variable, but make sure you need that index
    * iterating over a `range()` is probably a last resort, try iterating directly over
      the iterable or using `zip`
* consider [list
  comprehensions](https://www.w3schools.com/python/python_lists_comprehension.asp)
  for simple operations

### Comments
* Include a docstring in every method
* Rely on clear variable and method names and add comments sparingly where the
  intent/approach is non-intuitive

### Modularity
* If you have cut & paste code in two different places, it probably should be a
  method/function (or in some cases a loop)
* Even very short methods can be valuable if the method name makes the code more
  readable
* Ideally, methods should be no longer than one screen worth of lines
* Practice **Separation of Concerns**:
    * a single method should have a single purpose that is clear from the name
    * avoid any combination of reading, using and writing data in the same
      method

## Checklist 

Before submitting a PR, ask yourself: "Have I...."
* [ ] modularized my code into methods that each have a clear and
  singular purpose?
* [ ] included a docstring for every method?
* [ ] replaced all magic numbers with variables?
* [ ] used method names (verbs) and variable names (nouns) that make the
  code clearly readable?
* [ ] removed instances of copy/paste code or nearly identical sections of code?
* [ ] made good data structure design choices?
