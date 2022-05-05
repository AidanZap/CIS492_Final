from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import database as db

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.run()

@app.route('/pipeline', methods=["GET"])
@cross_origin()
def pipeline():
    country = request.args.get("country")
    media_type = int(request.args.get("type"))
    time_period = int(request.args.get("time_period"))
    rating = int(request.args.get("rating"))
    duration = int(request.args.get("duration"))
    genre = request.args.get("genre")
    result = db.pipeline(country, media_type, time_period, rating, duration, genre)

    if not result:
        return Response("Query was too specific, no results found!", status=400, mimetype="text/plain")
    elif type(result) is not list and result["error"]:
        return Response(result["error"], status=500, mimetype="text/plain")
    else:
        return jsonify(result)
