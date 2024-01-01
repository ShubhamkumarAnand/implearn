# Bloom Filter - Probabilistic Data Structure To Check Membership

A bloom filter is a space-efficient data structure used to test whether an item is a member of a set. It is represented by a bit array of length n, where each bit is initially set to zero. When an item is added to the filter, multiple hash functions are applied to it, and the corresponding bits in the array are set to one. To check if an item is in the filter, the same hash functions are applied, and if any of the corresponding bits are zero, the item is not a member. The performance of the filter depends on the hash functions used.

- [Explanation Article Link](https://systemdesign.one/bloom-filters-explained/)
- [Implementation Article Link](https://brilliant.org/wiki/bloom-filter/#:~:text=A%20bloom%20filter%20is%20a,is%20added%20to%20the%20set.)
