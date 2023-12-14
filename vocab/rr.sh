#!/bin/bash

# Specify the file
file="vi_vocab_cleaned.txt"

# Use sed to delete empty lines and lines with whitespace characters
sed '/^\s*$/d' "$file" > o.txt