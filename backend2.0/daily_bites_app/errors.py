from daily_bites_app import app


class BadArgumentError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


@app.errorhandler(BadArgumentError)
def handle_bad_argument_error(e):
    return {"message": str(e)}, 400
