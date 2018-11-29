#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

failout() {
	printf '%s\n' "$@" >&2
	exit 1
}

main() {
	local seq="$*"
	[[ "$seq" == *[^ACGTacgt]* ]] && failout "Invalid nucleotide detected."
	seq=${seq//A/U}              # Replace all As with Us
	seq=${seq//T/A}              # Replace all Ts with As
	seq=${seq//C/0}              # Replace all Cs with 0s
	seq=${seq//G/C}              # Replace all Gs with Cs
	printf '%s\n' "${seq//0/G}"  # Replace all 0s with Gs
}

main "$@"
