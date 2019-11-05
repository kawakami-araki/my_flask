from flask import Blueprint,render_template,url_for,redirect
import app_sql

note_bp = Blueprint('note_bp',__name__,url_prefix='/note')

@note_bp.route('/<int:num>',methods=['GET','PORT'])
def note(num):
    app_list = app_sql.session.query(app_sql.Subordinate_forces).offset(num*10).limit(10).all()
    num += 1
    return render_template('note.html',my_list=app_list,num=num)


# @note_bp.route('/<int:comony>',methods=['GET','PORT'])
# def note(comony):
#     app_list = app_sql.session.query(app_sql.Subordinate_forces).offset(num*10).limit(10)[0]
#     return render_template('note.html')