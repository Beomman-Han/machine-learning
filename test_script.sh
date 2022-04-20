#!/bin/bash

## test for algorithm/algorithm_paradigm
for py in `ls algorithm/algorithm_paradigm/*/*.py`; do
    python $py
done

## test for algorithm/classic_problem
for py in `ls algorithm/classic_problem/*py`; do
    python $py
done

## test for data_structure
for py in `ls data_structure/*.py`; do
    python $py
done
