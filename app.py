from http import HTTPStatus

from flask import Flask, request, abort, Response

from services.coalesce import get_coalesced


app = Flask(__name__)


@app.route('/')
def controller():
    """
    Declares the controller for the only endpoint on the application. It
    validates the member_id parameter presence and value and coalesce diverse
    data results into a single one.

    :return: A JSON representation of coalesced data.
    """
    v = request.args.get("member_id")
    if not v:
        abort(HTTPStatus.BAD_REQUEST)

    try:
        member_id = int(v)
    except ValueError:
        abort(HTTPStatus.BAD_REQUEST)

    try:
        r = get_coalesced(member_id)
    except Exception:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)

    return Response(r.to_json(), mimetype="application/json")
