# 	Author: Vince Verdadero (19009246)
#   Created: 06 / 04 / 21
#   Last edited: 13/ 04 / 21
#   Description: A program to automate the selection
#                create a ranking in terms of the order of priority that patients should be referred to a dietitian.
#  	This program will:
#  	Calculate the BMI for each patient and classify the patients as underweight,normal,overweight or obese.
#   Display the patients name, age, build, BMI and weight classification
#   Sort the output as obese shown at the top of screen, followed by underweight, then overweight then normal.
#   Display the worst 5 underweight and the worst 5 obese patients in two groupings,make and female.
#  	User advice: None

# These imports are used to read the csv file and used for the date from the file
import csv
import datetime
from datetime import date


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
        return self.Patient_name  # get the patient's name

    def get_patients_age(self):
        return self.patients_age  # get patient's age

    def get_patients_bmi(self):
        return self.patients_BMI  # get patient's BMI

    def get_weight_class(self):
        return self.class_of_patients_weight  # get the weight class of patient

    class_of_patients_weight = ""


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

            # This will append the patient to the list of patients
            List_of_patient.append(patient)

    patientData.close()  # close the patients data
    return List_of_patient  # Returns the the list of patients


# Def function to print out the patient for the output

def patient_fields_task1(patient):
    print("Patient's name:", patient.Patient_name, "||", " Patient's age: ", patient.patients_age, "||",
          " Patient's build: ", patient.build_of_patient, "||", " Patient's BMI:", patient.patients_BMI, "||",
          "Patient's weight class:", patient.class_of_patients_weight)


# This is a def function to illustrate the order of patients by weight class with a line break of every 10 patients

def order_of_weight_patients(obese_patients, underweight_patients, overweight_patients, normalweight_patients):
    # Patients should be listed as specification says in this order: obese, underweight, overweight, normal

    weight_counter = 0  # Counter to determine how many patients there are depending on weight

    print("Here is a list of patients and are classed by their significant weight")
    print("Every 10 patients are listed for you to examine, please look through this carefully!")
    input("Please press enter to proceed for task 1. \n")

    # For loop to determine how many patients are obese
    for patient in obese_patients:
        patient_fields_task1(patient)
        weight_counter += 1  # increment by 1 and will counted to 10
        if 0 == weight_counter % 10:
            print("\n")

    # For loop to determine how many patients are underweight
    for patient in underweight_patients:
        patient_fields_task1(patient)
        weight_counter += 1  # increment by 1 and will counted to 10
        if 0 == weight_counter % 10:
            print("\n")

    # For loop to determine how many patients are overweight
    for patient in overweight_patients:
        patient_fields_task1(patient)
        weight_counter += 1  # increment by 1 and will counted to 10
        if 0 == weight_counter % 10:
            print("\n")

    # For loop to determine how many patients are normal
    for patient in normalweight_patients:
        patient_fields_task1(patient)
        weight_counter += 1  # increment by 1 and will counted to 10
        if 0 == weight_counter % 10:
            print("\n")


# This is a def function to list the five worst underweight and obese patients

def list_five_worst_patients(underweight_patients, obese_patients):
    # From the CSV file given we can store these attributes as a lists and put these as subgroups from male and females
    under_weight_male_patients = []
    under_weight_female_patients = []
    obese_male_patients = []
    obese_female_patients = []

    # Here is a for loop to determine the Underweight patients whether male or female
    for patient in underweight_patients:
        if "M" == patient.Patient_sex:
            under_weight_male_patients.append(patient)
        else:
            under_weight_female_patients.append(patient)

    # Here is a for loop to determine the obese patients whether male or female
    for patient in obese_patients:
        if "M" == patient.Patient_sex:
            obese_male_patients.append(patient)
        else:
            obese_female_patients.append(patient)

    # Sorts out the subgroups by their BMI
    # The lambda expression is executed and the result is returned whether the subgroups is one of the worst patient
    # The reverse() method reverses the elements of the subgroup list.
    under_weight_male_patients.sort(key=lambda patient: patient.patients_BMI, reverse=True)
    under_weight_female_patients.sort(key=lambda patient: patient.patients_BMI, reverse=True)
    obese_male_patients.sort(key=lambda patient: patient.patients_BMI, reverse=True)
    obese_female_patients.sort(key=lambda patient: patient.patients_BMI, reverse=True)

    # Here are print statements that list the worst 5 patients on underweight and obese

    input("Please press enter to display the worse underweight male patients \n")

    print("Worst underweight male patients: \n")
    for weight in under_weight_male_patients:
        patient_fields_task1(weight)
    print("\n")

    input("Please press enter to display the worse underweight female patients \n")

    print("Worst underweight female patients: \n")
    for weight in under_weight_female_patients:
        patient_fields_task1(weight)
    print("\n")

    input("Please press enter to display the worse obese male patients \n")

    print("Worst obese male patients: \n")
    for weight in obese_male_patients:
        patient_fields_task1(weight)
    print("\n")

    input("Please press enter to display the worse obese female patients \n")

    print("Worst obese female patients: \n")
    for weight in obese_female_patients:
        patient_fields_task1(weight)
    print("\n")


# This def function will read the csv file into patient objects and categorise them into arrays
def categorising_weight_of_patients():

    # From the CSV file given we can store these attributes as a lists
    underweight_patients = []
    normalweight_patients = []
    overweight_patients = []
    obese_patients = []

    # Call read_csv to create a list data structure containing objects of the patient class
    patient_list = read_csv()

    # Patients categorised into subsets by the patient's weight class
    for patient in patient_list:
        set_class_weight_of_patient(patient)
        if "Underweight" == patient.class_of_patients_weight:
            underweight_patients.append(patient)
        elif "Normal" == patient.class_of_patients_weight:
            normalweight_patients.append(patient)
        elif "Overweight" == patient.class_of_patients_weight:
            overweight_patients.append(patient)
        elif "Obese" == patient.class_of_patients_weight:
            obese_patients.append(patient)

    order_of_weight_patients(obese_patients, underweight_patients, overweight_patients, normalweight_patients)
    list_five_worst_patients(underweight_patients, obese_patients)


# Task 1 execution
categorising_weight_of_patients()
