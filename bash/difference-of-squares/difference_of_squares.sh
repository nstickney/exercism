#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

square_of_sum() {
	local total=0
	local i=0
	while (( "$i" < "$1" )); do
		((i+=1))
		((total+="$i"))
	done
	echo $((total**2))
}

sum_of_squares() {
	local total=0
	local i=0
	while (( "$i" < "$1" )); do
		((i+=1))
		((total+="$i"**2))
	done
	echo $total
}

difference() {
	local sq
	sq=$(square_of_sum "$1")
	local sm
	sm=$(sum_of_squares "$1")
	echo $((sq-sm))
}

main() {
	local num=${2#-}
	case $1 in
		"square_of_sum")  square_of_sum "$num";; 
		"sum_of_squares") sum_of_squares "$num";;
		"difference")     difference "$num";;
	esac
}

main "$@"
