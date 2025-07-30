#!/usr/bin/env bash

# Bash completion function for the 'howto' command
_howto_completions() {
  local cur_word howto_files
  cur_word="${COMP_WORDS[COMP_CWORD]}"

  # Find all files and directories recursively in the howto folder
  howto_files=$(find -L "$HOWTO/" -type f -o -type d | sed "s|$HOWTO/||")

  # Provide completion options based on current input
  COMPREPLY=($(compgen -W "$howto_files" -- "$cur_word"))
}

complete -F _howto_completions howto

