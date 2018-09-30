#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	local score=0
	for (( i=0; i<${#1}; i++ )); do
		case "${1:$i:1}" in
			[AaEeIiOoUuLlNnRrSsTt]) ((score+=1));;
			[FfHhVvWwYy])           ((score+=4));;
			[BbCcMmPp])             ((score+=3));;
			[DdGg])                 ((score+=2));;
			[JjXx])                 ((score+=8));;
			[QqZz])                 ((score+=10));;
			[Kk])                   ((score+=5));;
		esac
	done
	echo $score
}

main "$@"
