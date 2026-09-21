Part F)
My prompt:
Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity,
inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every
suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

The output:
✅ SmartCare Requirements Review (Part F)
🧩 1. Stakeholders & Scope Review
Ambiguity: “Control access point to patient information”
Issue: The phrase is unclear — does it mean authentication, role‑based access, audit logging, or simply preventing unauthorised access?

Classification: Validation‑required — the brief does not define the intended access control model.

Ambiguity: “Provide appointment history”
Issue: It is unclear whether history must include all past appointments or only a limited period.

Classification: Validation‑required — the brief mentions “limited appointment history” but does not specify the required depth.

Inconsistency: “Allow staff to update appointment information” vs FR‑08
Issue: Scope says “update appointment information,” but FR‑08 only allows updating status, not date/time or practitioner.

Classification: Evidence‑based — your own scope and FRs conflict.

Missing clarification: Practitioner responsibilities
Issue: Practitioners are listed as stakeholders but no requirement describes what they can do in the system.

Classification: Validation‑required — unclear whether practitioners need direct system access.

⚙️ 2. Functional Requirements Review
FR‑01 / FR‑02 / FR‑03 / FR‑04 – “view information”
Issue: “View” is ambiguous — does this include search, filtering, or only selecting from a list?

Classification: Validation‑required — the brief mentions difficulty finding information, but does not specify search behaviour.

FR‑05 – Creating an appointment
Issue: Does the system validate the appointment time format?

Classification: Validation‑required — the brief does not specify time format rules.

FR‑06 – Preventing double bookings
Issue: Requirement is clear and testable, but does not specify whether overlapping appointments (e.g., 10:00–10:30 vs 10:15–10:45) count as duplicates.

Classification: Validation‑required — the brief only mentions “duplicate bookings,” not overlapping ones.

FR‑07 – Viewing appointment details
Issue: “Appointment status” is referenced but not defined anywhere.

Classification: Validation‑required — the brief mentions inconsistent status but does not define valid statuses.

FR‑08 – Updating appointment status
Issue: “Status values defined by the system” is vague — unclear whether these are fixed, configurable, or role‑restricted.

Classification: Validation‑required — no evidence in the brief.

FR‑09 – Recording appointment history
Issue: Requirement is clear, but does not specify whether history includes cancelled appointments.

Classification: Validation‑required — brief does not specify.

🛡️ 3. Non‑Functional Requirements Review
NFR‑01 – Display within 2 seconds
Issue: Testable, but unclear whether this applies to all devices, all record sizes, or only typical usage.

Classification: Validation‑required — brief does not specify performance expectations.

NFR‑02 – Login requirement
Issue: Wording unclear: “shall require to log in” — who must log in? Staff only? Practitioners?

Classification: Validation‑required — brief does not specify user roles.

NFR‑03 – Prevent unauthorised modification
Issue: Good requirement, but unclear whether read‑only access is allowed for some roles.

Classification: Validation‑required — brief does not define role permissions.

NFR‑04 – Consistent appointment status
Issue: Testable, but depends on FR‑08’s undefined status list.

Classification: Evidence‑based — brief mentions inconsistent status.

NFR‑05 – Preserve records when closed
Issue: Clear and testable, but unclear whether this implies local storage, cloud storage, or file‑based persistence.

Classification: Validation‑required — brief does not specify storage method.

👤 4. User Stories & Acceptance Criteria Review
User Story 1 – Finding patient information
Issue: Linked requirements include FR‑03 (create practitioner record), which is unrelated to finding patient information.

Classification: Evidence‑based — inconsistency in your own linking.

User Story 2 – Booking an appointment
Issue: Acceptance criteria do not specify what happens if the practitioner does have an appointment — negative scenario missing.

Classification: Validation‑required — brief mentions duplicate bookings but does not specify error behaviour.

User Story 3 – Preventing duplicate bookings
Issue: Clear and testable.

Classification: Evidence‑based — directly supported by the brief.

User Story 4 – Updating appointment status
Issue: “Valid appointment status” is undefined.

Classification: Validation‑required — brief does not define valid statuses.

📌 Summary of Key Issues
Evidence‑based issues (supported by the brief or your own requirements):
Duplicate bookings (FR‑06, User Story 3)

Inconsistent appointment status (NFR‑04)

Linking error in User Story 1

Scope vs FR inconsistency (update appointment info vs only update status)

Validation‑required issues (need client clarification):
What “maintainable” means

What “appointment history” includes

Whether practitioners use the system directly

Search behaviour for finding patient information

Valid appointment statuses

Time format rules

Overlapping appointment rules

Role‑based access control

Performance expectations

Storage method

Negative booking behaviour

Whether appointment updates include date/time changes

Part G)
Ai suggestion. Classification. Reason 
Scope says staff can update appointment information, but Fr-08 only updates status. Accepted. The scope and FR-08 do not match.
Staff should be able to search for a patient information. Accepted. Staff have difficutly finding patient information
It is unclear 