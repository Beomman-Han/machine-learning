#!/bin/bash

## run all python codes at machine_learning
for py in `ls machine_learning/*py`; do
    python ${py}
done
