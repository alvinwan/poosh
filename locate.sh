export tpug_hash=`git rev-list HEAD | tail -2 | head -1`
ssh $1 "export path=\`find ${2:-~} -name ${tpug_hash:2}\`;cd \$(dirname \$path);cd ../../../;pwd"
