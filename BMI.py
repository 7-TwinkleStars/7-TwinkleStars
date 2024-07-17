MassKG = int(input('Enter Weight: '))
HeightM = int(input('Enter Height: '))
BMI = (MassKG / HeightM * HeightM)
print(f'Your BMI is {BMI}')


def main():
    year = int(input("Enter year:"))
    lunar_year_cycle_position = year % 19
    weekday_slide_part_1 = year % 4
    weekday_slide_part_2 = year % 7
    leap_year_100 = year // 100
    leap_year_400 = leap_year_100 // 4
    lunar_orbit_correction = (13 + 8 * leap_year_100) // 25
    century_start = (15 - lunar_orbit_correction + leap_year_100 - leap_year_400) % 30
    sunday_offset = (4 + leap_year_100 - leap_year_400) % 7
    days_added = (19 * lunar_year_cycle_position + century_start) % 30
    days_of_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7
    total_days_added = (22 + days_added + days_of_week_offset)
    day_of_easter = total_days_added % 31
    month_of_easter = 3 + (total_days_added // 31)

    print(f'Easter is {day_of_easter}, {month_of_easter}.')


if __name__ == "__main__":
    main()
