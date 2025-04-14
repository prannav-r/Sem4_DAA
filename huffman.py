import heapq
from collections import Counter

def huffman (x):
    freq=Counter(x)
    
    heap = []
    for char,f in freq.items():
        node = [f,[char,'']]
        heap.append(node)
    heapq.heapify(heap)

    while len(heap)>1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(heap,[lo[0]+hi[0]]+lo[1:]+hi[1:])

    huff={}
    for char,code in heap[0][1:]:
        huff[char]=code

    return huff,freq

x,y=huffman("hello")
print("Huffman Codes:",x)
print("Frequencies:",y)