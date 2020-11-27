"""
This file consists of the functions which are used to initialize, modify or delete
fundamental configurations required by the application.
"""

from Database.database_connection import *
from Database.school_database_variables import *


# initially saving the school details
# (called by class SchoolInfoForm in W_SchoolInfoForm file)
def save_school_details(
        name, board, level_of_education, classroom_no,
        total_teachers, working_days, address, working_hours
    ):
    # following (all) is the insert query
    db[school_info].insert(
        {
            "name": name,
            "board": board,
            "level_of_education": level_of_education,
            "classroom_no": classroom_no,
            "total_teachers": total_teachers,
            "working_days": working_days,
            "address": address,
            "working_hours": working_hours,
            "data_inserted": "true"
        }
    )
    # acknowledgement of record insertion
    print("Basic school details entered successfully.")


# getting the school details (searching can be done only by name of school)
# (called by class SchoolInfoForm in W_SchoolInfoForm file)
def get_school_details(name=None):
    cursor = db[school_info].find({"name": name}, {"_id": 0})
    school_details = {key: None for key in school_attrib}
    for value in cursor:
        school_details.update(value)

    for k, v in school_details.items():
        print(k, " : ", v)

    return school_details


# call this function for saving fee details for the first time ever
def save_fee_structure_details(
        admission_fee, re_admission_fee, tuition_fee,
        late_fee, vvn, computer_fee, project_fee, other_fee
    ):
    # following (all) is the insert query
    db[fee_details].insert(
        {
            "admission_fee": admission_fee,
            "re_admission_fee": re_admission_fee,
            "tuition_fee": tuition_fee,
            "late_fee": late_fee,
            "vvn": vvn,
            "computer_fee": computer_fee,
            "project_fee": project_fee,
            "other_fee": other_fee,
            "data_inserted": "true"
        }
    )
    # acknowledgement of record insertion
    print("Fee structure details saved successfully.")


# call this function to get fee details from database
def get_fee_structure():
    cursor = db[fee_details].find({}, {"_id": 0})
    fee = {key: None for key in fee_attrib}
    for value in cursor:
        fee.update(value)

    for k, v in fee.items():
        print(k, " : ", v)

    return fee


# call this to check if school details are already inserted and if yes then disable school details window accordingly
def if_school_details_are_inserted():
    cursor = db[school_info].find_one({"data_inserted": "true"}, {"_id": 0})
    if cursor["data_inserted"] == "true":
        print("disable the school details window , data is already inserted")
        return True


# call this to check if fee details are already inserted and if yes then disable fee window accordingly
def if_fee_details_are_inserted():
    cursor = db[fee_details].find_one({"data_inserted": "true"}, {"_id": 0})
    if cursor["data_inserted"] == "true":
        print("disable the fee details window , data is already inserted")
        return True
