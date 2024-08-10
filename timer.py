def add_time(time="00:00 AM",dur="00:01:00",weekday=None,month=None,year="0"):
    hours,mins=time.split(":")
    mins,period=mins.split(" ")
    dur_days,dur_h,dur_m=dur.split(":")
    mins=int(mins)+int(dur_m)
    add_period = 0
    if period == "PM":
        add_period = 12
    total_h = int(hours)+int(dur_h)+add_period+mins//60
    remain_m = mins%60
    days = total_h//24+int(dur_days)
    remain_h = total_h%24
    new_period = "AM"
    if (remain_h//12)%2==1:
        new_period ="PM"
        remain_h = remain_h%12
    if (remain_h) == 0 and new_period == "PM":
        remain_h = 12
        new_period = "AM"
    if remain_m<10:
        remain_m = "0"+str(remain_m)
    next_day = "(same day)"
    if days==1:
        next_day = "(next day)"
    elif days>1:
        n_days = days
        n_years  = n_days//365
        if n_years >= 1:
            n_days = n_days%365
        n_weeks = n_days//7
        n_days = n_days%7+n_years//4
        next_day=f"({n_years} years {n_weeks} weeks {n_days} days later)"
    new_week = "" 
    if weekday:
        week = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        cur_week = week.index(weekday.lower())
        new_week = "\n"+week[(cur_week+days)%7].capitalize()
    new_month = ""
    new_year = ""
    dir = 1
    start_y,bc = year.split(" ")
    if bc == "BC":
        dir = -1
    start_y = int(start_y)*dir
    if month:
        bisestile = start_y%4
        giorno,mese = month
        months = ["january","february","march","april","may","june","july","august","september","october","november","december"]
        calendar = {m:31 if months.index(m)%2 == 0 else 30 for m in months}
        for m in months[7:]:
            if months.index(m)%2==1:
                calendar[m] = 31
            else:
                calendar[m] = 30
        calendar["february"] = 28
        if bisestile:
            calendar["february"] = 29
        left = days
        cur_day = giorno
        cur_month = mese.lower()
        end_year = start_y
        while left > 0:
            left-=1
            cur_day +=1
            if cur_day > calendar[cur_month]:
                cur_day = 0
                left+=1
                cur_month=months[(months.index(cur_month)+1)%12]
                if cur_month == months[0]:
                    end_year+=1
                    if end_year%4==0:
                        calendar["february"] = 29
                    else:
                        calendar["february"] = 28
        new_month  = f" {cur_day} {str(cur_month).capitalize()}"
        if start_y:
            ad = "AD"
            if end_year == 0:
                ad = ""
            elif end_year < 0:
                ad = "BC"
            new_year = f" {abs(end_year)} {ad}"
    return f"{remain_h}:{remain_m} {new_period} {next_day}{new_week}{new_month}{new_year}"

test=add_time("4:16 PM","100:00:00","Saturday",(10,"August"),"2024 AD")

print(test)