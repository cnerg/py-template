# py-template
This repository serves as a template for new python projects and a way to express best practices

## Best Practices

### User input
* Always use `argparse` for command-line arguments
* Assume the use of `yaml` for structured input files unless there are compelling reasons for something else

### User output
* Always use `logger` for status output
* Carefully choose an output format for standard formats, considering the following in order of priority:
    * CSV
    * yaml
    * json
    * HDF5
    * SQL

### Modularity
* All runnable scripts should include a block like:

``` python
if __name__ == __main__():
    do_main_task()
```

### Testing
* Always use `pytest` for testing
* Introduce a simple continuous integration (CI) action ASAP

### Collaboration
* Generate pull requests (PRs) with as little code change as possible
* Include tests in all PRs

### Packaging and installation
* Introduce a `pyproject.toml` file ASAP
