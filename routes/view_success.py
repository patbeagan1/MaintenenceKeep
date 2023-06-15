def success():
    return f"""
        <div>
          <h2>Success!</h2>
          <a href="/">Return home</a>
        </div>
        """


def failure(e: Exception):
    message = f"<p>Exception is {e}</p>" if e else ""

    return f"""
        <div>
          <h2>Failure!</h2>
          <div>The requested action was not completed.</div>
            {message}
          <a href="/">Return home</a>
        </div>
        """
