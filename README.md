"Letter crashes" occur when two words or phrases share a character at the same index. For example, `FOOBAR` and `GROWTH` have a single crash: `O`, at the third position.

This script finds all pairs of words/phrases that have letter crashing.

# Usage

To compare two lists of words/phrases, run the script with each list of phrases saved as a newline-delimited .txt file:

```python find_letter_crashes.py mbta_stations.txt tube_station_names.txt```

If you wish to find all crashes within only one list, compare the list to itself:

```python find_letter_crashes.py mbta_stations.txt mbta_stations.txt```

Note that comparing a list to itself will cause each pair to display twice, as both (A, B) and (B, A). (TODO: Fix that.)

## Optional flags

`--ignorespaces` will remove all whitespace before comparing phrases.
`--ignorepunctuation` will remove all punctuation (non-letters, non-numbers) before comparing phrases.
`--singlecrashesonly` will restrict to pairs that only crash at one position.

All of these flags default to False.
