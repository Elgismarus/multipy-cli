#!/bin/sh

mkdir -p dist/doc
pydoc -w `find . -type f -regex ".*\.py" -not -name "__init__.py"`
mv *.html dist/doc/
