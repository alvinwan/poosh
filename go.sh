ssh $1 -t "cd `bash locate.sh $1 ${2:-~}`; bash -l"
