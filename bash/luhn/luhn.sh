#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR

answer_out() {
	printf '%s\n' "$1"
	exit "${2:-0}"
}

main() {
	# Clean all whitespace characters
	local number="${*//[[:space:]]/}"

	# Basic checks
	[[ ! $number =~ ^[[:digit:]]{2,}$ ]] && answer_out "false"

	# Number validity
	local sum=0
	local len="${#number}"
	for ((i=0; i<len; i++)); do
		local digit="${number:$i:1}"
		local place="$((len - i))"
		[ "$((place % 2))" -eq 0 ] && digit="$((digit * 2))"
		[ "$digit" -gt 9 ] && digit="$((digit - 9))"
		sum="$((sum + digit))"
	done
	[ $((sum % 10)) -eq 0 ] && answer_out "true"
	answer_out "false"
}

main "$*"
