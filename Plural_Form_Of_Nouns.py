for _ in range(int(input())):
    
    s = input()
    
    if s[-1] == 'x' or s[-1] == 's' or s[-1] == 'o' or (s[-1] == 'h' and s[-2] == 'c'):
        
        print(s+"es")
        
    elif s[-1] == 'y':
        
        print(s[:len(s)-1]+"ies")
        
    elif s[-1] == 'f' or (s[-1] == 'e' and s[-2] == 'f'):
        
        if s[-1] == 'f':
            
            print(s[:len(s)-1]+"ves")
            
        else:
            
            print(s[:len(s)-2]+"ves")
        
    else:
        
        print(s+"s")
