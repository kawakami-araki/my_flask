from flask import Flask,render_template

from blue_prints.note_bp import note_bp

from blue_prints.photos_bp import photos_bp

app = Flask(__name__)

app.register_blueprint(note_bp)

app.register_blueprint(photos_bp)



@app.route('/',methods=['GET','POST'])
def hello_world():
    return render_template('First.html')

# @app.route('/note/',methods=['GET','POST'])
# def note():
#     app_list = app_sql.session.query(app_sql.Subordinate_forces).all()
#     return render_template('note.html',my_list=app_list)

# @app.route('/note/photos/',methods=['GET','POST'])
# def photos():
#     return render_template('Photos.html')

@app.route('/inner',methods=['GET','POST'])
def inner():
    return render_template('Add_roles.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=10001)
