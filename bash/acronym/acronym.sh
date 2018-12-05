#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local acronym=''
	for ((i=0; i<${#1}; i++)); do
		local letter="${1:$i:1}"
		if [[ "$letter" == [a-z] ]]; then
			if ((i == 0)) || [[ ! "${1:$i-1:1}" == [a-z] ]]; then
				acronym+="${letter^}"
			fi
		fi
	done
	printf '%s\n' "$acronym"
}

main "$@"
