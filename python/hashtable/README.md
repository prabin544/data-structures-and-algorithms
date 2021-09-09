# Hashtables
<!-- Short summary or background information -->
Author: Prabin Singh

## Challenge
<!-- Description of the challenge -->

Implement a Hashtable Class with the following methods:

- Add
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- Get
  - Arguments: key
  - Returns: Value associated with that key in the table

- Contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.

- Hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Structure and Testing

Utilize the Single-responsibility principle: any methods you write should be clean, reusable, abstract component parts to the whole challenge. You will be given feedback and marked down if you attempt to define a large, complex algorithm in one function definition.

Write tests to prove the following functionality:

  1. Adding a key/value to your hashtable results in the value being in the data structure
  2. Retrieving based on a key returns the value stored
  3. Successfully returns null for a key that does not exist in the hashtable
  4. Successfully handle a collision within the hashtable
  5. Successfully retrieve a value from a bucket within the hashtable that has a collision
  6. Successfully hash a key to an in-range value

## Credit & Collaborations
Daniel, Davee and Wondwosen
