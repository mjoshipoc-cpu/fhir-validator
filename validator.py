from pydantic.v1 import ValidationError
from fhir.resources.R4B import construct_fhir_element
from config import REQUIRED_FIELDS, VALUE_SETS, COMMON_VALUE_SETS


def _get_path(data: dict, path: str):
    parts = path.split(".")
    current = [data]
    for part in parts:
        nxt = []
        for item in current:
            if isinstance(item, dict) and part in item:
                val = item[part]
                nxt.extend(val if isinstance(val, list) else [val])
        current = nxt
    return current


class FHIRResourceValidator:
    def __init__(self, resource_type: str):
        self.resource_type = resource_type
        self.required_fields = REQUIRED_FIELDS.get(resource_type, [])
        self.value_sets = {**COMMON_VALUE_SETS, **VALUE_SETS.get(resource_type, {})}

    def validate_structure(self, data: dict):
        try:
            resource = construct_fhir_element(self.resource_type, data)
            return True, resource, []
        except ValidationError as e:
            return False, None, e.errors()
        except KeyError:
            return False, None, [{"msg": f"Unknown resourceType: {self.resource_type}"}]

    def validate_required_fields(self, data: dict) -> list:
        return [
            f"Missing required field: {field}"
            for field in self.required_fields
            if not data.get(field)
        ]

    def validate_value_sets(self, data: dict) -> list:
        errors = []
        for path, allowed in self.value_sets.items():
            for value in _get_path(data, path):
                if value not in allowed:
                    errors.append(f"Invalid value at '{path}': {value}")
        return errors

    def validate(self, data: dict) -> dict:
        if data.get("resourceType") != self.resource_type:
            return {
                "resourceType": data.get("resourceType"),
                "overall_valid": False,
                "structural_errors": [
                    f"Expected resourceType '{self.resource_type}', got '{data.get('resourceType')}'"
                ],
            }

        struct_ok, _, struct_errors = self.validate_structure(data)
        required_errors = self.validate_required_fields(data)
        value_errors = self.validate_value_sets(data)

        return {
            "resourceType": self.resource_type,
            "structurally_valid": struct_ok,
            "structural_errors": struct_errors,
            "required_field_errors": required_errors,
            "value_set_errors": value_errors,
            "overall_valid": struct_ok and not required_errors and not value_errors,
        }
