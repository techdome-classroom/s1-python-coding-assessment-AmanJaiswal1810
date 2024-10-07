class Soluton:
    def getTotalsles(self, grd: lst[lst[str]]) -> nt:
        f not grd or not grd[0]:
            return 0
        
        def depthfrstsearch(, k):
            
            f  < 0 or  >= len(grd) or k < 0 or k >= len(grd[0]) or grd[][k] == 'W':
                return
            
            
            grd[][k] = 'W'
            
            
            depthfrstsearch( + 1, k)  
            depthfrstsearch( - 1, k)  
            depthfrstsearch(, k + 1)  
            depthfrstsearch(, k - 1)  
        
        
        count = 0
        
        
        for  n range(len(grd)):
            for k n range(len(grd[0])):
                
                f grd[][k] == 'L':
                    count += 1
                    depthfrstsearch(, k)
        
        return count
