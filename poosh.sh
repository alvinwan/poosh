scp `bash diff.sh | sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g'` $1:$path
