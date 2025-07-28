#!/bin/bash

# This is arguably the paradigmatic minimal bash completion.
_emoji() {
    local emojis=($(emoji --list))
    local cur_word="${COMP_WORDS[COMP_CWORD]}"
    local prev_word="${COMP_WORDS[COMP_CWORD - 1]}"
    COMPREPLY=( $(compgen -W "${emojis[*]}" -- ${cur_word}) )
}
complete -F _emoji emoji
