def solution(A):
    N = len(A)
    
    # The full range of numbers 
    total_elements = N + 1
    
    #expected sum of numbers from 1 to N + 1
    expected_sum = (total_elements * (total_elements + 1)) // 2
    
    # Calculate the actual sum of the elements 
    actual_sum = sum(A)
    
    # Missing element difference
    return expected_sum - actual_sum

