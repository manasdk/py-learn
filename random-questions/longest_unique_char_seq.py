#! /usr/bin/env python

import argparse
import six


def longest_unique_char_seq(words):
    longest_sub_sequence = []
    current_sub_sequence = []
    r_idx = 0
    while (r_idx < len(words)):
        word = words[r_idx]
        if word in current_sub_sequence:
            word_idx = current_sub_sequence.index(word)
            current_sub_sequence = current_sub_sequence[word_idx + 1:]
        else:
            current_sub_sequence.append(word)
            r_idx += 1
        if len(current_sub_sequence) > len(longest_sub_sequence):
            longest_sub_sequence = list(current_sub_sequence)
    return longest_sub_sequence

def main(args_):
    longest_sequence = longest_unique_char_seq(args_.words)
    print 'words : %s\nsubs  : %s' % (args_.words, longest_sequence)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--words', nargs='+', type=str, required=True)
    args_ = parser.parse_args()
    main(args_)