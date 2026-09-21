Part B)
Stakeholders
1) Staff: manage the apointments and look up patient information
2) Practitioners: provide patient care and use patient and appointment records
3) Management: oversees the clinic
4) Patients: Have their personal and appointment information stored in the system
Scope
Inscope)
Store and manage patient information 
Store and manage practitioner information 
Store and manage appointment information
Provide a system which replaces spreadsheets and paper records
Allow staff to find patient information more easily
Prevent duplicate appointments
Provide a appointment history so previous appointments can be viewed 
Allow staff to update appointment information
Control access point to patient information
Out of scope)
Online patient booking 
Patient mobile app
Automated sms and email reminders
Online payments
Intergration with external medical sysetms 

Part C)
Fr-01: The system shall allow staff to create a patient record
Fr-02: The system shall allow staff to view patient information
Fr-03: The system shall allow staff to create a practitioner record
Fr-04: The system shall allow staff to view practitioner information
Fr-05: The system shall allow staff to create an appointment for a patient with a practitioner
Fr-06: The system shall prevent two appointments being booked at the same time with the same practitioner 
Fr-07: The system shall allow staff to view appointment details, including the patient, practitioner, date, time and appointment status.
Fr-08: The system shall allow staff to update an appointment's status using the status values defined by the system.
Fr-09: The system shall record each appointment in the patient's appointment history

Part D)
NRF-01: The system shall display a requested patient, practitioner or appointment record within 2 seconds
NRF-02: The system shall require to log in before they can access their information
NRF-03: The system shall prevent unauthorised users from modifying patient, practitioner or appointment records
NRF-04: The system shall maintain consistent appointment status information so that an appointment only has one current status at a time
NRF-05: The system shall preserve stored patient, practitioner and appointment records when the system is closed and reopened.

Part E)
User Story 1 - Finding Patient information
Story: As a staff member, I want to search for an view a patients appointment information, so that I can find the correct information needed to manage the appointment 
Linked requirements: Fr-01, Fr-02, Fr-03
Scenario: Patient records exist
Given a patient record exists in the system, when the staff member searches for and selects the patient. Then the system displays the patient's stored information.

User story 2 - Booking an appointment
Story: As a staff member, I want to book an appointment for a patient with a practitioner, so that the patient's appointment is recorded in the system.
Linked requirements: Fr-05, Fr-07
Scenario: Appointment is available 
Given the patient and practitioner records exist And the practitioner has no appointment at the selected time. When the staff member books the appointment, then the system creates the appointment and displays its details.

User story 3 - Preventing Duplicate Bookings
Story: As a staff member, I want the system to prevent double bookings, so that two appointments are not booked with the same practitioner at the same time
Linked requirements: Fr-06
Scenario: Practitioner is already booked
Given a practitioner already has an appointment at the selected time, when the staff member attempts to book another appointment with that practitioner at the same time. Then the system refuses to create the second appointment.

User story 4 - Updating Appointment status
Story: As a staff member, I want to update an appointment status,so that staff and practitioners can see the current status of an appointment.
Linked requirements: Fr-08
Scenario: Appointment status is updated
Given an appointment exists in the system, when the staff member selects a valid appointment status. Then the system saves the appointment with the selected status.