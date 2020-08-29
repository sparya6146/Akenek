import heapq

def kCheapestPairs(nums1,nums2, k):
    if not nums1 or not nums2 or not k:
        return None
    n = len(nums1)
    m = len(nums2)
    heap = []
    for i in range(n):
        for j  in range(m):
            curr_total = nums1[i] + nums2[j]
            if len(heap) < k:
                heapq.heappush(heap, (-curr_total, [nums1[i], nums2[j]]))
                continue
            if curr_total < -1 * heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-curr_total, [nums1[i], nums2[j]]))
    return [item[1] for item in heap]

if __name__=='__main__':
    delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
    CheapestPairs = kCheapestPairs(delhi_to_mumbai,mumbai_to_delhi,10)
    print(sorted(CheapestPairs,key=lambda x: x[0]+x[1]))
