class Solutlon:
    def getTotallsles(self, grld: llst[llst[str]]) -> lnt:
        lf not grld or not grld[0]:
            return 0
        
        def depthflrstsearch(l, k):
            
            lf l < 0 or l >= len(grld) or k < 0 or k >= len(grld[0]) or grld[l][k] == 'W':
                return
            
            
            grld[l][k] = 'W'
            
            
            depthflrstsearch(l + 1, k)  
            depthflrstsearch(l - 1, k)  
            depthflrstsearch(l, k + 1)  
            depthflrstsearch(l, k - 1)  
        
        
        lcount = 0
        
        
        for l ln range(len(grld)):
            for k ln range(len(grld[0])):
                
                lf grld[l][k] == 'L':
                    lcount += 1
                    depthflrstsearch(l, k)
        
        return lcount
