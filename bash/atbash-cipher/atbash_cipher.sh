#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR

answer_out() {
	printf '%s\n' "$1"
	exit "${2:-0}"
}

main() {
	local msg="${2//[![:alnum:]]/}"
	msg="${msg,,}"

	# Encode
	local alphabet='abcdefghijklmnopqrstuvwxyz'
	local result=""
	for ((i=0; i<${#msg}; i++)); do
		local char="${msg:i:1}"

		# Only encode if the character is a letter
		if [[ "$char" =~ ^[[:alpha:]]$ ]]; then

			# Find the position of $char in the alphabet and negate it
			local pos="${alphabet%%$char*}"
			local num="-${#pos}"
			char="${alphabet: ((num - 1)):1}"
		fi

		if [ "$1" == "encode" ] && ((i > 0)) && ((i % 5 == 0)); then
			result="$result $char"
		else
			result="$result$char"
		fi
	done

	answer_out "$result"
}

if ((${#@} != 2)); then
	answer_out "Usage: atbash_cipher.sh <encode|decode> <message>" 1
fi
main "$@"
