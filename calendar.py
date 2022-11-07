from datetime import datetime, timedelta


days_name = {
   0: 'Monday',
   1: 'Tuesday',
   2: 'Wednesday',
   3: 'Thursday',
   4: 'Friday',
   5: 'Saturday',
   6: 'Sunday',
}

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []


def birthday(users: list):
    current_date = datetime.now()
    max_date = current_date + timedelta(days=7)

    for user in users:
        birthday_date = user['birthday']
        this_year_birthday = datetime(current_date.year, birthday_date.month, birthday_date.day)
        if current_date < this_year_birthday <= max_date:
            birth_week_day = this_year_birthday.weekday()
            if birth_week_day == 0 or birth_week_day == 5 or birth_week_day == 6:
                monday.append(user['name'])
            if birth_week_day == 1:
                tuesday.append(user['name'])
            if birth_week_day == 2:
                wednesday.append(user['name'])
            if birth_week_day == 3:
                thursday.append(user['name'])
            if birth_week_day == 4:
                friday.append(user['name'])
        else:
            continue
    print_birth_day()


def print_birth_day():

    current_week_day = datetime.now().weekday()
    monday_users = ', '.join(monday)
    tuesday_users = ', '.join(tuesday)
    wednesday_users = ', '.join(wednesday)
    thursday_users = ', '.join(thursday)
    friday_users = ', '.join(friday)

    if current_week_day == 0:
        print(f'{days_name[1]}: {tuesday_users}')
        print(f'{days_name[2]}: {wednesday_users}')
        print(f'{days_name[3]}: {thursday_users}')
        print(f'{days_name[4]}: {friday_users}')
        print(f'{days_name[0]}: {monday_users}')
    elif current_week_day == 1:
        print(f'{days_name[2]}: {wednesday_users}')
        print(f'{days_name[3]}: {thursday_users}')
        print(f'{days_name[4]}: {friday_users}')
        print(f'{days_name[0]}: {monday_users}')
        print(f'{days_name[1]}: {tuesday_users}')
    elif current_week_day == 2:
        print(f'{days_name[3]}: {thursday_users}')
        print(f'{days_name[4]}: {friday_users}')
        print(f'{days_name[0]}: {monday_users}')
        print(f'{days_name[1]}: {tuesday_users}')
        print(f'{days_name[2]}: {wednesday_users}')
    elif current_week_day == 3:
        print(f'{days_name[4]}: {friday_users}')
        print(f'{days_name[0]}: {monday_users}')
        print(f'{days_name[1]}: {tuesday_users}')
        print(f'{days_name[2]}: {wednesday_users}')
        print(f'{days_name[3]}: {thursday_users}')
    else:
        print(f'{days_name[0]}: {monday_users}')
        print(f'{days_name[1]}: {tuesday_users}')
        print(f'{days_name[2]}: {wednesday_users}')
        print(f'{days_name[3]}: {thursday_users}')
        print(f'{days_name[4]}: {friday_users}')


if __name__ == '__main__':

    users = [
        {'name': 'Bill', 'birthday': datetime(year=1994, month=11, day=8)},
        {'name': 'John', 'birthday': datetime(year=1996, month=11, day=9)},
        {'name': 'Lili', 'birthday': datetime(year=1997, month=11, day=9)},
        {'name': 'Kim', 'birthday': datetime(year=1985, month=11, day=14)},
        {'name': 'Jill', 'birthday': datetime(year=1995, month=11, day=10)},
        {'name': 'Ben', 'birthday': datetime(year=1989, month=11, day=15)},
        {'name': 'Stiv', 'birthday': datetime(year=1992, month=11, day=14)},
        {'name': 'Tom', 'birthday': datetime(year=1986, month=11, day=13)},
        {'name': 'Ilon', 'birthday': datetime(year=1998, month=11, day=13)},
        {'name': 'Rick', 'birthday': datetime(year=1987, month=11, day=16)},
        {'name': 'Jack', 'birthday': datetime(year=1994, month=11, day=12)}
    ]

    birthday(users)