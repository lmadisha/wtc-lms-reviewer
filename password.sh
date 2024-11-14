#!/bin/bash
# send commands
wtc-lms login
# shellcheck disable=SC2188
<<< Madisha2004
echo "Please enter your password!"
# shellcheck disable=SC2188
read -s PASSWORD
# shellcheck disable=SC2188
<<< PASSWORD
# Enters the password
# shellcheck disable=SC2162
read -s PASSWORD
# echos the password you entered.
echo "Your entered: $PASSWORD"