def sqInRect(lng, wdth):
    if lng == wdth:
    # your code
        return None
    
    elif lng > wdth:
        pass
        result = []
        other = lng * wdth - wdth * wdth
        #print(other)
        result.append(wdth)
        while other - wdth * wdth >=2:
            other = other - wdth * wdth
            result.append(wdth)
        while other - wdth * wdth < 2:
            for wdth_1 in range(wdth,0,-1):
                if other - wdth_1 * wdth_1 > 2:
                    other = other - wdth_1 * wdth_1
                    result.append(wdth_1)
                else:
                    continue
            
        
        
        
        for wdth_1 in range(wdth,0,-1):
            
                if other - wdth_1 * wdth_1 >2:
                    result.append(wdth_1)
                    other = other - wdth_1 * wdth_1
                    
                    
            x=(other - wdth_1*wdth_1)
            #print(x)
            if str(x).isdigit():
                result.append(wdth_1)
                print(wdth_1)
            #print(wdth_1)
            wdth_1 = wdth - 1
            if wdth_1 >=2 and (other - (wdth_1 * wdth_1) >=2):
                result.append(wdth_1)
                result.append(1)
                result.append(1)
                pass
        return result    
        
    else:
        #pass
        result = []
        other = lng * wdth - lng * lng
        #print(other)
        result.append(lng)
        for wdth_1 in range(lng,2,-1):
            print(wdth_1)
            lng_1 = lng - 1
            if lng_1 >=2 and (other - (lng_1 * lng_1) >=2):
                result.append(lng_1)
                result.append(1)
                result.append(1)
                pass
        return result