#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	num="$1"
	exp=${#num}
	sum=0
	for ((i=0; i<exp; i++)); do
		digit=${num:$i:1}
		sum=$((sum+digit**exp)) 
	done
	if [ "$sum" -eq "$num" ]; then
		printf '%s\n' "true"
	else
		printf '%s\n' "false"
		exit 1
	fi
}

main "$@"
