def date_time(dat_tim):
    sana,soat=dat_tim.split()
    day,month,year=list(map(int,sana.split('.')))
    hour,minute=list(map(int,soat.split(':')))
    
    def if_else(soat_1) -> str:
        if soat_1==1:
            return 'hour'
        else:
            return 'hours'

    def if2_else(minut) -> str:
        if minut==1:
            return 'minute'
        else :
            return 'minutes'
        
    dct={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}


 
    print(f"{day} {dct[month]} {year} year {hour} {if_else(hour)} {minute} {if2_else(minute)}")

date_time('21.05.2018 16:30')
date_time("21.10.1999 18:01")
date_time("19.09.2999 01:59")


