#!/bin/bash

PARENT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

. $PARENT/utils/utils.sh
. $PARENT/utils/check.sh $1

diff() {
    git diff --name-only --diff-filter=AM HEAD
    git ls-files --others --exclude-standard
}

files=`diff | tr "\n" " "`
if [ -z "$files" ]
then
  echo " * [ERR] No files to poosh. Do you have untracked or modified files? Check using 'git status'."
else
  scp $files $1:`locate $1 $2`
fi
