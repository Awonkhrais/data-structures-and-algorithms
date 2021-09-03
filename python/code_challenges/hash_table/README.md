# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge

The challenge was with collisions and implementing a linked list to solve them, also with testing internals.

## Approach & Efficiency
Big O:

Time: O(n).
space: O(n).


## API

* Create a hashtable with the following methods:
    - `add`which takes in both the key and value. Hash the key, and add the key and value pair to the table, handling collisions as needed.
    - `get` that takes in the key and returns the value from the table.
    - `contains` that takes in the key and returns a boolean, indicating if the key exists in the table already.
    - `hash` that takes in an arbitrary key and returns an index in the collection.

