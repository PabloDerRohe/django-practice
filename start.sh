#!/usr/bin/env bash

if [ $VIRTUAL_ENVIROMENT ]
then
    deactivate
fi
    . venv/bin/activate
