#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local FACTORS=("3" "5" "7")
	local WORDS=("Pling" "Plang" "Plong")
	local rain=""
	local i=0
	local length=${#FACTORS[@]}
	while ((i < length)); do
		(( "$1" % FACTORS[i] == 0 )) && rain+="${WORDS[i]}"
		((i+=1))
	done
	[ "$rain" = "" ] && rain="$1"
	echo "$rain"
}

main "$@"
