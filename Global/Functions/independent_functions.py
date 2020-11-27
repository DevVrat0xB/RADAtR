"""
Contains all functions which are independent of any class or module.
Several different classes, methods may make use of these functions for processing intermediate outputs.
"""


# function which takes datetime as input and  return current date and time
# as a combined, single string-type in YYMMDDHHmm format.
# Y: Year number (last 2 digits)
# M: Month number
# D: Day number of a month
# H: Hour number (24-format, 00-23)
# m: Minute number (00-59)
def convert_datetime_to_number_string(timestamp):
    return timestamp.strftime("%y%m%d%H%M")     # a string type


# function to check if an index exists in the list or not
def index_exists_in(the_list, index):
    for i in range(len(the_list)):
        if the_list[i] == index:
            return True
        else:
            continue

    # in case, the index doesn't exist in the list already
    return False
