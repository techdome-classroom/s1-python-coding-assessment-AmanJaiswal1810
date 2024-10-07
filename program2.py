def decode_message(s: str, p: str) -> bool:
    
     = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    [0][0] = True  # Empty pattern matches empty string

    
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            [0][j] = [0][j - 1]
    
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                [i][j] = [i][j - 1] or [i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                [i][j] = [i - 1][j - 1]
    
    return [len(s)][len(p)]
