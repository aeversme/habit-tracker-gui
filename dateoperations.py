import datetime as dt

# pass date_choice.value and date_entry_textbox.value into date_handler


def date_handler(date_option_choice, date_entry):
    # Flow for 'today'
    if date_option_choice == 'today':
        date = dt.datetime.now()
        date_for_api = format_today_for_api(date)
    # Flow for 'custom'
    else:
        date = date_entry
        try:
            converted_custom_date = convert_custom_date(date)
        except (ValueError, IndexError):
            print('Invalid date entered, try again.')
            return 'invalid date'
        if is_valid_pixela_date(converted_custom_date):
            date_for_api = converted_custom_date
        else:
            print('Date out of range, try again.')
            return 'date out of range'
    return date_for_api


def format_today_for_api(date):
    today_for_api = date.strftime('%Y%m%d')
    return today_for_api


def convert_custom_date(date):
    date_entry_split = [int(value) for value in date.split('-')]
    year = date_entry_split[0]
    month = date_entry_split[1]
    day = date_entry_split[2]
    converted_date = dt.datetime(year=year, month=month, day=day).strftime('%Y%m%d')
    return converted_date


def is_valid_pixela_date(date):
    is_valid = False
    today_int = int(dt.datetime.now().strftime('%Y%m%d'))
    if (today_int - 10000) < int(date) <= today_int:
        is_valid = True
    return is_valid
