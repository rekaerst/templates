#!/bin/bash
cd "$(dirname "$0")"/..
pylupdate5 main.py -ts eng-chs.ts
pylupdate5 main.py -ts eng-fr.ts

lrelease eng-fr.ts eng-chs.ts
