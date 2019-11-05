from flask import Blueprint,render_template,url_for,redirect
import app_sql

photos_bp = Blueprint('photos_bp',__name__,url_prefix='/photo')

@photos_bp.route('/',methods=['GET','POST'])
def photos():
    return render_template('Photos.html')
