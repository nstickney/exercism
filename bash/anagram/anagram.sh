#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR

is_anagram() {
	local anagram=0
	local word="${1^^}"
	local match="${2^^}"
	if [ "$word" != "$match" ] && [ "${#word}" == "${#match}" ]; then
		anagram=1
		for ((i=0; i<${#1}; i++)); do
			local wset="${word//[^${word:$i:1}]}"
			local mset="${match//[^${word:$i:1}]}"
			[ "${#wset}" != "${#mset}" ] && anagram=0 && break
		done
	fi
	printf '%s\n' "$anagram"
}

main() {
	IFS=" " read -ra words <<< "$2"
	local results=()
	for ((i=0; i<${#words[@]}; i++)); do
		[ "$(is_anagram "$1" "${words[$i]}")" == 1 ] && \
			results+=("${words[$i]}")
	done
	printf '%s\n' "${results[*]}"
}

main "$@"
