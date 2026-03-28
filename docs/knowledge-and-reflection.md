# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> All these functions are hash functions because they take a key (like string) and convert it into an integer value that can be used as an index in a hash table. They all share a few key property: the are deterministic (same imput gives same output), they return  a number and they limit the result to a fixed range using `% size`. This makes them suitable for storing and retrieving data efficiently.  

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> The stupidly simple hash is very, but it always returns the same value. This means it has terrible uniformity and extremely high collisions, so it is not useful in practice.
> The sum of ASCII values is simple and efficient and it is deterministic. However, it has poor collision resistance because different keys can easily produce the same sum (words that have the same letters and same amount). It is also not very sensitive to small input changes.
> The Pearson hash is more balanced. It is still fast and deterministic but it gives better uniformity and fewer collisions compared to simple methods. It is also more sensitive to input changes. However, it is not designed for security.
> The built-in Python hash is efficient and usually provides good distribution (uniformity). It is deterministic within ona program run, but in modern Python it  may change between runs for security reasons. It has moderate collision resistance but is not cryptographically secure.
> The SHA256 hash is the strongest. It has very high uniformity, strong collision resistance, and is highly sensitive to even small input changes. It is also secure and used in cryptography. The main disadvantage is that it is slower and more computationally expensive than the others.

>References (APA 7)

> National Institute of Standards and Technology. (2015). Secure Hash Standard (SHS) (FIPS PUB 180-4). https://doi.org/10.6028/NIST.FIPS.180-4

> Python Software Foundation. (2024). hash() function. https://docs.python.org/3/library/functions.html#hash

> Wikipedia contributors. (2024). Pearson hashing. Wikipedia. https://en.wikipedia.org/wiki/Pearson_hashing


3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Uniformity. A good hash function should spread keys evenly across the table. This reduces collisions and keeps operations like search, insert, and delete fast. If the distribution is poor, performance can degrade significantly (Cormen et al., 2009).

> Efficiency. The hash function should be fast to compute. Hash maps are used for quick access, so if the hash function is slow, it defeats the purpose of using a hash table.

> Collision resistance. It is important to minimise collisions. Fewer collisions mean less need for extra handling (like chaining or probing), which improves overall performance.

> References (APA 7)

> Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms (3rd ed.). MIT Press.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would choose the Pearson hash function for this task.It gives a good balance between speed and quality of hashing. Since I am building a hash map for a double linked list, I need a function that distributes keys more evenly to reduce collisions. Pearson hashing does this better than simple functions like summing ASCII values.
> It is also efficient to compute, so it will not slow down the program. At the same time, it is more sensitive to small changes in the input, which helps produce different hash values for similar keys.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> random.seed(42) - This sets a fixed seed for the random generator. It ensures that the same shuffled table is created every time, which makes the hash function deterministic.

> pearson_table = list(range(256)) - This creates a list of numbers from 0 to 255 with no duplicates. This is important for good uniformity and helps avoid unnecessary collisions.

> random.shuffle(pearson_table) - This shuffles the table into a random order. It improves how values are spread, which increases uniformity and collision resistance.

> hash_ = 0 - Initializes the hash value. It is simple and supports efficiency and determinism.

> for char in key: - Loops through each character in the key. This ensures the whole input affects the result, improving uniformity.

> hash_ = pearson_table[hash_ ^ ord(char)] - ord(char) converts the character to a number. Then ^ (XOR) mixes the current hash value with the character value. This makes the function sensitive to small input changes, improving collision resistance and uniformity.Looking up the result in pearson_table adds more mixing, which helps spread values more evenly across the table.

> return hash_ % size - Limits the result to the table size. This ensures the value fits in the hash map and keeps operations efficient (efficiency).

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> pseudocode
procedure store-Player (map, key, player_or_name):
      index ← HASH(key) mod SIZE
      bucket ← map.buckets[index]          // PlayerList (doubly linked list)

      node ← bucket.first
      while node ≠ null:
          if node.key == key:
              if player_or_name is Player:
                  node.player ← player_or_name
              else:
                  node.player.name ← player_or_name
              return
          node ← node.next

      if player_or_name is Player:
          player ← player_or_name
      else:
          player ← new Player(key, player_or_name)

      bucket.insert_last( new PlayerNode(player) )
      map.count ← map.count + 1

## Reflection

1. What was the most challenging aspect of this task?

>  Getting the hashing and collision chaining consistent across Player.hash, __hash__, and PlayerHashMap.get_index, then validating it with tests (especially the collision case and update behavior). That alignment between hashing, bucket selection, and list traversal was the trickiest part.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

>  I would replace each bucket’s PlayerList with a built‑in structure like a Python list (dynamic array) or dict. A list would simplify insertion and traversal while still supporting chaining, and a dict per bucket would make lookups and updates faster and simpler by using key lookup directly. This would reduce custom linked‑list code and potential bugs, while improving readability and often performance for typical workloads.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
