from Database.database_connection import *
from Database.school_database_variables import *


class Student:
    def __init__(self, name, guardian_name, registration_number, dob,
                 gender, address, category, previous_education,
                 fee_status, email, contact_no, disability=None):
        self.name = name
        self.guardian_name = guardian_name
        self.registration_number = registration_number
        self.dob = dob
        self.gender = gender
        self.address = address
        self.category = category
        self.previous_education = previous_education
        self.fee_status = fee_status
        self.email = email
        self.contact_no = contact_no
        self.disability = disability
        self.stud_id = self.generate_stud_id()    # this will work iff generate_stud_id() is defined

    # Used to generate student unique id for respective student
    # Not Yet Defined
    def generate_stud_id(self):
        pass


# Call this function to store a student in
# student_object's type will be above mentioned class "Student" object
def store_in_db(student_object):
    db[student_collection].insert({"name": student_object.name, "guardian_name": student_object.guardian_name,
                                   "registration_number": student_object.registration_number,
                                   "dob": student_object.dob, "gender": student_object.gender,
                                   "address": student_object.address, "category": student_object.category,
                                   "previous_education": student_object.previous_education,
                                   "fee_status": student_object.fee_status, "email": student_object.email,
                                   "contact_no": student_object.contact_no, "disability": student_object.disability,
                                   "stud_id": student_object.stud_id})

    print("Data Inserted In Student Collection")


# Call this function to get student collection
def get_details_from_db():
    cursor = db[student_collection].find({})
    return cursor
