"Letter crashes" occur when two words or phrases share a character at the same index. For example, `FOOBAR` and `GROWTH` have a single crash: `O`, at the third position.

This script finds all pairs of words/phrases that have crashing letters.

# Usage

To compare two lists of words/phrases, run the script with each list of phrases saved as a newline-delimited .txt file:

```python find_letter_crashes.py mbta_stations.txt tube_station_names.txt```

Crashing pairs will display as a 3-tuple: (element from List 1, element from List 2, [all crashing letters])

If you wish to find all crashes within only one list, compare the list to itself. Note that this will cause each crashing pair to display twice, as both (A, B) and (B, A). (//TODO: Fix that.)

```python find_letter_crashes.py mbta_stations.txt mbta_stations.txt```

## Optional flags

`--ignorespaces` will remove all whitespace before comparing phrases.
`--ignorepunctuation` will remove all punctuation (non-letters, non-numbers) before comparing phrases.
`--singlecrashesonly` will restrict to pairs that only crash at one position.

All of these flags default to False.
