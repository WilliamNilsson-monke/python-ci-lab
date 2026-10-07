def is_palindrome(text: str) -> bool:
  
    
    
    halfway = len(text) // 2
    queue = list(text[:halfway])

    if len(text) % 2 == 0:
        second_half = text[halfway:]
    else: 
        second_half = text[halfway + 1:]

    for c in second_half:
        if c != queue.pop():
            return False
        
    return True
