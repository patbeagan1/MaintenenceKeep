_data_filename = ""


def get_data_filename():
    global _data_filename
    return _data_filename

def set_data_filename(incoming: str):
    global _data_filename
    _data_filename = incoming
