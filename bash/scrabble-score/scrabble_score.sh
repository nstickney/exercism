#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	word=$1

	local ones=AaEeIiOoUuLlNnRrSsTt
	local twos=DdGg
	local threes=BbCcMmPp
	local fours=FfHhVvWwYy
	local fives=Kk
	local eights=JjXx
	local tens=QqZz

	local score=0
	for (( i=0; i<${#word}; i++ )); do
		if [[ $ones = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 1 ))
		elif [[ $twos = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 2 ))
		elif [[ $threes = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 3))
		elif [[ $fours = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 4 ))
		elif [[ $fives = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 5 ))
		elif [[ $eights = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 8 ))
		elif [[ $tens = *"${word:$i:1}"* ]]; then
			score=$(( "$score" + 10 ))
		fi
	done
	echo $score
}

main "$@"
