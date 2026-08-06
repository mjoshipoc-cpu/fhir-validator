REQUIRED_FIELDS = {
    "AllergyIntolerance":   ["patient"],
    "Condition":            ["subject"],
    "Patient":              [],
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
    "Patient": {
        "gender": {"male", "female", "other", "unknown"},
    },
}

COMMON_VALUE_SETS = {
    "telecom.system": {"phone", "fax", "email", "pager", "url", "sms", "other"},
    "identifier.use": {"usual", "official", "temp", "secondary", "old"},
    "name.use":       {"usual", "official", "temp", "nickname", "anonymous", "old", "maiden"},
}
