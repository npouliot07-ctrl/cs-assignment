def solution(A, K):

    if not A:
        return A
        
    # Divide K if it's larger than the array length
    K = K % len(A)
    
    # Slice and build the array again
    return A[-K:] + A[:-K]
