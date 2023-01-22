# CSE 310-04 Applied Programming - Jeremiah Pineda
# W03 Module 1 CloudDB
# Scott LeFoll
#01/20/23

"""This module contains functions that interact with the Cloud Firestore database.
    The functions in this module are used to authenticate the credentials, and then to 
    read, update, and delete documents in the sample student NoSQL database 
    (CSE310 Cloud DB Module 1). The functions in this module are used to demonstrate
    authentication and the basic CRUD operations in Cloud Firestore.
    
    The following functionality is implemented:
    
    authenticate user - authenticates the user with the credentials
    update application data when database changes - updates the application data when the database changes
    
    retrieve all records - retrieves and displays all documents in the collection (students)
    display a record - searches and displays a specific document in the collection
    create a record - creates a new document in the collection
    delete a record - deletes a document from the collection
    update a field - updates a document in the collection
    delete an index - deletes an index from a document in the collection
    create an index - creates an index in a document in the collection
    
    The functionality for the following operations is not fully implemented yet:
    
    delete multiple records - deletes multiple documents from the collection based on a search criteria
    
"""

import firebase_admin
import datetime
import requests
import pprint
import functions_framework

from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
from google.cloud import storage
from google.cloud.firestore_v1 import ArrayRemove, ArrayUnion
from google.cloud.firestore_v1 import DELETE_FIELD
from google.cloud.firestore_v1 import DocumentReference
from google.cloud.firestore_v1 import DocumentSnapshot

# load the credentials from the JSON file
cred = credentials.Certificate('cse310-cloud-db-module-1-firebase-adminsdk-nb5nk-b1bd873598.json')
# initialize the app with the credentials
default_app = firebase_admin.initialize_app(cred)
# initialize the firestore client
db = firestore.client()


# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def hello_gcs(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {name}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")
    
    
def display_record(name_str):
    """Reads a document from the collection.
    
    Args: name_str (str): the student name in the document to read

    Returns:
        string: the document
    """

    # get the document from the collection    
    doc = db.collection('students').document(name_str).get()
    print()
    pprint.pprint(doc.to_dict())
    print()
    return doc.to_dict()


def read_collection():
    """Reads a collection from the database.
    
    Returns:
    
    """
    # get the collection from the database
    docs = db.collection('students').where('type', '==', 'undergrad').stream()
    print()
    for doc in docs:
        student = doc.to_dict()
        pprint.pprint(student)

        
def update_field(name_str, field_str, value_str):
    """Updates the graduation year of a student.
    Args:   name_str (str): the student name in the document to read
            field_str (str): the field to update
            value_str (str): the value to update the field with
    
    """
    
    # update a single field value in the specified student record
    doc_ref = db.collection('students').document(name_str).update({ field_str: value_str })


def remove_index(name_str, field_str):
    """ Removes the classes index from the student's indices.
        Args:   name_str (str): the student name in the document to read
                field_str (str): the field to remove the index from
    
    """    
    # remove the last_name index from the student's indices
    doc_ref = db.collection('students').document(name_str).update({'indices': firestore.ArrayRemove([field_str])})


def add_index(name_str, field_str):
    """ Adds the classes index to the student's indices.
        Args:   name_str (str): the student name in the document to read
                field_str (str): the field to add the index to
    """    
    # add the last_name index to the student's indices
    doc_ref = db.collection('students').document(name_str).update({'indices': firestore.ArrayUnion([field_str])})
    

def delete_document(name_str):
    """ Deletes a document from the collection.

    Args:
        name_str (str): the student record to delete
    """    
    # remove a Student Record from the collection
    db.collection('students').document(name_str).delete()


def delete_field(name_str, field_str):
    """ Deletes a field from a document.

    Args:   name_str (str): the student record to delete a field in
            field_str (str): the field to delete
    """    
    # load the document
    doc_ref = db.collection('students').document(name_str)
    # delete the specified Field from the Student Record
    doc_ref.update({
        field_str: firestore.DELETE_FIELD
    })


# def delete_multiple(field_str, value_str):
#     """ Deletes multiple Student Records based on a field condition.

#     Args:   field_str (str): the field search in to delete the records
#             value_str (str): the value to search for in the field
    
#     """
    
#     docs = db.collection('students').where(field_str, '==', value_str).stream()
#     for doc in docs:
#         doc.delete()
        
    # load the document
    # doc_ref = db.collection('students').document(name_str)
    # delete the specified Field from the Student Record
    # doc_ref.update({
    #     field_str: firestore.DELETE_FIELD
    # })
    
    
def add_document(name_str):
    """Adds a new Student Record.
    Args:   name_str (str): the student name in the document to read
    
    """    
    f_name = name_str[:name_str.find("_")].title()
    l_name = name_str[name_str.find("_")+1:].title()
    
    # add a single Student Record to the document database
    db.collection("students").document(name_str).set({
        'last_name': l_name,
        'first_name': f_name
    }, merge=True)
    

def menu_input():
    """Displays a menu and asks the user for a menu choice.
    """
    while True:
        # Ask the user for a menu choice.
        print()
        print()
        print("CSE 310 Module 1: CloudDB Menu:")
        print()
        print("0. Display a single Student Record")
        print("1. Display a collection of Student Records")
        print("2. Update a field in a Student Record")
        print("3. Remove the index from a field in a Student Record")
        print("4. Add an an index to field in a Student Record")
        print("5. Delete a Student Record")
        print("6. Delete a field from a Student Record")
        print("7. Add a field to a Student Record")
        print("8. Add a new Student Record")
        print("9. Delete multiple Student Records using a field condition")
        print("hit 'Enter' to exit")
        print()
        print()

        choice_str = input("Please enter a menu choice (0 - 9): ")
        if choice_str == "":
            # if the user hits 'Enter', then exit the program
            print("Exiting the program")
            exit()
        
        try:
            # try to convert the user input to int.
            choice_int = int(choice_str)
            if choice_int < 0 or choice_int > 9:
                # if the input is not in the range 0 - 9, then go back to input
                print("Please enter a valid menu choice (0 - 9)")
                continue
            else:
                # if the input is in the range 0 - 9, then execute the corresponding function
                match choice_int:
                    case 0:
                        # display a single student record
                        print()
                        student_str = input("Please enter the name of the Student Record to display (ie. jim_smith): ").lower().replace(" ", "_")                        
                        display_record(student_str)
                    case 1:
                        # display a collection of student records
                        read_collection()
                    case 2:
                        # update a field from a student record
                        print()
                        student_str = input("Please enter the name of the Student Record to update (ie. jim_smith): ").lower().replace(" ", "_")                        
                        print()
                        field_str = input("Please enter the name of the Field update (ie. grad_year): ").lower().replace(" ", "_")                        
                        print()
                        value_str = input("Please enter the value to update the Field with (ie. 2023): ")
                        update_field(student_str, field_str, value_str)
                        display_record(student_str)                    
                    case 3:
                        # remove the last_name index from a student's record
                        print()
                        student_str = input("Please enter the name of a Student Record to remove an index from (ie. jim_smith): ").lower().replace(" ", "_")
                        print()                        
                        field_str = input("Please enter the name of the Field index to remove(ie. grad_year): ").lower().replace(" ", "_")                        
                        remove_index(student_str, field_str)
                        display_record(student_str)
                    case 4:
                        # add an index to a student's record
                        print()
                        student_str = input("Please enter the name of a Student Record to add an index to (ie. jim_smith): ").lower().replace(" ", "_")                        
                        print()                        
                        field_str = input("Please enter the name of the Field to add an index on(ie. grad_year): ").lower().replace(" ", "_")                        
                        add_index(student_str, field_str)
                        display_record(student_str)
                    case 5:
                        # delete a student's record
                        print()
                        student_str = input("Please enter the name of a Student Record to delete (ie. jim_smith): ").lower().replace(" ", "_")                        
                        delete_document(student_str)
                        read_collection()
                    case 6:
                        # delete a field from a student's record
                        print()
                        student_str = input("Please enter the name of the Student Record to delete a field from (ie. jim_smith): ").lower().replace(" ", "_")                        
                        print()
                        field_str = input("Please enter the name of the Field to delete (ie. grad_year): ").lower().replace(" ", "_")                                                
                        delete_field(student_str, field_str)
                        display_record(student_str)
                    case 7:
                        # add a field to a student record
                        print()
                        student_str = input("Please enter the name of the Student Record to add a field to (ie. jim_smith): ").lower().replace(" ", "_")                        
                        print()
                        field_str = input("Please enter the name of the Field to add (ie. grad_year): ").lower().replace(" ", "_")                        
                        print()
                        value_str = input("Please enter the value to update the new Field with (ie. 2023): ")
                        update_field(student_str, field_str, value_str)
                        display_record(student_str)                    
                    case 8:
                        # add a new student record
                        print()
                        student_str = input("Please enter the name of the Student Record to add (ie. jim_smith): ").lower().replace(" ", "_")     
                        # Add a new document in collection "students"
                        add_document(student_str)
                        display_record(student_str)
                        
                        while True:
                            # add a field to a student record
                            print()
                            field_str = input("Please enter the name of the Field to add, or hit 'Enter' if done (ie. grad_year): ").lower().replace(" ", "_")                        
                            if field_str == "":
                                break
                            
                            print()
                            value_str = input("Please enter the value to update the new Field with (ie. 2023): ")
                            update_field(student_str, field_str, value_str)
                            display_record(student_str)
                            
                    case 9:
                        # delete multiple Student Records using a Category
                        print()
                        field_str = input("Please enter the Field to search in for the deletion (ie. jim_smith): ").lower()
                        print()
                        value_str = input("Please enter the Value to search in the Field for the deletion (ie. 2023): ")
                        # delete_multiple(field_str, value_str)
                        read_collection()
                    case _:
                        # exit the program
                        exit()
                        
                continue 
            
        except ValueError:
            # if the int conversion throws an error, then go back to input
            print()
            print("Please enter a valid menu choice (0 - 9)")
            continue
        
print()
print()
print("CSE 310 Module 1: CloudDB Student Records")   
read_collection()

menu_input()



