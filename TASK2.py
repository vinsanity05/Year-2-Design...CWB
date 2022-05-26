# Author: Vince Verdadero (19009246)
# Created: 09 / 04 / 21
# Last edited: 14 / 04 / 21
# Description: A program to automate the selection
#              Create a ranking in terms of the order of priority that patients should be referred to a dietitian.
# This program will: Establish which patients need to be referred to a dietitian
#                    Rank the order of priority according the rules given from specification
#                    Display patient names of those that need to be referred to a dietitian
#                    Insert breaks every 10 patients to allow the user of the system to study the results
# User advice: None

# These imports are used to read the csv file and used for the date from the file
import csv
import datetime
from datetime import date

print("Here is a list of patients and are classed by top priority to low priority whether they need to be referred "
      "to dietitian")
print("Every 10 patients are listed for you to examine, please look through this carefully!")
input("Please press enter to proceed for task 2. \n")


# Here we have a patient class, this represents each patient in the file.
# All of the attributes will be stored for validation
class Patient:

    # constructor for the Patient class
    def __init__(self, patient_name, date_of_birth, sex, height_of_patient, weight_of_patient, build):
        self.calculateBMI = None
        self.Patient_name = patient_name  # will be stored as a string
        self.date_of_birth = date_of_birth  # will be stored as a string
        self.Patient_sex = sex  # will be stored as a string
        self.build_of_patient = build  # will be stored as a string

        self.height_of_patient = float(height_of_patient)  # Stored as a float
        self.weight_of_patient = int(weight_of_patient)  # Stored as an integer

        self.patients_BMI = self.weight_of_patient / (self.height_of_patient ** 2)  # this will calculate the BMI
        # from the  above attributes

        self.patients_age = calculate_patients_age(date_of_birth)  # Calculating the age according to date of birth

    # Here are getters and setters

    def get_patients_name(self):
        return self.Patient_name  # get the patients name

    def get_patients_age(self):
        return self.patients_age  # get patient's age

    def get_patients_bmi(self):
        return self.patients_BMI  # get patient's BMI

    def get_weight_class(self):
        return self.class_of_patients_weight  # get the weight class of patient

    # Here from the CSV file given we can store these attributes as a lists
    Smoker = []
    Asthmatic = []
    NJT_or_NGR = []
    Hypertension = []
    Renal_RT = []
    Ileostomy_or_Colostomy = []
    Parenteral_Nutrition = []

    class_of_patients_weight = ""
    topPriority = False


# In this def function, this will calculate the age by subtracting his/her DOB from today's date
def calculate_patients_age(date_of_birth):
    # This will be stored in a list containing in a patient object's date_of_birth attribute
    # Using The split() method will returns the patients date of birth
    # Then it will be separated by the delimiter string. This method will return one or more new strings.
    date_of_birth_List = date_of_birth.split("/")

    year = int(date_of_birth_List[0])  # This will separate of year into integer values
    month = int(date_of_birth_List[1])  # This will separate of month into integer values
    day = int(date_of_birth_List[2])  # This will separate of day into integer values

    # Patient date of birth stored in date variable
    date_of_birth = datetime.date(day, month, year)

    # Today's date stored to check dates of birth against
    date_of_today = date.today()
    # This will calculate the patients age from today's date and return
    return ((date_of_today - date_of_birth) / 365).days


# This is a def function to set the class weight of patients and to determine their BMI

def set_class_weight_of_patient(patient):
    if 18.5 > patient.patients_BMI:
        # This will class the Patient as underweight if BMI is under 18.5
        patient.class_of_patients_weight = "Underweight"

    elif 18.5 <= patient.patients_BMI <= 25:
        # This will class the Patient as normal if BMI is greater than or equal to 18.5 but less than or equal to 25
        patient.class_of_patients_weight = "Normal"

    if 25 < patient.patients_BMI <= 28:
        # This will class the Patient as overweight if BMI is greater than 25 but less than or equal to 28
        patient.class_of_patients_weight = "Overweight"

    elif patient.patients_BMI > 28:
        # This will class the Patient as obese if BMI is greater than 28
        patient.class_of_patients_weight = "Obese"


# This will read the csv file
# This will Read the data from the csv file and it delivers it to an array.
# This will organise it into patient objects.

def read_csv():
    List_of_patient = []

    with open("DADSA 2021 CWK B DATA COLLECTION.csv", newline='') as patientData:

        csv_reader = csv.reader(patientData)
        next(csv_reader)

        for row in csv_reader:  # This will iterate each patient from each row in the file

            # A new patient object is discovered and all data will be set by its constructor
            patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5])

            # This will get the information from the CSV file into a Patient object
            if row[6] != '':
                patient.Smoker = True
            if row[7] != '':
                patient.Asthmatic = True
            if row[8] != '':
                patient.NJT_or_NGR = True
            if row[9] != '':
                patient.Hypertension = True
            if row[10] != '':
                patient.Renal_RT = True
            if row[11] != '':
                patient.Ileostomy_or_Colostomy = True
            if row[12] != '':
                patient.Parenteral_Nutrition = True

            # This will append the patient to the list of patients
            List_of_patient.append(patient)

    patientData.close()  # close the patients data
    return List_of_patient  # Returns the the list of patients


# Def function to print out the patient for the output

def patient_fields_task2(patient):
    print("Patient's name:", patient.Patient_name, "||", " Patient's age: ", patient.patients_age, "||",
          " Patient's build: ", patient.build_of_patient, "||", " Patient's BMI:", patient.patients_BMI, "||",
          "Patient's weight class:", patient.class_of_patients_weight, "||", "Top priority:", patient.topPriority)


# This def function will calculate whether the patient needs to be referred or not

def refer_or_not(referral_list):
    refer_or_not_list = []

    for patient in referral_list:
        if (
                # uses DeMorgan's law to provide specific Boolean statements
                # which can be written in different ways for the same effect.
                not (not (
                        patient.class_of_patients_weight == "Obese" or patient.class_of_patients_weight ==
                        "Underweight")
                     and not (
                                patient.Hypertension
                                or patient.Asthmatic
                                or patient.Smoker
                                or patient.NJT_or_NGR
                                or patient.Renal_RT
                                or patient.Ileostomy_or_Colostomy
                                or patient.Parenteral_Nutrition))):
            refer_or_not_list.append(patient)

    return refer_or_not_list


# This def function will calculate who is priority

def calculating_who_is_priority(priority_list):
    for patient in priority_list:
        count = 0
        # uses DeMorgan's law to provide specific Boolean statements
        # which can be written in different ways for the same effect.
        if (not (not ((patient.Asthmatic or patient.Smoker)
                      and patient.patients_age > 55) and not (patient.class_of_patients_weight == "Obese "
                                                              and patient.Hypertension))):
            count += 3  # this will be counted if patients has all 3

        if patient.Smoker:
            count += 1  # Adds 1 to the counter if the patient is a smoker
        if patient.Asthmatic:
            count += 1  # Adds 1 to the counter if the patient is asthmatic
        if patient.NJT_or_NGR:
            count += 1  # Adds 1 to the counter if the patient has a condition of NJT or NGR
        if patient.Hypertension:
            count += 1  # Adds 1 to the counter if the patient has a condition of Hypertension
        if patient.Renal_RT:
            count += 1  # Adds 1 to the counter if the patient has a condition of Renal RT
        if patient.Ileostomy_or_Colostomy:
            count += 1  # Adds 1 to the counter if the patient has a condition of ileostomy or colostomy
        if patient.Parenteral_Nutrition:
            count += 1  # Adds 1 to the counter if the patient has a condition of parenteral nutrition
        if count > 3:
            patient.topPriority = True  # if patients has more than 3 conditions set it to be true

    # Return to priority list
    return priority_list


# This def function will output and show who is top priority or not

def top_priority_or_not():
    # Call read_csv to create a list data structure containing objects of the patient class
    patient_list = read_csv()

    for patient in patient_list:
        set_class_weight_of_patient(patient)

    # Here all all patients that are listed top priority
    # their topPriority attribute is assigned here
    patient_list = calculating_who_is_priority(patient_list)

    list_of_patient_who_is_top_priority = []

    for patient in patient_list:
        if patient.topPriority:
            # Remove from patient_List
            patient_list.remove(patient)
            # append to list of patient of patient who is top priority
            list_of_patient_who_is_top_priority.append(patient)

    # Sorts out the patient by their priority
    # The lambda expression is executed and the result is returned of the patients priority
    # The reverse() method reverses the elements of the patients list.
    patient_list.sort(reverse=True, key=lambda patient: patient.topPriority)
    list_of_patient_who_is_top_priority.sort(reverse=True, key=lambda patient: patient.topPriority)

    top_priority_list = list_of_patient_who_is_top_priority + patient_list

    count = 0
    for patient in top_priority_list:
        patient_fields_task2(patient)
        count += 1
        if count % 10 == 0:
            input("\n Please press enter to proceed for the next 10 patients. \n")


# Task 2 execution
top_priority_or_not()
