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
	local seq="$1"

	local A="${seq//[^a|A]}"
	local C="${seq//[^c|C]}"
	local G="${seq//[^g|G]}"
	local T="${seq//[^t|T]}"

	(( ${#seq} == ${#A} + ${#C} + ${#G} + ${#T} )) ||\
		failout "Invalid nucleotide in strand"

	printf 'A: %s\nC: %s\nG: %s\nT: %s\n' "${#A}" "${#C}" "${#G}" "${#T}"
}

print_usage() {
	printf '%s\n' "Usage: nucleotide_count.sh <sequence>"
	exit 1
}

# If called without exactly one argument, print usage message
if [ ! "$#" -eq 1 ]; then
	print_usage
fi
main "$@"
