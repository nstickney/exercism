#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'


main() {
	shopt -s nocasematch

	for i in {a..z}; do
		[[ "$1" != *"$i"* ]] && printf '%s\n' "false" && exit
	done

	printf '%s\n' "true"
}

print_usage() {
	printf '%s\n' "Usage: pangram.sh <string>"
	exit 1
}

# If called without exactly one arguments, print usage message
[ "$#" != 1 ] && print_usage
main "$@"
