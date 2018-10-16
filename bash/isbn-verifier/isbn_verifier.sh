#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local isbn="${1//[!0-9X]/}"

	if [ ! "${#isbn}" == 10 ]; then
		printf '%s\n' "false"
		exit 0
	fi

	local score=0
	for (( i=0; i<"${#isbn}"; i++ )); do
		if [ "${isbn:i:1}" == "X" ]; then
			if (( "$i" != 9 )); then
				printf '%s\n' "false"
				exit 0
			else
				(( score += 10 ))
			fi
		else
			(( score += (10 - i) * ${isbn:i:1} ))
		fi
	done

	if (( score % 11 == 0 )); then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
	fi
}

print_usage() {
	printf '%s\n' "Usage: isbn_verifier.sh <isbn>"
	exit 1
}

# If called without exactly one argument, print usage message
if [ ! "$#" -eq 1 ]; then
	print_usage
fi
main "$@"
