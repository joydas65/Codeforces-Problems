for _ in range(int(input())):
    
    clock = input()
    
    if clock[:2] == "00":
        print("12"+clock[2:]+" AM")
    elif int(clock[:2]) > 12:
        t = int(clock[:2]) - 12
        if t <= 9:
            t = "0" + str(t)
        print(str(t) + clock[2:] + " PM")
    elif int(clock[:2]) < 12:
        print(clock + " AM")
    else:
        print(clock + " PM")
