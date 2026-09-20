Part C) My prrompt for copilot:

Act as a Python tutor.
I am learning introductory software technology.
Here is a small appointment-booking function.
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.


The output it gave me:

The function you shared is the human‑written SmartCare prototype from your Stage 1 lab. I’ll walk you through it like a tutor — clear, structured, and focused on understanding rather than rewriting.

✅ 1. What the code does
The program stores appointment details (patient, practitioner, time) and prints them out.
It uses:

A list (appointments) to hold multiple appointment records

A dictionary for each appointment

A function book_appointment() to add an appointment

A function display_appointments() to print all stored appointments

When run, it:

Prints a welcome message

Books two appointments

Displays all recorded appointments

This matches the assignment description:

“Each appointment records patient name, practitioner name and appointment time.”

⚠️ 2. Three limitations
No validation for practitioner or time  
Only patient name is checked. Strange inputs like None or empty strings will still be accepted.

No conflict checking  
The system allows two appointments at the same time with the same practitioner — one of the required test cases in Part F.

No user input  
Everything is hard‑coded. A receptionist cannot actually enter appointments.

You can explore each limitation further using:

input validation

error handling

data conflicts

🔧 3. Suggested improvements (without rewriting the whole app)
Add simple checks for practitioner name and appointment time

Add a check inside book_appointment() to detect double‑bookings

Add a small helper function to validate strings, e.g. [validate_text](ca://s?q=Show_me_a_simple_text_validation_function)

Add optional logging or print statements to help the receptionist understand what went wrong

These are small, controlled improvements — exactly what Part G asks for.

❓ 4. Two questions to test your understanding
Why is a list of dictionaries more flexible than using separate variables like patient1_name, patient2_name?

What could happen if you don’t validate the appointment time before storing it?

My answers for its questions:
1. A list of dictionaries is more flexible because you can store many appointments in the same structure rather than creating seperate variables, instead each appointment can be stored in a list.
2. If you dont validate the appointment time, the user could enter an invalid time. This would cause incorrect appointment information to be stored which could make the system harde to use.


Part D) My prompt create a simple beginner-friendly Python function that stores patient name, practitioner name and
appointment time. Explicitly prohibit a database or GUI.




Copilots output
def create_appointment(patient_name, practitioner_name, appointment_time):
    """Store a single appointment in a dictionary."""
    
    # Basic validation to avoid empty values
    if not patient_name:
        raise ValueError("Patient name cannot be empty.")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty.")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty.")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    return appointment


# Example usage
appt = create_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
print(appt)

