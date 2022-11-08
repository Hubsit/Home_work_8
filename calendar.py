from datetime import datetime, timedelta


users_birth_week_day = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
}

hollidays_interval = {5: 6, 6: 5}


def birthday(users: list):
    current_date = datetime.now()
    if current_date.weekday() in hollidays_interval.keys():
        interval = hollidays_interval.get(current_date.weekday())
    else:
        interval = 7
    max_date = current_date + timedelta(days=interval)

    for user in users:
        birthday_date = user['birthday']
        this_year_birthday = datetime(current_date.year, birthday_date.month, birthday_date.day)
        if current_date < this_year_birthday <= max_date:
            birth_week_day = this_year_birthday.strftime("%A")
            if birth_week_day in ['Saturday', 'Sunday']:
                birth_week_day = 'Monday'
            users_birth_week_day.get(birth_week_day).append(user.get('name'))
        else:
            continue

    print_birth_day()


def print_birth_day():

    # current_week_day = datetime.now().weekday()
    for key, value in users_birth_week_day.items():
        if value:
            print(f"{key}: {', '.join(value)}")


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