#!/bin/bash

cd /workspaces/Webapp33/src
uv pip install --upgrade pip setuptools wheel\
	    && uv pip install -e ".[dev]"
