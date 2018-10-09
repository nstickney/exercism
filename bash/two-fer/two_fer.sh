#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting due to errexit on line $LINENO. Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	printf 'One for %s, one for me.\n' "$1"
}

if (( "$#" >= 1 )); then
	main "$@"
else
	main "you"
fi
