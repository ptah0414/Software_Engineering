from flask import Flask
from flask import request
from flask import render_template
from flask import url_for, redirect, flash
from flask import abort
from flask import session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from datetime import datetime
import time


app = Flask(__name__, template_folder="templates")
app.config["MONGO_URI"] = "mongodb://localhost:27017/temp"
app.config['SECRET_KEY'] = '1234'

mongo = PyMongo(app)


@app.template_filter('formatdatetime')
def format_datetime(value):
    if value is None:
        return ""

    now_timestamp = time.time()
    offset = datetime.fromtimestamp(
        now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    value = datetime.fromtimestamp((int(value) / 1000)) + offset

    return value.strftime('%m/%d %H:%M')


@app.route("/view")
def board_view():
    idx = request.args.get("idx")

    if idx is not None:
        board = mongo.db.board
        data = board.find_one({"_id": ObjectId(idx)})
        if data is not None:
            result = {
                "id": data.get("_id"),
                "name": data.get("name"),
                "title": data.get("title"),
                "contents": data.get("contents"),
                "pubdate": data.get("pubdate"),
                "writer_id": data.get("writer_id", "")
            }

            return render_template("view.html", result=result)
    return abort(404)


@app.route("/write", methods=["GET", "POST"])
def board_write():
    if request.method == "POST":
        name = request.form.get("name")
        writer_id = session.get("id")
        title = request.form.get("title")
        contents = request.form.get("contents")
        current_utc_time = round(datetime.utcnow().timestamp() * 1000)
        board = mongo.db.board

        post = {
            "writer_id": writer_id,
            "name": name,
            "title": title,
            "contents": contents,
            "pubdate": current_utc_time,
        }
        print(post)
        x = board.insert_one(post)
        
        return redirect(url_for("lists"))
    else:
        return render_template("write.html")


@app.route("/list")
def lists():
    query = {}

    board = mongo.db.board
    datas = board.find(query)

    return render_template(
        "list.html",
        datas=list(datas),
    )


@app.route("/edit/<idx>", methods=["GET", "POST"])
def board_edit(idx):
    if request.method == "GET":
        board = mongo.db.board
        data = board.find_one({"_id": ObjectId(idx)})
        if data is None:
            flash("해당 게시물이 존재하지 않습니다.")
            return redirect(url_for("lists"))
        else:
            return render_template("edit.html", data=data)

    else:
        title = request.form.get("title")
        contents = request.form.get("contents")
        board = mongo.db.board

        board.update_one({"_id": ObjectId(idx)}, {
            "$set": {
                "title": title,
                "contents": contents,
            }
        })
        return redirect(url_for("board_view", idx=idx))


@app.route("/delete/<idx>")
def board_delete(idx):
    board = mongo.db.board
    board.delete_one({"_id": ObjectId(idx)})
    return redirect(url_for("lists"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9090)
