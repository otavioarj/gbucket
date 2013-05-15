gbucket
=======

Grimly Bucket Sort

A Python implemented Bucket Sort, where worst scenario for sorting A[1...n] is Theta(n). That is possible by using a hashing function to index elements on buckets.
Every element is placed at tail of Bucket_list[x], for x=e*i mod (size Bucket_list), where e is A[i].

That code have the worst scenario for regular Bucket Sort already implemented. It is the default execution:
$ python gbucket.py
10
20
0
20
0
20
0
20
0
20
0
[65536, 65536, 65536, ..... 65536]

Where each line before A print is actually the size of each Bucket at Bucket_list. So for 100 elements equals 2^16, that algorithm use at maximum 20 buckets in one list. 
If any parameter is given, /dev/urandom is read for 100 pseudo-aleatory elements.

