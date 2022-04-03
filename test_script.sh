#!/bin/bash

## test codes in algorithm_paradigm/
for py in `ls algorithm/algorithm_paradigm/*/*.py`; do
    python $py
done

## test codes in data_structure/
for py in `ls data_structure/*.py`; do
    python $py
done
