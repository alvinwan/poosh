. lib/utils.sh
. lib/check.sh $1
ssh $1 -t "cd `locate $1 $2`; bash -l"
