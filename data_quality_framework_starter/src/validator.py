"""Simple reusable data quality checks for lists of dictionaries."""

def validate_records(records, required_fields):
    """Validate records and return a summary plus row-level issues.

    Args:
        records: A list of dictionaries, such as rows read from a CSV.
        required_fields: Field names that must be present and non-empty.

    Returns:
        A dictionary containing total_rows, valid_rows, invalid_rows, and issues.
    """
    issues = []

    for row_number, record in enumerate(records, start=1):
        missing = [
            field for field in required_fields
            if field not in record or record[field] is None or str(record[field]).strip() == ""
        ]

        if missing:
            issues.append({
                "row": row_number,
                "issue": "Missing required value",
                "fields": missing,
            })

    invalid_rows = len({issue["row"] for issue in issues})
    total_rows = len(records)

    return {
        "total_rows": total_rows,
        "valid_rows": total_rows - invalid_rows,
        "invalid_rows": invalid_rows,
        "issues": issues,
    }
