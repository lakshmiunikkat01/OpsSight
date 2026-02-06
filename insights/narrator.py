def generate_insight(row):
    region = row["region"]
    department = row["department"]
    sector = row["sector"]
    ops_value = row["ops_value"]
    ops_delta = row["ops_delta"]

    direction = "increase" if ops_delta > 0 else "decrease"

    insight = (
        f"{region} – {department} ({sector}) shows an abnormal operational "
        f"{direction}, with an estimated deviation of {ops_delta:,.0f}. "
        f"This is driven by a disproportionately high cost allocation."
    )

    return insight
