
# Simple Date conversion function : 10-character-string -> 6-character-string (universal date)
# 'dd.mm.yyyy' -> 'yyyymmdd'
def EuroToStandardDateConversion(euroDate):
    yyyy = euroDate[6:10]
    mm = euroDate[3:5]
    dd = euroDate[0:2]
    return yyyy + mm + dd

# Examples
date_01 = '01.01.2019'
date_02 = '31.12.2020'
date_03 = '08.08.2019'
date_04 = '02.09.2020'

d1 = EuroToStandardDateConversion(date_01)
d2 = EuroToStandardDateConversion(date_02)
d3 = EuroToStandardDateConversion(date_03)
d4 = EuroToStandardDateConversion(date_04)

print d1,d2,d3,d4

# Simple Time-Formatting funcion
# 4-character-string for time -> 5-character-string
# '2030' -> '20:30'
def ConvertToTime(hhmm):
    return hhmm[0:2]+ ':' + hhmm[2:4]

ConvertToTime('2050')
