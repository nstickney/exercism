#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR

error_out() {
	printf '%s\n' "$1" >&2
	exit "$2"
}

main() {
	# Clean all non-digit characters
	local number="${1//[^0-9]}"

	# Check format
	if [[ "$number" =~ ^1{0,1}[2-9][0-9]{2}[2-9][0-9]{6}$ ]]; then
		printf '%s\n' "${number: -10}"
	else
		error_out "Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9" 1
	fi
}

main "$@"
