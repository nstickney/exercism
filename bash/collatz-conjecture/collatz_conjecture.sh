#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local n="$1"
	if (( n < 1 )); then
		echo "Error: Only positive numbers are allowed" 
		exit 1
	fi
	local steps=0
	while (( n != 1 )); do
		if (( n % 2 == 0 )); then
			(( n /= 2 ))
		else
			(( n = 3*n+1 ))
		fi
		(( steps += 1 ))
	done
	echo "$steps"
}

main "$@"
