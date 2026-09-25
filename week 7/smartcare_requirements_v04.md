Part A)
Patient: patientID, name — createRecord(), viewInfo()
Practitioner: practitionerId, name — createRecord(), viewInfo() — no specialty 
Appointment: appointmentId, dateTime, status, link to Patient, link to Practitioner — book(), hasConflict(): bool, updateStatus(newStatus), viewDetails() — no cancel() method
This week adds specialty to Practitioner, which wasn't in the Week 6 UML. However, this is directly required by this week's task, so it isn't an AI assumption. It also adds AppointmentStatus and cancel(). In Week 6, I rejected the AppointmentStatus enum because the brief didn't give any valid status values, and I rejected cancel() because it wasn't linked to a requirement. This week's task now gives the status values and specifically requires cancellation, so these are valid changes based on the new requirements. The existing updateStatus(newStatus) will still handle the actual status changes, with cancel() just acting as a wrapper around it.

Part B)
class Patient:
    def __init__(self, patient_id: str, name: str) -> None:
        if not patient_id:
            raise ValueError("patient_id cannot be empty")
        if not name:
            raise ValueError("name cannot be empty")
        self.patient_id: str = patient_id
        self.name: str = name

    def view_info(self) -> str:
        return f"Patient(id={self.patient_id}, name={self.name})"

Part C)
class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        if not practitioner_id:
            raise ValueError("practitioner_id cannot be empty")
        if not name:
            raise ValueError("name cannot be empty")
        if not specialty:
            raise ValueError("specialty cannot be empty")
        self.practitioner_id: str = practitioner_id
        self.name: str = name
        self.specialty: str = specialty  # not in Week 6 UML — added per this week's Part C instruction

    def view_info(self) -> str:
        return f"Practitioner(id={self.practitioner_id}, name={self.name}, specialty={self.specialty})"

Part D)
from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class InvalidStatusTransitionError(Exception):
    """Raised when an appointment status change is not allowed."""


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: "Patient",
        practitioner: "Practitioner",
        date_time: datetime,
    ) -> None:
        if not appointment_id:
            raise ValueError("appointment_id cannot be empty")
        if patient is None:
            raise ValueError("patient is required")
        if practitioner is None:
            raise ValueError("practitioner is required")
        if date_time is None:
            raise ValueError("date_time is required")

        self._appointment_id: str = appointment_id
        self._patient = patient
        self._practitioner = practitioner
        self._date_time: datetime = date_time
        self._status: AppointmentStatus = AppointmentStatus.SCHEDULED

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> "Patient":
        return self._patient

    @property
    def practitioner(self) -> "Practitioner":
        return self._practitioner

    @property
    def date_time(self) -> datetime:
        return self._date_time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    @staticmethod
    def has_conflict(
        practitioner: "Practitioner",
        date_time: datetime,
        existing_appointments: list["Appointment"],
    ) -> bool:
        return any(
            appt.practitioner is practitioner
            and appt.date_time == date_time
            and appt.status == AppointmentStatus.SCHEDULED
            for appt in existing_appointments
        )

    @classmethod
    def book(
        cls,
        appointment_id: str,
        patient: "Patient",
        practitioner: "Practitioner",
        date_time: datetime,
        existing_appointments: list["Appointment"],
    ) -> "Appointment":
        if cls.has_conflict(practitioner, date_time, existing_appointments):
            raise ValueError("Practitioner already has an appointment at this time")
        return cls(appointment_id, patient, practitioner, date_time)

    def update_status(self, new_status: AppointmentStatus) -> None:
        if not isinstance(new_status, AppointmentStatus):
            raise TypeError("new_status must be an AppointmentStatus value")
        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransitionError("A cancelled appointment cannot change status")
        self._status = new_status

    def cancel(self) -> None:
        # Routes through update_status() rather than being a separate mechanism,
        # so one method enforces all transition rules.
        self.update_status(AppointmentStatus.CANCELLED)

    def view_details(self) -> str:
        return (
            f"Appointment(id={self._appointment_id}, patient={self._patient.name}, "
            f"practitioner={self._practitioner.name}, time={self._date_time}, "
            f"status={self._status.value})"
        )

Part E)
Model consistency, Copilot used patient_id/practitioner_id: int, not object links, approved UML specifies links to Patient/Practitioner.
Unsupported features, Copilot added a completed status not required by the brief or this week's task.
Public state mutation, status is read-only via property, changeable only through update_status().
Unnecessary inheritance, None present.
Invented dependencies, Standard library only (enum, datetime).
Error handling, Terminal-state protection present, but Copilot removed hasConflict(), contradicting the approved UML, which requires it. Restored as a static method.
Missing constructor validation, Copilot's version validated nothing. Added validation matching Patient/Practitioner.
Interface namingm Copilot used __str__ instead of the UML's viewDetails(). Renamed to view_details().

Part F)
from datetime import datetime

patient = Patient("P1", "Alice Smith")
practitioner = Practitioner("D1", "Dr. John Doe", "General Practice")

# Valid object creation
appt = Appointment.book("A1", patient, practitioner, datetime(2026, 10, 5, 10, 0), [])
print(appt.view_details())

# Invalid input
try:
    Appointment("", patient, practitioner, datetime.now())
except ValueError as e:
    print("Caught expected error:", e)

# Double-booking check
try:
    Appointment.book("A2", patient, practitioner, datetime(2026, 10, 5, 10, 0), [appt])
except ValueError as e:
    print("Caught expected error:", e)

# Cancel a scheduled appointment
appt.cancel()
print(appt.status)

# Illegal repeated transition
try:
    appt.cancel()
except InvalidStatusTransitionError as e:
    print("Caught expected error:", e)
    
Part G)
Changed the constructor validation for Patient, Practitioner, and Appointment to use the same pattern (if not X: raise ValueError(...)) so the validation is consistent across all three classes. Removed Copilot's COMPLETED state and the patient_id/practitioner_id int fields. This keeps the code consistent with the approved two-status design and the object references. Kept cancel() as a simple wrapper around update_status() instead of having a separate transition path. This means update_status() is still the only method that handles the rule that no changes can be made after cancellation.

Part H)
Prompt: Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML.
Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add
database, UI, notification or service classes. Protect status transitions and explain any decision not directly
visible in the UML.

Generated contribution: Copilot gave me an Appointment class with integer patient_id/practitioner_id fields instead of object references. It also added a three-value AppointmentStatus enum (SCHEDULED, COMPLETED, CANCELLED), status protection using properties and transition checks, and a __str__ method. It also explained five design decisions, including why it left out hasConflict().

Decisions: Accepted: The status transition protection using update_status(), no extra database/UI/service classes, and using an enum since this week's task now gives actual status values. Modified: Changed patient_id/practitioner_id from integers to object references to match the approved UML. Changed __str__ to view_details() to match the UML and the other classes. I also added constructor validation to keep it consistent with Patient and Practitioner. Rejected: Removed the COMPLETED status because it wasn't required by the task. I also rejected Copilot's decision to remove hasConflict(). Its reasoning made sense on its own, but it didn't match the approved UML, which already included hasConflict(): bool in Appointment, so I kept it.

Verification evidence: Part F shows that the corrected version was tested for valid construction, empty-field rejection, conflict detection when booking, successful cancellation, and rejection of a second cancellation. All tests passed.

Reflection)
The biggest issue this week wasn't AI adding something unsupported. It was Copilot removing something that was already part of my approved design. Its reasoning for removing hasConflict() made sense on its own, but it didn't match my Week 6 UML, which already gave Appointment that responsibility. This was different from the Week 6 FR-10 issue, where Copilot misunderstood an existing requirement. This time, it made a reasonable design choice that just didn't fit the design I had already approved. The Week 6 UML also set some things that I needed to keep consistent, such as the object links, hasConflict(), and appointmentId being a string. So even if Copilot suggested something that made sense, I still needed to check it against my existing UML. The only changes I made to the Week 6 design were adding AppointmentStatus and cancel(), which were directly required by this week's task rather than being based on Copilot's suggestions.