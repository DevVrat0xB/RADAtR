"""
Represent a (bare) widget (to be placed inside 'SettingsCategories' Widget) that contains several
input fields for storing fundamental school information.
"""

import sys
from Global.Functions.independent_functions import index_exists_in
from Global.Functions.validation_functions import *
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QCheckBox, QComboBox, QTimeEdit
)


# represents a form which takes basic information about the school as an input
class SchoolInfoForm(QWidget):
    def __init__(self, parent=None, footer_ref=None):
        super().__init__(parent)

        """used to point to the footer widget which will have the 'next', 'back' buttons.
                    Footer will also have required function to control the warning prompts"""
        self.footerWidgetRef = footer_ref

        # variable dependencies
        self.screenCount = 0                        # used for changing index for stacked widgets
        self.InvalidInputFields = []
        self.ignoredWarnings = []               # same as InvalidInputFields variable, but used only for waring purpose
        self.workingDaysCheckboxes = []    # contains all the checkboxes generated for working days
        self.streamCheckboxes = []              # contains all the checkboxes generated for streams
        self.daysSelected = []
        self.streamSelected = []

        # list of warnings that would be prompted on the GUI on respective invalid input (a dictionary type)
        # {"input_field_number": "warning on invalid input for the field"}
        self.warningMessages = {
            "1": "[Invalid Name] Check numbers, spaces and special characters.",
            "2": "[Invalid Address] Check special characters (except - or ,).",
            "3": "[No input] Please select a board.",
            "4": "[No input] Please select an education level.",
            "5": "[No input] Please select at least 1 stream.",
            "6": "[Invalid classrooms no.] Value must be less than 71.",
            "7": "[Invalid teachers no.] Value must be less than 71.",
            "8": "[No input] Please select no. of shifts.",
            "9": "[Invalid Time] Start and End time cannot be same.",
            "10": "[No input] Select at least 1 working day."
        }

        # list of all major Boards in India
        self.boardList = [
            '-- Select --',
            'Central Board of Secondary Education',
            'Indian Certificate of Secondary Education/Indian School Certificate',
            'State Board'
        ]

        # list of education levels
        self.educationLevels = [
            '-- Select --',
            'Up to 5th class (Primary)',
            'Up to 8th class',
            'Up to 10th class (High School)',
            'Up to 12th class (Intermediate)'
        ]

        # possible stream combination (must be exported from a dedicated file/DB)
        self.streams = [
            'Science (Physics, Chemistry, Maths) with Computers',
            'Science (Physics, Chemistry, Maths) without Computers',
            'Science (Physics, Chemistry, Biology) without Computers',
            'Commerce'
        ]

        # main layout of the widget
        self.mainLayout = QFormLayout(self)

        # font family, size and color
        form_font = QFont("Trebuchet")
        form_font.setPointSize(10)
        self.setFont(form_font)

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.formPalette = self.palette()
        self.formPalette.setColor(self.foregroundRole(), QColor('white'))
        self.setPalette(self.formPalette)

        # input fields widgets
        # text widgets for the window
        self.schoolNameLabel = QLabel('1) School Name')
        self.schoolAddressLabel = QLabel('2) School Address')
        self.boardLabel = QLabel('3) Board Affiliated to')
        self.educationLevelLabel = QLabel('4) Offers classes')
        self.streamLabel = QLabel('5) Streams available')
        self.workingDaysLabel = QLabel('10) Operates on')

        """" input fields of the window """
        # for school name input
        self.schoolNameField = QLineEdit()                         # input field 1
        self.schoolNameField.textChanged.connect(lambda: self.check_name_field_validity())
        self.schoolNameField.setFixedWidth(450)

        # for school address (3 liner) input
        self.schoolAddressFieldPart1 = QLineEdit()            # input field 2 (line 1)
        self.schoolAddressFieldPart1.textChanged.connect(lambda: self.check_address_field_validity())
        self.schoolAddressFieldPart1.setFixedWidth(450)
        self.schoolAddressFieldPart2 = QLineEdit()            # Line 2 (part 2)
        self.schoolAddressFieldPart2.textChanged.connect(lambda: self.check_address_field_validity())
        self.schoolAddressFieldPart2.setFixedWidth(450)
        self.schoolAddressFieldPart3 = QLineEdit()            # Line 3 (part 3)
        self.schoolAddressFieldPart3.textChanged.connect(lambda: self.check_address_field_validity())
        self.schoolAddressFieldPart3.setFixedWidth(450)

        # for board name selection
        self.boardField = QComboBox(self)                         # input field 3
        self.boardField.addItems(self.boardList)                # the passed list values must be fetch from DB
        self.boardField.currentIndexChanged.connect(lambda: self.check_board_field_validity())
        self.boardField.setFixedWidth(450)

        # for education level selection
        self.educationLevelField = QComboBox(self)          # input field 4
        self.educationLevelField.addItems(self.educationLevels)  # the passed list values must be fetch from DB
        self.educationLevelField.currentIndexChanged.connect(lambda: self.check_education_level_field_validity())
        self.educationLevelField.setFixedWidth(450)

        # for stream selection
        # container/area for containing all checkboxes of each stream combinations
        self.streamsInputArea = QWidget(self)                   # input field 5
        self.streamsInputAreaLayout = QVBoxLayout(self.streamsInputArea)
        # generating checkboxes...
        for index in range(len(self.streams)):
            stream_checkbox = self.generate_stream_options_for(index, self.streams[index])
            self.streamCheckboxes.append(stream_checkbox)

        # ########
        # form asking about assets of the school (ie classrooms and teachers)
        self.assetFormArea = QWidget(self)
        self.assetFormAreaLayout = QFormLayout(self.assetFormArea)
        self.classCountLabel = QLabel('6) No. of classrooms')
        self.classCountField = QLineEdit()  # input field 6
        self.classCountField.textChanged.connect(lambda: self.check_classes_field_validity())
        self.classCountField.setFixedWidth(70)
        self.teacherCountLabel = QLabel('7) No. of teachers')
        self.teacherCountField = QLineEdit()  # input field 7
        self.teacherCountField.textChanged.connect(lambda: self.check_teachers_field_validity())
        self.teacherCountField.setFixedWidth(70)
        self.assetFormAreaLayout.addRow(self.classCountLabel, self.classCountField)
        self.assetFormAreaLayout.addRow(self.teacherCountLabel, self.teacherCountField)

        # widget for timing form
        self.timingInputArea = QWidget(self)
        self.timingInputAreaLayout = QFormLayout(self.timingInputArea)
        self.shiftLabel = QLabel('8) Total Shifts')
        self.shiftField = QComboBox(self.timingInputArea)  # input field 8
        self.shiftField.addItems(["Select", "1", "2", "3", "4"])
        self.shiftField.currentIndexChanged.connect(lambda: self.check_shifts_field_validity())
        self.shiftField.setFixedWidth(70)
        self.schoolHoursLabel = QLabel('9) School hours')

        # widget for storing 2 input fields (for start timing and end timing) into single row
        self.startEndFields = QWidget(self.timingInputArea)
        self.startEndFieldsLayout = QHBoxLayout(self.startEndFields)
        self.schoolStartTimeField = QTimeEdit()  # input field 9 (a)
        self.schoolStartTimeField.timeChanged.connect(lambda: self.check_school_hours_field_validity())
        self.schoolStartTimeField.setFixedWidth(100)
        self.schoolEndTimeField = QTimeEdit()  # input field 9 (b)
        self.schoolEndTimeField.timeChanged.connect(lambda: self.check_school_hours_field_validity())
        self.schoolEndTimeField.setFixedWidth(100)
        self.startEndFieldsLayout.addWidget(self.schoolStartTimeField)
        self.startEndFieldsLayout.addWidget(QLabel(' to '))
        self.startEndFieldsLayout.addWidget(self.schoolEndTimeField)
        self.startEndFieldsLayout.addStretch(1)

        # adding widgets to timing form layout
        self.timingInputAreaLayout.addRow(self.shiftLabel, self.shiftField)
        self.timingInputAreaLayout.addRow(self.schoolHoursLabel, self.startEndFields)

        # widgets for placing checkboxes for working days
        self.workingDaysCheckboxArea = QWidget(self)
        self.workingDaysCheckboxAreaLayout = QHBoxLayout(self.workingDaysCheckboxArea)
        self.daysList = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # generating checkboxes...
        for index in range(len(self.daysList)):             # input field 10
            day_checkbox = self.create_working_days_checkbox_for(index, self.daysList[index])
            self.workingDaysCheckboxes.append(day_checkbox)

        # adding all widgets into main layout
        self.mainLayout.addRow(self.schoolNameLabel, self.schoolNameField)
        self.mainLayout.addRow(self.schoolAddressLabel, self.schoolAddressFieldPart1)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart2)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart3)
        self.mainLayout.addRow(self.boardLabel, self.boardField)
        self.mainLayout.addRow(self.educationLevelLabel, self.educationLevelField)
        self.mainLayout.addRow(self.streamLabel, self.streamsInputArea)
        self.mainLayout.addRow(self.assetFormArea, self.timingInputArea)
        self.mainLayout.addRow(self.workingDaysLabel, self.workingDaysCheckboxArea)
        self.mainLayout.setContentsMargins(10, 20, 0, 0)
        self.setLayout(self.mainLayout)

        # calling validation functions for each field at initial stage
        self.check_if_all_valid()
    # ####################################################################
    # ##################### GUI ENDS HERE ###################################
    # ####################################################################

    # ####################################################################
    # ############ GUI COMPONENTS CREATING FUNCTIONS STARTS HERE #############
    # ####################################################################

    # function which generates the stream options checkboxes
    def generate_stream_options_for(self, checkbox_index, stream_value):
        stream_option_checkbox = QCheckBox(stream_value)
        stream_option_checkbox.toggled.connect(lambda: self.process_stream_checkbox(checkbox_index))
        self.streamsInputAreaLayout.addWidget(stream_option_checkbox)
        return stream_option_checkbox

    # function to create checkboxes for working days
    def create_working_days_checkbox_for(self, checkbox_index, checkbox_value):
        working_day_checkbox = QCheckBox(checkbox_value)
        working_day_checkbox.toggled.connect(lambda: self.process_working_days_checkbox(checkbox_index))
        self.workingDaysCheckboxAreaLayout.addWidget(working_day_checkbox)
        return working_day_checkbox

    # ####################################################################
    # ############# GUI COMPONENTS CREATING FUNCTIONS ENDS HERE ##############
    # ####################################################################

    # ####################################################################
    # ############## INPUT FIELDS VALIDATING FUNCTIONS STARTS HERE ##############
    # ####################################################################

    """ 
    Function definitions for each input field for its respective validation. 
    These functions make use of following one or more "helper functions":
    
    [Function available in Global/Functions/independent_functions.py file]
      *     check_if_pure_string()
      *     check_if_alpha_numeric()
      *     check_if_special_string()
      *     check_if_numeric()
      
      [Functions available in current class]
      *     add_validity()
      *     remove_validity()    
    """
    # function to validate "school name" input field (ie FIELD 1)
    def check_name_field_validity(self):
        # number of "name" input field => 1
        valid_input = check_if_pure_string(self.schoolNameField.text())
        if valid_input:
            self.add_validity(self.InvalidInputFields, 1)
            self.add_validity(self.ignoredWarnings, 1)
            self.update_warnings(1, True)
        else:
            self.remove_validity(self.InvalidInputFields, 1)
            self.remove_validity(self.ignoredWarnings, 1)
            self.update_warnings(1, False)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "school address" input field (ie FIELD 2)
    def check_address_field_validity(self):
        # number of "address" input field => 2

        # validation of address (ie field 2, part 1 only)
        address_valid = check_if_special_string(self.schoolAddressFieldPart1.text())

        # validation for part2 and part3 of address; checked only if they have non empty strings
        if self.schoolAddressFieldPart2.text() != "":
            part2_valid = check_if_special_string(self.schoolAddressFieldPart2.text())
            address_valid = address_valid and part2_valid
        if self.schoolAddressFieldPart3.text() != "":
            part3_valid = check_if_special_string(self.schoolAddressFieldPart3.text())
            address_valid = address_valid and part3_valid

        if address_valid:
            self.add_validity(self.InvalidInputFields, 2)
            self.add_validity(self.ignoredWarnings, 2)
            self.update_warnings(2, True)
        else:
            self.remove_validity(self.InvalidInputFields, 2)
            self.remove_validity(self.ignoredWarnings, 2)
            self.update_warnings(2, False)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "board" input field (ie FIELD 3)
    def check_board_field_validity(self):
        # number of "board" input field => 3
        self.validate_combobox(self.boardField, 3)

    # function to validate "eduction level" input field (ie FIELD 4)
    def check_education_level_field_validity(self):
        # number of "board" input field => 4
        self.validate_combobox(self.educationLevelField, 4)

    # function to validate "stream offered" input field (ie FIELD 5)
    def check_stream_field_validity(self):
        # number of "stream offered" input field => 5
        # checking if at least one of the streams is selected
        if len(self.streamSelected) == 0:
            self.remove_validity(self.InvalidInputFields, 5)
            self.remove_validity(self.ignoredWarnings, 5)
            self.update_warnings(5, False)
        else:
            self.add_validity(self.InvalidInputFields, 5)
            self.add_validity(self.ignoredWarnings, 5)
            self.update_warnings(5, True)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "No. of class rooms" input field (ie FIELD 6)
    def check_classes_field_validity(self):
        # number of "No. of class rooms" input field => 6
        # checking if number of classes is given and it is less than 70
        max_class_limit = 70
        total_classes = self.classCountField.text()
        # giving total classes a value of 0 if it is left blank
        if total_classes == "":
            self.remove_validity(self.InvalidInputFields, 6)
            self.remove_validity(self.ignoredWarnings, 6)
            self.update_warnings(6, False)
        else:
            valid_class_input = check_if_numeric(str(total_classes))
            if valid_class_input and (max_class_limit >= int(total_classes) > 0):
                self.add_validity(self.InvalidInputFields, 6)
                self.add_validity(self.ignoredWarnings, 6)
                self.update_warnings(6, True)
            else:
                self.remove_validity(self.InvalidInputFields, 6)
                self.remove_validity(self.ignoredWarnings, 6)
                # self.send_warning_to_prompt_area_for(6)
                self.update_warnings(6, False)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "No. of teachers" input field (ie FIELD 7)
    def check_teachers_field_validity(self):
        # number of "No. of teachers" input field => 7
        # checking if number of teachers is given and it is less than 70
        max_teacher_limit = 70
        total_teachers = self.teacherCountField.text()
        # giving total teachers a value of 0 if it is left blank
        if total_teachers == "":
            self.remove_validity(self.InvalidInputFields, 7)
            self.remove_validity(self.ignoredWarnings, 7)
            self.update_warnings(7, False)
        else:
            valid_teacher_input = check_if_numeric(str(total_teachers))
            if valid_teacher_input and (max_teacher_limit >= int(total_teachers) > 0):
                self.add_validity(self.InvalidInputFields, 7)
                self.add_validity(self.ignoredWarnings, 7)
                self.update_warnings(7, True)
            else:
                self.remove_validity(self.InvalidInputFields, 7)
                self.remove_validity(self.ignoredWarnings, 7)
                self.update_warnings(7, False)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "Total Shifts" input field (ie FIELD 8)
    def check_shifts_field_validity(self):
        # number of "shifts" input field => 8
        # checking if any no of shift is selected or not
        self.validate_combobox(self.shiftField, 8)

    # function to validate "School Hours" input field (ie FIELD 9)
    def check_school_hours_field_validity(self):
        start_time = self.schoolStartTimeField.text()
        end_time = self.schoolEndTimeField.text()

        if start_time == end_time:
            self.remove_validity(self.InvalidInputFields, 9)
            self.remove_validity(self.ignoredWarnings, 9)
            self.update_warnings(9, False)
        else:
            self.add_validity(self.InvalidInputFields, 9)
            self.add_validity(self.ignoredWarnings, 9)
            self.update_warnings(9, True)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to validate "Operates on" input field (ie FIELD 10)
    def check_working_days_field_validity(self):
        # number of "Operates on" input field => 10
        # checking if at least one of the days is selected
        if len(self.daysSelected) == 0:
            self.remove_validity(self.InvalidInputFields, 10)
            self.remove_validity(self.ignoredWarnings, 10)
            self.update_warnings(10, False)
        else:
            self.add_validity(self.InvalidInputFields, 10)
            self.add_validity(self.ignoredWarnings, 10)
            self.update_warnings(10, True)

        # updating status of "next" button accordingly
        self.check_next_button_validity()

    # function to check validity of all field. To be called only once at the beginning
    def check_if_all_valid(self):
        self.check_name_field_validity()
        self.check_address_field_validity()
        self.check_board_field_validity()
        self.check_education_level_field_validity()
        self.check_stream_field_validity()
        self.check_classes_field_validity()
        self.check_teachers_field_validity()
        self.check_shifts_field_validity()
        self.check_school_hours_field_validity()
        self.check_working_days_field_validity()

        # hiding any warning message generated before even giving any input
        self.footerWidgetRef.hide_warning()
        self.ignoredWarnings = []   # resetting the list
        print(f"Warnings have been reset. ({len(self.ignoredWarnings)})")

    # function for checking if all required fields have been validated
    def check_next_button_validity(self):
        # if all fields are valid, size of "InvalidInputFields" will be 0, which would, then enable the next button
        if len(self.InvalidInputFields) == 0:
            self.footerWidgetRef.nextButton.setEnabled(True)
        else:
            self.footerWidgetRef.nextButton.setEnabled(False)

    # ####################################################################
    # ############## INPUT FIELDS VALIDATING FUNCTIONS ENDS HERE ###############
    # ####################################################################

    # process working days checkboxes on toggling
    def process_working_days_checkbox(self, checkbox_index):
        if self.workingDaysCheckboxes[checkbox_index].isChecked():
            self.daysSelected.append(self.daysList[checkbox_index])
        else:
            self.daysSelected.remove(self.daysList[checkbox_index])

        # validating the field after processing
        self.check_working_days_field_validity()

    # process working days checkboxes on toggling
    def process_stream_checkbox(self, checkbox_index):
        if self.streamCheckboxes[checkbox_index].isChecked():
            self.streamSelected.append(self.streams[checkbox_index])
        else:
            self.streamSelected.remove(self.streams[checkbox_index])

        # validating the field after some option is selected
        self.check_stream_field_validity()

    # function to check if any option (from the drop-down) is selected or not
    def validate_combobox(self, combobox, field_number):
        combobox_index = combobox.currentIndex()

        # checking if 1st option is selected; 1st option is not a real option (like "-- select --", "choose one" etc)
        if combobox_index == 0:
            self.remove_validity(self.InvalidInputFields, field_number)
            self.remove_validity(self.ignoredWarnings, field_number)
            self.update_warnings(field_number, False)
        else:
            self.add_validity(self.InvalidInputFields, field_number)
            self.add_validity(self.ignoredWarnings, field_number)
            self.update_warnings(field_number, True)

        # function added later, to re-check all fields validity and enable/disable "next" button accordingly
        if len(self.InvalidInputFields) == 0:
            self.footerWidgetRef.nextButton.setEnabled(True)
        else:
            self.footerWidgetRef.nextButton.setEnabled(False)

    # function to display updated warnings after some input (either wrong or right)
    def update_warnings(self, current_field_no, field_validity_status):
        # following will be used to put correct field name in warning at run time.
        fields_name = [
            "Name", "Address", "Board", "Education", "Stream", "Classes", "Teachers", "Shift", "Time", "Days"
        ]
        # debugging
        print(f"called by {fields_name[current_field_no - 1]}")
        print(f"current value of no. of warnings: {len(self.ignoredWarnings)}")

        if len(self.ignoredWarnings) > 1:
            print(f"\nIF CASE: total warnings = {len(self.ignoredWarnings)}")
            warning_to_send = f"" \
                f"[Multiple warnings] " \
                f"Invalid {fields_name[current_field_no - 1]} field " \
                f"and {len(self.ignoredWarnings) - 1} more fields. "

            self.footerWidgetRef.show_warning(warning_to_send)
        elif len(self.ignoredWarnings) == 1:
            print(f"ELIF CASE: total warnings = {len(self.ignoredWarnings)}")
            if field_validity_status:
                # getting 1st invalid field (from ignoredWarnings)
                new_field_no = self.ignoredWarnings[0]
                self.send_warning_to_prompt_area_for(new_field_no)
            else:
                self.send_warning_to_prompt_area_for(current_field_no)

        else:       # len(self.ignoredWarnings) == 0
            print(f"ELSE CASE: total warnings = {len(self.ignoredWarnings)}")
            self.footerWidgetRef.hide_warning()

    @staticmethod
    # mark given field as invalid
    def remove_validity(the_list, field_number):
        if not index_exists_in(the_list, field_number):
            the_list.append(field_number)

    @staticmethod
    # mark given field as valid
    def add_validity(the_list, field_number):
        if index_exists_in(the_list, field_number):
            the_list.remove(field_number)

    # function to send suitable waring message to Settings_Footer's prompt area
    def send_warning_to_prompt_area_for(self, field_no):
        print(f"\nNo. of Warnings: {len(self.ignoredWarnings)}")
        warning_to_send = self.warningMessages[f"{field_no}"]
        self.footerWidgetRef.show_warning(warning_to_send)

    # store information into the database (called upon clicking of "next" button)
    def initialize_school_configurations(self):
        school_name = self.schoolNameField.text()
        address_line1 = self.schoolAddressFieldPart1.text()
        address_line2 = self.schoolAddressFieldPart2.text()
        address_line3 = self.schoolAddressFieldPart3.text()
        school_address = f'{address_line1} \n {address_line2} \n {address_line3}'
        board_name = self.boardField.currentText()
        education_level = self.educationLevelField.currentText()
        no_of_shifts = self.shiftField.currentText()
        total_classes = self.classCountField.text()
        total_teachers = self.teacherCountField.text()
        start_timing = self.schoolStartTimeField.text()
        end_timing = self.schoolEndTimeField.text()

        print(f'Opted values are as follow:'
              f'School Name: {school_name}\n'
              f'School Address: {school_address}\n'
              f'board Name: {board_name}\n'
              f'Education Level: {education_level}\n'
              f'Streams available: {self.streamSelected}\n'
              f'Working Days: {self.daysSelected}\n'
              f'No. of Classes: {total_classes}\n'
              f'No. of teacher: {total_teachers}\n'
              f'No. of Shifts: {no_of_shifts}\n'
              f'Timings: From {start_timing} to {end_timing}')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    basic_info_window_object = SchoolInfoForm()
    basic_info_window_object.show()
    sys.exit(application.exec_())
