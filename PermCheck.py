def solution(A):
    
    N = len(A)
    
    unique_elements = set(A)
    
    # If there is duplicate it isn't a permutation 
    if len(unique_elements) != N:
        return 0
    
    # Check if the maximum element is exactly N. 
    if max(unique_elements) == N:
        return 1
        
    return 0
