#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR

answer_out() {
	printf '%s\n' "$1"
	exit "${2:-0}"
}

main() {
	local msg="${1,,}"
	msg="${msg//[^[:alnum:][:space:],\'\"]}"
	msg="${msg//[[:space:],]/ }"

	declare -A words
	for i in $msg; do
		shopt -s extglob
		local word="${i##*([\"\'])}"
		word="${word%%*([\"\'])}"
		shopt -u extglob
		local count="${words[$word]:-0}"
		words[$word]="$((++count))"
	done

	for i in "${!words[@]}"; do
		printf '%s: %s\n' "$i" "${words[$i]}"
	done
}

[ ! ${#@} -eq 1 ] && answer_out "Usage: word_count.sh <message>" 1
main "$@"
