#!/usr/bin/env bash
# https://google.github.io/styleguide/shell.xml

# This option will make the script exit when there is an error
set -o errexit
# This option will make the script exit when it tries to use an unset variable
set -o nounset

main() {

    if [[ "$1" == "total" ]]; then
        total=0
        for i in {1..64}; do
            total=$(echo "$total"+2^\("$i"-1\) | bc)
        done
        echo "$total"
        exit
    fi

    if (($1 < 1)); then
        echo "Error: invalid input" 1>&2
        exit 1
    elif (($1 > 64)); then
        echo "Error: invalid input" 1>&2
        exit 1
    fi
    
    echo 2^\("$1"-1\) | bc

}

# Calls the main function passing all the arguments to it via '$@'
# The argument is in quotes to prevent whitespace issues
main "$@"
