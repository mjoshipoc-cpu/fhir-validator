REQUIRED_FIELDS = {
    # Clinical Module
    "AllergyIntolerance":     ["patient"],
    "Condition":              ["subject"],
    "Procedure":              ["subject", "status"],
    "FamilyMemberHistory":    ["patient", "status", "relationship"],
    "CarePlan":               ["subject", "status", "intent"],
    "Goal":                   ["subject", "lifecycleStatus", "description"],
    "CareTeam":               [],

    # Diagnostic Module
    "Observation":            ["status", "code"],
    "DocumentReference":      ["status", "content"],
    "ImagingStudy":           ["status", "subject"],
    "DiagnosticReport":       ["status", "code"],
    "ServiceRequest":         ["status", "intent", "subject"],

    # Medication Module
    "MedicationDispense":     ["status", ("medicationCodeableConcept", "medicationReference")],
    "MedicationAdministration": [
        "status", "subject",
        ("medicationCodeableConcept", "medicationReference"),
        ("effectiveDateTime", "effectivePeriod"),
    ],
    "Immunization": [
        "status", "vaccineCode", "patient",
        ("occurrenceDateTime", "occurrenceString"),
    ],

    # Administration
    "Patient":                [],
    "Practitioner":           [],
    "Organization":           [],
    "Location":               [],
}

VALUE_SETS = {
    "AllergyIntolerance": {
        "clinicalStatus.coding.code":      {"active", "inactive", "resolved"},
        "verificationStatus.coding.code":  {"unconfirmed", "confirmed", "refuted", "entered-in-error"},
        "type":                            {"allergy", "intolerance"},
        "category":                        {"food", "medication", "environment", "biologic"},
        "criticality":                     {"low", "high", "unable-to-assess"},
        "reaction.severity":               {"mild", "moderate", "severe"},
    },
    "Condition": {
        "clinicalStatus.coding.code":     {"active", "recurrence", "relapse", "inactive", "remission", "resolved"},
        "verificationStatus.coding.code": {"unconfirmed", "provisional", "differential", "confirmed", "refuted", "entered-in-error"},
    },
    "Procedure": {
        "status": {"preparation", "in-progress", "not-done", "on-hold", "stopped", "completed", "entered-in-error", "unknown"},
    },
    "FamilyMemberHistory": {
        "status": {"partial", "completed", "entered-in-error", "health-unknown"},
    },
    "CarePlan": {
        "status": {"draft", "active", "on-hold", "revoked", "completed", "entered-in-error", "unknown"},
        "intent": {"proposal", "plan", "order", "option"},
    },
    "Goal": {
        "lifecycleStatus": {"proposed", "planned", "accepted", "active", "on-hold", "completed", "cancelled", "entered-in-error", "rejected"},
    },
    "CareTeam": {
        "status": {"proposed", "active", "suspended", "inactive", "entered-in-error"},
    },
    "Observation": {
        "status": {"registered", "preliminary", "final", "amended", "corrected", "cancelled", "entered-in-error", "unknown"},
    },
    "DocumentReference": {
        "status": {"current", "superseded", "entered-in-error"},
    },
    "ImagingStudy": {
        "status": {"registered", "available", "cancelled", "entered-in-error", "unknown"},
    },
    "DiagnosticReport": {
        "status": {"registered", "partial", "preliminary", "final", "amended", "corrected", "appended", "cancelled", "entered-in-error", "unknown"},
    },
    "ServiceRequest": {
        "status":   {"draft", "active", "on-hold", "revoked", "completed", "entered-in-error", "unknown"},
        "intent":   {"proposal", "plan", "directive", "order", "original-order", "reflex-order", "filler-order", "instance-order", "option"},
        "priority": {"routine", "urgent", "asap", "stat"},
    },
    "MedicationDispense": {
        "status": {"preparation", "in-progress", "cancelled", "on-hold", "completed", "entered-in-error", "stopped", "declined", "unknown"},
    },
    "MedicationAdministration": {
        "status": {"in-progress", "not-done", "on-hold", "completed", "entered-in-error", "stopped", "unknown"},
    },
    "Immunization": {
        "status":      {"completed", "entered-in-error", "not-done"},
        "primarySource": {True, False},
    },
    "Patient": {
        "gender": {"male", "female", "other", "unknown"},
    },
    "Practitioner": {
        "gender": {"male", "female", "other", "unknown"},
    },
    "Location": {
        "status": {"active", "suspended", "inactive"},
        "mode":   {"instance", "kind"},
    },
}

COMMON_VALUE_SETS = {
    "telecom.system": {"phone", "fax", "email", "pager", "url", "sms", "other"},
    "identifier.use": {"usual", "official", "temp", "secondary", "old"},
    "name.use":       {"usual", "official", "temp", "nickname", "anonymous", "old", "maiden"},
}
