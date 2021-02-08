"""
The Pixela APIs expect a 'date' header value in the format YYYYMMDD. These functions check custom date inputs, if used,
for entry errors and validity within a specific time range, and then convert the desired date object into the proper
string format.
"""

import datetime as dt


def date_handler(date_option_choice, date_entry):
    """Receives the user's choice of date option and any data in the custom date textbox, and returns
    a date in the correct string format."""
    if date_option_choice == 'today':
        date_object = dt.datetime.now()
    else:
        try:
            custom_date_object = convert_date_string_to_datetime_object(date_entry)
        except (ValueError, IndexError):
            return 'invalid date'
        if is_valid_pixela_date(custom_date_object):
            date_object = custom_date_object
        else:
            return 'date out of range'
    return date_object.strftime('%Y%m%d')


def convert_date_string_to_datetime_object(date):
    """Receives the user's custom date and returns a datetime object."""
    date_entry_split = [int(value) for value in date.split('-')]
    return dt.datetime(year=date_entry_split[0], month=date_entry_split[1], day=date_entry_split[2])


def is_valid_pixela_date(date):
    """Checks a date against a valid range and returns a Boolean."""
    today = dt.datetime.now()
    year_ago = today - dt.timedelta(days=365)
    return year_ago < date <= today
