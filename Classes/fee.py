"""
This file is for the basic structure of the fee of a student. It also consist functions to process fee info like
calculating due date for late fee, storing and updating fee structure in DB etc.
A student may require several instance of this class during a specific course of time.
"""

from Database.database_connection import *
from Database.school_database_variables import *
from Global.Functions.independent_functions import convert_datetime_to_number_string
import datetime


class Fee:
    def __int__(
            self, std_id=None, period=None, adm_fee=0, re_adm_fee=0, tuition_fee=0, late_fee=0,
            vvn=0, comp_fee=0, project_fee=0, other_fee=0
            ):
        self.forStudent = std_id
        self.forPeriod = period
        self.admissionFee = adm_fee
        self.reAdmissionFee = re_adm_fee
        self.tuitionFee = tuition_fee
        self.lateFee = late_fee
        self.VVN = vvn                  # vidyalaya vikas nidhi
        self.projectFee = project_fee
        self.otherFee = other_fee
        # following fee receipt ID will be added to student record, after the fee is submitted successfully
        self.feeReceiptID = self.generate_fee_id()
        self.bankTransactionID = None            # fee submission will be completed only if this value gets updated

    # used to generate an ID for the fee receipt
    def generate_fee_id(self):
        if self.forStudent is None:
            print("[Error] No student ID given for the fee. \n Exiting...")
            exit(1)
        else:
            date = datetime.datetime.now()
            timestamp_as_string = convert_datetime_to_number_string(date)
            fee_id = self.forStudent + timestamp_as_string
            return fee_id

