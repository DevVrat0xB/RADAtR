"""
File containing all the general or custom validation functions of intermediate results or input fields.
"""
import re


# function for simple string validation
def check_if_pure_string(string):
    result = bool(re.fullmatch("(^[a-zA-Z][a-zA-Z ]*)", string))
    return result


# function for alphabetical and numerical string
def check_if_alpha_numeric(string):
    result = bool(re.fullmatch("(^[a-zA-Z][a-zA-Z0-9 ]*)", string))
    return result


# function for string with special characters
def check_if_special_string(string):
    result = bool(re.fullmatch("(^[a-zA-Z][a-zA-Z0-9, -]*)", string))
    return result


# function to check if string contains only number
def check_if_numeric(string):
    result = bool(re.fullmatch("(^[0-9]*)", string))
    return result


