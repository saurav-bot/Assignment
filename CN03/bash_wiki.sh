#!/usr/bin/env bash


fname="default_log.txt"
curl=$(which curl)

while getopts ":f:" arg; do
    case $arg in
    	f) fname=$OPTARG;;
    esac
done


shift "$(($OPTIND -1))"

args=("$@")
n=$#
i=1
word=${args[0]}


while [[ $i < $n ]] ; do
	word="$word""_""${args[i]}"
	i=$(( i+1 ))
	
done
	
	
	
url="https://en.wikipedia.org/wiki/$word"

echo -ne "###########                                (33%)\r"
sleep 1
echo -ne "##########################                 (66%)\r"
status=$(curl -LI $url -o /dev/null -w "%{http_code}\n" -s)
echo -ne "###########################################(100%)\r"
echo -ne "\n"
echo $url


if [[ $status == 200 ]]
	then 
		echo $url >> $fname
		echo "History saved in $fname file"
else

	echo "Not found. Try Again."
fi
	
