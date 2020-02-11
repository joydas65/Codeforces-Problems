n = int(input())

arr = list(map(int, input().split()))

left,right,sereja,dima,c = 0,n-1,0,0,0

while left <= right:
    
    if arr[left] == max(arr[left],arr[right]):
        
        if c % 2 == 0:
            sereja += arr[left]
        else:
            dima += arr[left]
        left += 1
        
    else:
        
        if c % 2 == 0:
            sereja += arr[right]
        else:
            dima += arr[right]
        right -= 1
        
    c += 1
print(sereja,dima)
