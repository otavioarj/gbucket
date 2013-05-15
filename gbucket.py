# Author Otavio Augusto, at otavioarj gmail.com
# This code is at GPLv2

#!/usr/bin/python
import struct, math,sys


def bucketsort( A):
	code = hashing(len(A))
	buckets = [list() for _ in range( code )]
	bucks=len(buckets)
	for i in range(0,len(A),1):		
		x = re_hashing(A[i], i, bucks)
		buckets[x].append( A[i] )
	#print len(buckets)
	for x  in range(0,bucks):
		print "Bucket %d , size: %d"%(x,len(buckets[x]))
		buckets[x]=merge_sort(buckets[x])
	ndx=0
	for b in range( len( buckets ) ):
		for v in buckets[b]:
			A[ndx] = v
			ndx += 1
 
 
def hashing( lA):
	return int( math.sqrt(lA))
 
 
def re_hashing(x, i, bucks  ):
  return int((i*x) % bucks) 

def merge_sort(li):
    if len(li) < 2: return li
    m = len(li) / 2
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1            
    result += l[i:]
    result += r[j:]
    return result


def main():
	A=[]
	file=open("/dev/urandom","rb")
	for i in range(0,100):
		if(len(sys.argv)>1):
			barray=file.read(4)
			num=0
			for x in range(4,-1,-1):
				num+=ord(barray[x-1])*8*(4-x)
		else:
			num=2**16
		A.append(num)
	#A=[2,5,7,9]
	bucketsort(A)
	print A

main()
