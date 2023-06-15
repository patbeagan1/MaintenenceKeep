from util.datamanager import get_data_filename


def view_status_raw():
    with open(get_data_filename(), "r") as f:
        return f.read()
