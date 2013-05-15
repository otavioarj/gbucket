gbucket
=======

Grimly Bucket Sort

A Python implemented Bucket Sort, where worst scenario for sorting A[1...n] is Theta(n). That is possible by using a hash function to index elements on buckets.
Every element is placed at tail of Bucketlist[x], for x=e*i mod (size Bucketlist), where e is A[i].

That code have the worst scenario for regular Bucket Sort already implemented. It is the default execution:
$ python gbucket.py
Bucket 0 , size: 20
Bucket 1 , size: 0
Bucket 2 , size: 20
Bucket 3 , size: 0
Bucket 4 , size: 20
Bucket 5 , size: 0
Bucket 6 , size: 20
Bucket 7 , size: 0
Bucket 8 , size: 20
[65536, 65536, 65536, ..... 65536]

Where each line before A print is actually the size of each Bucket at Bucketlist. So for 100 elements equals 2^16, that algorithm use at maximum 20 buckets in one list. 
If any parameter is given, /dev/urandom is read for 100 pseudo-aleatory elements.

