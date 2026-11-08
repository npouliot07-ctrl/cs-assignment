def solution(A):
    total_sum = sum(A)
    left_sum = A[0]
    min_diff = abs(left_sum - (total_sum - left_sum))
    
    for i in range(1, len(A) - 1):
        left_sum += A[i]
        diff = abs(left_sum - (total_sum - left_sum))
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

