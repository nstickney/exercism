#!/usr/bin/env bash

# Bash strict mode (https://github.com/alphabetum/bash-boilerplate)
set -eEuo pipefail
trap 'echo "Aborting (errexit line $LINENO). Exit code: $?" >&2' ERR
IFS=$'\n\t'

main() {
	printf 'Hello, %s\n' "${@:-you}"
}

print_usage() {
	printf 'Usage: ./error_handling <greetee>'
	exit 1
}

if (( "${#@}" != 1 )); then
	print_usage
fi
main "$@"
