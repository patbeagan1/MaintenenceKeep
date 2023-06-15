def add_new_task():
    output = []
    output.append("<html><body><div>")
    add_new_task_submission_form(output)
    output.append("</div></body></html>")
    return "".join(output)


def add_new_task_submission_form(output):
    output.append(f"""
        <form action="/add" method="get">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="seconds">Number of seconds:</label><br>
            <input type="number" id="seconds" name="seconds"><br>
            <input type="submit" value="Submit">
        </form>
        """)
