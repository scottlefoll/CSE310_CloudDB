# Implementation of Cloud Datbase Funtionality using Google Firestore and Python

### CSE 310-04 Applied Programming - Jeremiah Pineda
### W03 Module 1 CloudDB
## Scott LeFoll
## 01/20/23
## Created by Scott LeFoll

## Module 1 Overview

The software uses an authentication token provided by Google Cloud to establish a secure connection 
to the Firebase and the Firestore Database. This connection is then used to implement CRUD 
functions. The objective is to gain initial experience with a cloud No SQL database, and 
understanding of the implementation in Google Cloud specifically. The ultimate goal is to integrate
this functionality into desktop and web applications in the future.

There is a basic on-screen menu that provided simple user prompts, and captures input that is 
used to feed the database operations. There is basic validation provided on the user input.

This application is provided for the following purpose:

To demonstrate a full range of basic database functionality in using the Cloud Firestore 
    database. The functions in this module are used to authenticate the credentials, and then 
    create, read, update, and delete documents in the student NoSQL database 
    (CSE310 Cloud DB Module 1). The functions in this module are used to demonstrate
    authentication and the basic CRUD operations in Cloud Firestore.
    
    The following functionality is implemented:
    
    authenticate user - authenticates the user with the credentials
    update application data when database changes - updates the application data when the 
    database changes
    
    retrieve all records - retrieves and displays all documents in the collection (students)
    display a record - searches and displays a specific document in the collection
    create a record - creates a new document in the collection
    delete a record - deletes a document from the collection
    update a record - updates a document in the collection
    delete an index - deletes an index from a document in the collection
    create an index - creates an index in a document in the collection

[Cloud Database Programming Demo Video](https://youtu.be/9vuWtdHKhhA)

[Cloud Database Programming Git Hub repo](https://github.com/scottlefoll/CSE310_CloudDB)


## Cloud Database

This application is using the Google Cloud Firestore Database

The database for this application has the following structure:

students:

    student_id
    last_name
    first_name
    dob: timestamp
    cat
    type: "undergrad"
    major
    height_inches
    weight_lbs
    street_address
    street_address2
    town
    state
    zip

classes:

    course_code
    course_title
    course_dept
    credits
    description
    prereqs

registrations:

    course_id
    semester
    student_id
    year



## Development Environment

The development environment for this application is:

Windows 10 Profesional
Python 3.11.1
VS Code 1.74.3

The dependencies for the application are:

firebase_admin
datetime
requests
pprint
functions_framework
google_cloud


# Useful Websites

The following websites were used in the research for this application:

- [Web Site Name](https://javascript.plainenglish.io/firebase-cloud-functions-tutorial-creating-a-rest-api-8cbc51479f80)
- [Web Site Name](https://javascript.plainenglish.io/firebase-cloud-functions-tutorial-firestore-trigger-functions-90bb3c3f9ea8)
- [Web Site Name](https://itnext.io/cloud-functions-firestore-triggers-d6fa30169ec8)
- [Web Site Name](https://stackoverflow.com/questions/57570202/universal-firestore-trigger-for-all-documents)
- [Web Site Name](https://cloud.google.com/functions/docs/tutorials/storage#functions-clone-sample-repository-python)
- [Web Site Name](https://medium.com/google-cloud/setup-and-invoke-cloud-functions-using-python-e801a8633096)
- [Web Site Name](https://pypi.org/project/python-firebase/)
- [Web Site Name](https://cloud.google.com/docs/authentication/application-default-credentials)
- [Web Site Name](https://cloud.google.com/sdk/docs/)
- [Web Site Name](https://saveyourtime.medium.com/firebase-cloud-firestore-add-set-update-delete-get-data-6da566513b1b)
- [Web Site Name](https://clemfournier.medium.com/make-crud-operations-on-firebase-firestore-in-python-d51ab6aa98af)
- [Web Site Name](https://towardsdatascience.com/essentials-for-working-with-firestore-in-python-372f859851f7)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

As I move forward with my Cloud Database learning, I would like to enhance this application with the following:
    
    Google Cloud - finish implementing the multi-record delete function
    
    Improve the Google Cloud triggers
    
    Implement the application in at least one other Cloud Database
