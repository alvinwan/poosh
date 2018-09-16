#!/bin/bash

if [ $# -lt 1 ]; then
  echo 1>&2 "$0: Need server name."
  exit 2
fi
