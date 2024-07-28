def add_time(start, duration, weekday=""):

    pm = 0
    if start[-2:] == "PM":
        pm = 12
    start_h = int(start[:-6])
    start_min = int(start[-5:-3])

    dur_h = int(duration[:-3])
    dur_min = int(duration[-2:])

    print(f"{pm+start_h}:{start_min} + {dur_h}:{dur_min}")
    
    new_total_min = start_h*60 + start_min + pm*60 + dur_h*60 + dur_min
    new_h = new_total_min//60
    new_min = new_total_min%60
    days = new_h//24
    new_h = new_h%24
    new_pm = new_h//12
    new_h = new_h%12
    new_time = ""
    if new_h == 0:
        new_time = "00:"
    else:
        new_time = str(new_h)+":"
    if len(str(new_min)) < 2:
        new_time += "0"
    new_time += str(new_min)
    if new_pm == 0:
        new_time += " AM"
    else:
        new_time += " PM"
    if weekday != "":
        week_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        cur_week_day = week_days.index(weekday.lower())
        new_week_day = (cur_week_day+days)%7
        new_time+= ", "+week_days[new_week_day].capitalize()

    next_day = ""
    if days > 1:
        next_day = " ("+str(days)+" days later)"
    elif days == 1:    
        next_day = " (next day)"
    new_time += next_day
    return new_time
new_time = add_time('2:59 AM', '24:00', 'saturDay')
print(new_time)