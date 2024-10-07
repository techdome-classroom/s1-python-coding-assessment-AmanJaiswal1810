def decode_message(s: str, p: str) -> bool:
    
    Dp_Table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    Dp_Table[0][0] = True  
    
    for l in range(1, len(p) + 1):
        if p[l - 1] == '*':
            Dp_Table[0][l] = Dp_Table[0][l - 1]
    
    
    for k in range(1, len(s) + 1):
        for l in range(1, len(p) + 1):
            if p[l - 1] == '*':
                Dp_Table[k][l] = Dp_Table[k][l - 1] or Dp_Table[k - 1][l]
            elif p[l - 1] == '?' or p[l - 1] == s[k - 1]:
                Dp_Table[k][l] = Dp_Table[k - 1][l - 1]
    
    return Dp_Table[len(s)][len(p)]
