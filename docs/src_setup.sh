#!/bin/bash

cd /workspaces/Webapp4/src
pip install --upgrade pip setuptools wheel\
	    && pip install -e ".[dev]"
