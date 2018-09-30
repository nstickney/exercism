#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local factors=(
		["3"]="Pling"
		["5"]="Plang"
		["7"]="Plong"
	)
	local rain=""
	for i in "${!factors[@]}"; do
		(( "$1" % i == 0 )) && rain+="${factors[i]}"
	done
	echo "${rain:-$1}"
}

main "$@"
