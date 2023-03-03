def maxSubarraySum(arr, n) :
    cur_sum=0 
    maxsum = 0 

    for i in range(n):
        cur_sum=cur_sum+arr[i] 
        maxsum=max(maxsum,cur_sum) 
        if cur_sum<0:
            cur_sum=0 
    # return the answer
    return maxsum
