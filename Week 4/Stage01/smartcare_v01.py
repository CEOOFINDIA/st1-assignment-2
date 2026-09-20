# Part A)
# 1)Each appointment needs to store the patient name, practitioner name and appointment time. This should be enough for a basic prototype, but not enough for a real clinic. A real clinic would need things such as the patients contact information, appointmeent type and appointment status. Since this being a small prototype you only need to the 3 pieces of information.
# 2)The main functions would be booking an appointment, and viewing all appointments. You should also be able to cancel an appointment, changing an appointment time and searching for a specific appointment by patient name.
# 3) There are a few thins that could go wrong with the system. For example, someone could leave the patients name blank, enter the wrong appointment time or book two appointments with the same practitioner at the same time. The person could also enter unvalid characters such as None which would cause probelms with the system.
# 4) Some part of the requirements are not clear. For example, it does not say exactly what the format the appointment time should be in. It is also unclear if the receptionist should be able to cancel or rebook an appointment.

# Part B)
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

appointments = []

# Part G improvement: prevent double booking the same practitioner and time
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    for appointment in appointments:
        if (appointment["practitioner"] == practitioner_name and
                appointment["time"] == appointment_time):
            raise ValueError("Practitioner is already booked at this time")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

print("Welcome to SmartCare: The Clinical Appointment Booking System!")
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
display_appointments()


# 1)The appointments are not saved permanently, so if the program closes all of the data is lost
# 2)There is no way to cancel an appointment, you are able to see your apointment but are not able to remove it.
# 3)There is no way to change the appointment, if the receptionist enters the wrong time or the patient needs to change their appointment time, there is no way to do that.
# 4)The system allows for double booking, so if two patients book the same practitioner at the same time, the system will not prevent it.
# 5)The system does not validate the practitioner name or appointment time, so inncorrect data can be entered without any checks.


# Part F)
# Human version
# Normal enviorment: Worked successfully
# Blank Name: Gave an error message
#Double booking: Allowed double booking, did not prevent it
#None value: Gave an error message

#Ai version
# Normal appointment: Works
# Blank Name: Gave an error message
# Double booking: Allowed double booking
# None value: Gave an error message
