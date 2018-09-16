#!/bin/bash

PARENT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

. $PARENT/utils/utils.sh
. $PARENT/utils/check.sh $1

ssh $1 -t "cd `locate $1 $2`; bash -l"
