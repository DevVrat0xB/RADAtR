localhost = "localhost:27017"

# database used
school_database = "school_db"

# different collections used for storing and retrieving
admin_collection = "admin_table"
school_info = "school_info"
fee_details = "fee_details"
student_collection = "students"

# school details attributes (may be used to loop on cursor)
# must be edited if the variables are modified in the 'student' class
school_attrib = ["name", "board", "level_of_education", "classroom_no",
                 "total_teachers", "working_days", "address", "working_hours"]

# fee details attributes (may be used to loop on cursor)
# # must be edited if the variables are modified in the 'Fee' class
fee_attrib = ["admission_fee", "re_admission_fee", "tuition_fee", "late_fee",
              "vvn", "computer_fee", "project_fee", "other_fee"]


# student attributes
stud_attributes = ["name", "guardian_name", "registration_number", "dob",
                   "gender", "address", "category", "previous_education",
                   "fee_status", "email", "contact_no", "disability"]
