import re


def russian_phone_number_validator(phone_number: str):
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
    result = re.match(pattern, phone_number)

    return bool(result)