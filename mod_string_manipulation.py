import re  # regular expression library
import string


def remove_special_char_and_compress(string1):
    allow = string.ascii_letters + string.digits + '.' + ','
    string1 = re.sub('[^%s]' % allow, '', str(string1))

    # sometimes there are two types in the "Type" column. Concatenate them.
    if string1.count(",") + 1 == 8:
        temp_arr = string1.split(',')
        temp_arr[4] = string1.split(',')[4] + string1.split(',')[5]
        temp_arr[5] = string1.split(',')[6]
        temp_arr[6] = string1.split(',')[7]
        temp_arr = temp_arr[:7]
        string1 = ','.join(temp_arr)
    return string1
