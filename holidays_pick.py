import holidays 

# uk_holidays = holidays.AUS(years=2025, prov='VIC').items()
uk_holidays = holidays.US(years=2025, state='AL').items()

i = 0
for date, event in sorted(uk_holidays):
    print(f'{date} {event}')
    i += 1
print(i)
