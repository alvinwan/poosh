#!/bin/bash

locate() {
    local OBJECT=`git rev-list HEAD | tail -2 | head -1`
    OBJECT=${OBJECT:2}
    
    local PACK=`ls $(git rev-parse --show-toplevel)/.git/objects/pack | grep .idx`
    ssh $1 "export path=\`find ${2:-~} -name $OBJECT -o -name $PACK\`;cd \$(dirname \$path);cd ../../../;pwd"
}
