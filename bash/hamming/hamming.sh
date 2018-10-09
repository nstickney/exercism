#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {

	local seq1="$1"
	local seq2="$2"

	# Check strands have equal length
	if [ ! ${#seq1} = ${#seq2} ]; then
		printf '%s\n' "left and right strands must be of equal length" >&2
		exit 1
	fi

	# Find distance
	local distance=0
	for (( i=0; i<${#1}; i++ )); do
		[ ! "${seq1:i:1}" = "${seq2:i:1}" ] && (( distance += 1 ))
	done

	printf '%s\n' $distance
}

print_usage() {
	printf '%s\n' "Usage: hamming.sh <strand1> <strand2>"
	exit 1
}

# If called without exactly two arguments, print usage message
[ "$#" != 2 ] && print_usage
main "$@"
