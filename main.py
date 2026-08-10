import json
import pandas as pd
from validator import FHIRResourceValidator


def validate_resource(data: dict) -> dict:
    try:
        resource_type = data.get("resourceType")

        if not resource_type:
            return {
                "resourceType": None,
                "overall_valid": False,
                "structural_errors": ["Missing resourceType"]
            }

        validator = FHIRResourceValidator(resource_type)
        return validator.validate(data)

    except Exception as e:
        return {
            "resourceType": data.get("resourceType"),
            "overall_valid": False,
            "structural_errors": [str(e)],
            "required_field_errors": [],
            "value_set_errors": []
        }


def validate_bundle(data: dict) -> dict:
    entries = data.get("entry", [])
    results = []

    for i, entry in enumerate(entries):

        try:
            resource = entry.get("resource")

            if not resource:
                results.append({
                    "entry_index": i,
                    "resourceType": None,
                    "overall_valid": False,
                    "structural_errors": [
                        "Entry missing 'resource'"
                    ]
                })
                continue

            report = validate_resource(resource)
            report["entry_index"] = i

            results.append(report)

        except Exception as e:
            results.append({
                "entry_index": i,
                "resourceType": entry.get("resource", {}).get("resourceType"),
                "overall_valid": False,
                "structural_errors": [str(e)]
            })

    return {
        "resourceType": "Bundle",
        "total_entries": len(entries),
        "valid_entries": sum(
            1 for r in results if r.get("overall_valid", False)
        ),
        "invalid_entries": sum(
            1 for r in results if not r.get("overall_valid", False)
        ),
        "overall_valid": all(
            r.get("overall_valid", False)
            for r in results
        ),
        "entry_results": results
    }


def validate_file(file_path: str) -> dict:
    """
    Read and validate a JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if data.get("resourceType") == "Bundle":
        return validate_bundle(data)

    return validate_resource(data)


def export_to_json(report: dict,
                   output_file: str = "validation_report.json"):
    """
    Save validation report as JSON.
    """
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(report, outfile, indent=4)

    print(f"JSON report created: {output_file}")



if __name__ == "__main__":

    report = validate_file("examples/r1.json")

    print(json.dumps(report, indent=4))

    with open("validation_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, default=str)

    print("Validation report saved to validation_report.json")


    