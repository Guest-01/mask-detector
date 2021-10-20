import os

from flask import Blueprint, flash, render_template, request
from werkzeug.utils import secure_filename

from mask_detector import BASE_DIR

from .detector import load_detect_save

bp = Blueprint("main", __name__)

imgpath = os.path.join(BASE_DIR, "static/userimg")


@bp.route("/")
def home():
    print(imgpath)
    return render_template("home.html")


@bp.route("/detect", methods=["GET", "POST"])
def detect():
    if request.method == "POST":
        f = request.files.get("formFile")
        if not f:  # no files
            flash("이미지 파일을 업로드해주세요")
            return render_template("detect.html")
        # remove prev imgs
        for file in os.scandir(imgpath):
            os.remove(file.path)
        f_name = secure_filename(f.filename)
        img_path = os.path.join(imgpath, f_name)
        f.save(img_path)
        load_detect_save(imgpath, f_name)
        return render_template("detect.html", img=f_name)
    return render_template("detect.html")
