Part A)
Nouns: Staff, practitioner, management, patient, appointment, patient record, practitioner record, appointment history, appointment status,  appointment system.

Verb: manage, look up, provide, use, oversee, store, view, , create, update, search, prevent, book, log in, display, maintain, preserve.

Business rules: 
Fr-06: two appointments cant share the same practitioner and time
Fr-08: appointment status can only be set to system defined values
NFR-01: records must display within 2 seconds
NFR-02: users must be able to log in before accessing patient information
NFR-03: unautherised users can't modify records
NFR-04: an appointment has exactly one current status at a time
NFR-05: records must persist across close and reopen

Part B)
Class - FR, NFR - State - behaviour
Patient - Fr-01, Fr-02, Fr-10 - patientID, name - createRecord(), view info()
Practitioner - Fr-03, Fr-04 - practitionerID, name - createRecord(), viewInfo()
Appointment - Fr-05, Fr-06, Fr-07, Fr-08, Fr-09 - appointmentID, dateTime, status, link to patient, link to practitioner - book(), hasConflict(), updateStatus(), viewDetails()

Part C)
Patient)
Responsibilties: Hold the patient information, and provide the details upon request
Collaborators: Appointment
Appointment)
Responsibilties: Hold date, time and status. refuse to be booked if the same practitioner already has an appointment at that time
Collaborators: Patient and Practitioner.

Part D)
Patient: patientID: string, name: string - createRecord(), viewInfo()
Practitioner: practitionerId: string, name: string - createRecord(), viewInfo()
Appointment: appointmentId: sting, name: string -  book (), hasConflict(): bool, updateStatus(newStatus), viewDetails()

Part E)
✅ Candidate Classes & Relationships (Requirement‑Driven)
🧩 1. Class: Patient
Supported by:

FR‑01 (create patient record)

FR‑02 (view patient information)

FR‑09 (appointment history)

Likely attributes:

patient_id

name

contact_details (optional — see unsupported section)

appointment_history (list of Appointment)

Relationships:

Patient → Appointment (one‑to‑many)

Supported by FR‑09: “record each appointment in the patient’s appointment history.”

🧩 2. Class: Practitioner
Supported by:

FR‑03 (create practitioner record)

FR‑04 (view practitioner information)

FR‑06 (prevent double bookings)

Likely attributes:

practitioner_id

name

specialty (optional — see unsupported section)

Relationships:

Practitioner → Appointment (one‑to‑many)

Supported by FR‑06: checking whether a practitioner already has an appointment at a given time.

🧩 3. Class: Appointment
Supported by:

FR‑05 (create appointment)

FR‑06 (prevent double bookings)

FR‑07 (view appointment details)

FR‑08 (update appointment status)

FR‑09 (record appointment in history)

Likely attributes:

appointment_id

patient_id (or reference to Patient)

practitioner_id (or reference to Practitioner)

date_time

status (using system‑defined values — FR‑08)

Relationships:

Appointment → Patient (many‑to‑one)

Supported by FR‑05: appointment is created “for a patient.”

Appointment → Practitioner (many‑to‑one)

Supported by FR‑05 and FR‑06.

🧩 4. Class: AppointmentStatus (Optional but Supported)
Supported by:

FR‑08 (update appointment status using system‑defined values)

NFR‑04 (consistent appointment status)

Reasoning:  
The system must enforce a controlled set of valid statuses.
A small class or enumeration would satisfy this requirement.

🧩 5. Class: UserAccount
Supported by:

NFR‑02 (system shall require login)

NFR‑03 (prevent unauthorised modification)

Likely attributes:

user_id

username

password_hash

role (staff, practitioner — unclear, see validation note)

Relationships:

None required by the confirmed requirements.

🔗 Summary of Supported Relationships
Relationship	Supported Requirement(s)
Patient → Appointment (1‑to‑many)	FR‑05, FR‑07, FR‑09
Practitioner → Appointment (1‑to‑many)	FR‑05, FR‑06
Appointment → Patient (many‑to‑one)	FR‑05
Appointment → Practitioner (many‑to‑one)	FR‑05, FR‑06
Appointment → AppointmentStatus	FR‑08, NFR‑04
UserAccount → System (login/auth)	NFR‑02, NFR‑03


🚫 Suggestions NOT Supported by Requirements (Flagged)
These are common design elements, but your confirmed requirements do not justify them.

❌ Class: Clinic / Organisation
No requirement mentions multiple clinics, departments, or organisational structure.

❌ Class: AuditLog
Although useful, no requirement mentions logging, auditing, or tracking changes.

❌ Class: SearchEngine / SearchService
Searching is implied in user stories, but no FR explicitly requires search functionality.
(Your user story mentions searching, but user stories are not binding requirements.)

❌ Class: ContactDetails
FRs do not require storing phone numbers, emails, or addresses.

❌ Class: AuthenticationService
NFR‑02 and NFR‑03 require login and access control, but do not specify how authentication is implemented.

❌ Class: AppointmentHistory
History is already covered by FR‑09 as part of the Patient class.
No requirement supports a separate history class.

📌 Final Output (Concise)
Supported Classes
Patient

Practitioner

Appointment

AppointmentStatus (enum/class)

UserAccount

Supported Relationships
Patient ↔ Appointment

Practitioner ↔ Appointment

Appointment ↔ AppointmentStatus

UserAccount ↔ System (authentication)

Unsupported Suggestions (Flagged)
Clinic

AuditLog

SearchService

ContactDetails

AuthenticationService

AppointmentHistory (separate class)

Part F)
Accepted:
AppointmentStatus: copilot calls this "supported," but FR-08/NFR-04 only require that status stays consistent and comes from a system-defined set they never say what that set is. Kept status as a plain attribute on Appointment rather than building a class around an undefined value list

UserAccount: the need for a login concept is genuinely supported by NFR-02/NFR-03, so the class itself is reasonable. But the specific attributes Copilot invented (password_hash, role) aren't supported

Rejected:
SearchService: This class is resonable to reject but not for  copilots resoning. Copilot said no Fr supports search, which is incorrect Fr-10 does.

Clinic, AuditLog, ContactDetails, AuthenticationService, separate AppointmentHistory class. None of these appear in the breif so copilots rejection is valid.



Part G)
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def view_info(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name

    def view_info(self):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time, status="scheduled"):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def has_conflict(self, existing_appointments):
        pass

    def update_status(self, new_status):
        pass

    def view_details(self):
        pass


Part H)
Appointment.patient / Appointment.practitioner match assosiations in Part D
status stays a plain attribute, matching the Part F decision not to model it as an enum.
No cancel() or AppointmentHistory in the skeleton stays consistent with the Part F rejection.
Behaviour bodies are left as pass deliberately, per the task instruction not to implement full behaviour yet.

Reflection)
The hardest modelling decision was the status attribute. AI suggested an AppointmentStatus enum, but the brief never defines the valid statuses, so using one would mean inventing requirements. A similar issue came up with UserAccount. NFR-02 and NFR-03 support having the class, but Copilot suggested attributes like password_hash and role that were not in the brief, so I left those out. AI also suggested extra features such as AppointmentHistory, cancel(), and AuditLog, but these could not be traced to any FR or NFR. opilot also incorrectly said that no FR required search functionality, even though FR-10 specifically states that staff must be able to search for a patient record. The final decision was still not to create a separate SearchService, but the AI's reasoning was incorrect. I used the FR/NFRs in smartcare_requirements_v02.md as the main evidence for my decisions. Anything included had to be supported by a requirement, while unsupported or incorrectly justified suggestions were removed.