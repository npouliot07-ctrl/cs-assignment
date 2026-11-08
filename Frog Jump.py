def solution(X, Y, D):
    # Calculate distance frog needs to cover
    distance = Y - X
    
    # If the frog is already at or past the target, 0 jumps are needed
    if distance <= 0:
        return 0
       
    # Calculate the min number of whole jump needed 
    jumps = distance // D

    # If remainder distance, clear target so add one jump to cover distance
    if distance % D != 0:
        jumps += 1
        
    return jumps
