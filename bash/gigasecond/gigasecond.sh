#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	date -u -d "$* 1000000000 seconds" "+%a %b %-d %R:%S %Z %Y"
}

print_usage() {
	printf '%s\n' "Usage: gigasecond.sh <start date> [start time]"
	exit 1
}

# If called without one or two arguments, print usage message
if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
	print_usage
fi
main "$@"
