"""
bala
"""
def current_age(birthday, today):
    """
    trala
    """
    year_diff = today.year - birthday.year
    no_birthday_this_year = (today.month, today.day) < (birthday.month, birthday.day)
    if no_birthday_this_year:
        return year_diff -1
    return year_diff
