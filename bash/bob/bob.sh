#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

reply() {
	printf '%s\n' "$@"
	exit 0
}

main() {
	local input="$*"
	input="${input#"${input%%[![:space:]]*}"}"   # Trim leading whitespace
	input="${input%"${input##*[![:space:]]}"}"   # Trim trailing whitespace
	[ "$input" == "" ] && reply "Fine. Be that way!"
	if [[ ! "$input" =~ [a-z] ]] && [[ "$input" =~ [A-Z] ]]; then
		[ "${input: -1}" == "?" ] && reply "Calm down, I know what I'm doing!"
		reply "Whoa, chill out!"
	fi
	[ "${input: -1}" == "?" ] && reply "Sure."
	reply "Whatever."
}

main "$@"
