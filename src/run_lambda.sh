#!/bin/bash
echo "[*]running lambda from Pycharm"
export SECRET_SAUCE="chocolate"
python-lambda-local -f "$1" "$2" "$3"