#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

degenerate() {
	if (( "$(bc <<< "$2 == $3 + $4 || $3 == $2 + $4 || $4 == $2 + $3")" == 1 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

equilateral() {
	if (( "$(bc <<< "$2 == $3 && $3 == $4")" == 1 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

isosceles() {
	if (( "$(bc <<< "$2 == $3 || $3 == $4 || $4 == $2")" == 1 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

scalene() {
	if [ "$(isosceles "$@")" == "false" ]; then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

main() {

	if (( "$(bc <<< "$2 == 0 || $3 == 0 || $4 == 0")" == 1 )) || \
		(( "$(bc <<< "$2 > $3 + $4 || $3 > $2 + $4 || $4 > $2 + $3")" == 1 )); then
		printf '%s\n' "false"
		exit 0
	fi

	case "$1" in
		"degenerate")  degenerate "$@";;
		"equilateral") equilateral "$@";;
		"isosceles")    isosceles "$@";;
		"scalene")     scalene "$@";;
	esac
}

print_usage() {
	printf '%s\n' "Usage: triangle.sh <type> side1> <side2> <side3>"
	printf '%s\n' "    type: one of degenerate, equilateral, isosceles, or scalene"
	exit 1
}

# If called without exactly four arguments, print usage message
if [ "$#" != 4 ]; then
	print_usage
fi
main "$@"
