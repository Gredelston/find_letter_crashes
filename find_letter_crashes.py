import argparse
import itertools
import os
import re
import sys


def main(file1, file2,
    ignore_spaces=False, ignore_punctuation=False,
    single_crashes_only=False):
    # Parse the two files
    phrases_by_length1 = extract_phrases_by_length(
        file1, ignore_spaces, ignore_punctuation)
    phrases_by_length2 = extract_phrases_by_length(
        file2, ignore_spaces, ignore_punctuation)

    # Find and print all crashing pairs
    shared_word_lengths = intersection(
        phrases_by_length1.keys(), phrases_by_length2.keys())
    for word_lengths in shared_word_lengths:
        phrases1 = phrases_by_length1[word_lengths]
        phrases2 = phrases_by_length2[word_lengths]
        crashing_pairs = find_crashing_pairs(
            phrases1, phrases2, single_crashes_only)
        if crashing_pairs:
            print()
            for pair in crashing_pairs:
                print(pair)


def extract_phrases_by_length(path_to_file, ignore_spaces, ignore_punctuation):
    phrases_by_length = {}
    assert os.path.isfile(path_to_file), "Invalid file: " + path_to_file
    with open(path_to_file) as f:
        lines = f.readlines()
    for line in lines:
        phrase = normalize_string(line, ignore_spaces, ignore_punctuation)
        if not phrase:
            continue
        word_lengths = tuple([len(word) for word in phrase.split()])
        append_element_to_dict_value(phrases_by_length, word_lengths, phrase)
    return phrases_by_length


def append_element_to_dict_value(d, key, elem):
    """Adds a new element to an iterable dict value, possibly autovivifying."""
    value = d.get(key, [])
    value.append(elem)
    d[key] = value
        

def normalize_string(string, ignore_spaces, ignore_punctuation):
    """Normalizes strings to prepare them for crashing comparison."""
    string = string.upper()
    if ignore_punctuation:
        string = re.sub(r"[^1-9a-z \n\r\t]", "", string, flags=re.I)
    if ignore_spaces:
        string = re.sub(r"\w+", "", string)
    else:
        string = string.strip()
        string = re.sub(r"[ \n\r\t]+", " ", string)
    return string


def intersection(l1, l2):
    """Find all elements that are in both list 1 and list 2."""
    return set(l1) & set(l2)


def find_crashing_pairs(l1, l2, single_crashes_only):
    """Finds all pairs of strings which crash at a single character."""
    crashing_pairs = []
    all_pairs = itertools.product(l1, l2)
    # Iterate through all pairs of strings
    for (str1, str2) in all_pairs:
        if len(str1) != len(str2) or str1 == str2:
            continue
        crashes = []
        # Walk through the strings, char-by-char
        for i in range(len(str1)):
            char1 = str1[i]
            char2 = str2[i]
            if char1 == char2 and re.match(r"\w", char1):
                crashes.append(char1)
        # If this is a valid crash, add it to our list
        if len(crashes):
            if len(crashes) > 1 and single_crashes_only:
                continue
            crashing_pairs.append((str1, str2, crashes))
    return crashing_pairs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Mandatory args
    parser.add_argument("file1", type=str)
    parser.add_argument("file2", type=str)
    # Optional flags
    parser.add_argument("--ignorespaces", default=False, action="store_true")
    parser.add_argument("--ignorepunctuation", default=False, action="store_true")
    parser.add_argument("--singlecrashesonly", default=False, action="store_true")
    # Parse & run
    args = parser.parse_args(sys.argv[1:])
    main(args.file1, args.file2, args.ignorespaces, args.ignorepunctuation, args.singlecrashesonly)