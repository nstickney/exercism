#!/usr/bin/env bash
# https://google.github.io/styleguide/shell.xml

# This option will make the script exit when there is an error
set -o errexit
# This option will make the script exit when it tries to use an unset variable
set -o nounset

main() {
    rev=""
    for i in $(seq 0 "$((${#1}-1))"); do
        rev="${1:$i:1}$rev"
    done
    echo "$rev"
}

# Calls the main function passing all the arguments to it via '$@'
# The argument is in quotes to prevent whitespace issues
main "$@"
