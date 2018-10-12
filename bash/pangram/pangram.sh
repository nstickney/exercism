#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	shopt -s nocasematch
	local alphabet="abcdefghijklmnopqrstuvwxyz"

	for (( i=0; i<${#alphabet}; i++ )); do
		[[ "$1" != *"${alphabet:i:1}"* ]] && break;
	done

	if (( "$i" == 26 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

print_usage() {
	printf '%s\n' "Usage: pangram.sh <string>"
	exit 1
}

# If called without exactly one arguments, print usage message
[ "$#" != 1 ] && print_usage
main "$@"
