#!/bin/bash

PARENT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

. $PARENT/utils/utils.sh
. $PARENT/utils/check.sh $1

diff() {
    git diff --name-only --diff-filter=AM HEAD
    git ls-files --others --exclude-standard
}

scp `diff | tr "\n" " "` $1:`locate $1 $2`
