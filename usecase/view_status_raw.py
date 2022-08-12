def view_status_raw():
    with open("build/data.csv", "r") as f:
        return f.read()