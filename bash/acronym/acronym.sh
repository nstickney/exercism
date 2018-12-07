#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local acronym=''
	for ((i=0; i<${#1}; i++)); do
		local letter="${1:$i:1}"
		[[ "$letter" == [a-z] ]] && \
			[[ "$i" == "0" || "${1:$i-1:1}" != [a-z] ]] && \
			acronym+="${letter^}"
	done
	printf '%s\n' "$acronym"
}

main "$@"
