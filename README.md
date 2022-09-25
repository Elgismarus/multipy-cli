# MultiPy-CLI

[![Maintainability](https://api.codeclimate.com/v1/badges/3620c76c9da2ee34656d/maintainability)](https://codeclimate.com/github/Elgismarus/multipy-cli/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/3620c76c9da2ee34656d/test_coverage)](https://codeclimate.com/github/Elgismarus/multipy-cli/test_coverage)

Small example of a CLI application searching for multiple of 3 and 5 in a list of integer.

# Compatibility

| Name | Version |
| --- | --- |
| Pyton | 3.10.4 |

# Contribute easily with VSCode
This project has been built with VSCode in a devcontainer. This allows for development environment consistency across engineers and eases onboarding and setup. This avoids frustration when the environment version changes and the required programming languages and/or dependencies must be installed on the local machine.

1. Open Terminal
1. Clone project
1. `cd` into project root directory
1. Type `code .` (this will open VSCode in current directory)
1. In VSCode, `ctrl+shift+P` and select `Remote container: Rebuild Container`

It usually takes some time the first time to build (download images/container). Once built, you will have all the VSCode plugins required and be able to work on the project. The test explorer is a good tool for debugging and running specific tests visually.

# Testing
_Note: The command below assumed that you are running in the VSCode environment_

Run tests suite through command line:
```
python3 -m unittest discover -s ./tests -p '*_test.py'
```

Run coverage:
```
coverage -m unittest discover -s ./tests -p '*_test.py'
# Report via command line
coverage report -m
# HTML format for visual
coverage html
```

# Documentation
Documentation can be generated via the following bash script:

```
bin/generate_doc.sh
```

The HTML document file will be generated in a new directory `dist/doc`.

# Sample

Run the sample demo for searching number multiple of 3 and 5 for numbers between 1 to 100. If the number is a multiple of 3, 5 or both, it will convert the number into text. If both, it will combine both multiple (e.g. ThreeFive).

```
python3 src/multipy/sample.py
```

Alternatively, you can see the result in the latest `sample` build in Github Actions.
