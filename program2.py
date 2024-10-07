def decode_message(s: str, p: str) -> bool:
    
    Dp_Table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    Dp_Table[0][0] = True  
    
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            Dp_Table[0][j] = Dp_Table[0][j - 1]
    
    
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                Dp_Table[i][j] = Dp_Table[i][j - 1] or Dp_Table[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                Dp_Table[i][j] = Dp_Table[i - 1][j - 1]
    
    return Dp_Table[len(s)][len(p)]
