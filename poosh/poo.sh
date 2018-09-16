#!/bin/bash

. utils/utils.sh
. utils/check.sh $1

diff() {
    git diff --name-only --diff-filter=AM HEAD
    git ls-files --others --exclude-standard
}

scp `diff | tr "\n" " "` $1:`locate $1 $2`
