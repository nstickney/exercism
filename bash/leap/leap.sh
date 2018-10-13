#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	if (( "$1" % 4 == 0 )) && (( "$1" % 100 != 0 )) || (( "$1" % 400 == 0 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

print_usage() {
	printf '%s\n' "Usage: leap.sh <year>"
	exit 1
}

# If called without exactly one digits-only arguments, print usage message
if [ "$#" != 1 ] || [[ ! "$1" =~ ^[0-9]+$ ]]; then
	print_usage
fi
main "$@"
