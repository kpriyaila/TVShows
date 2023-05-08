from flask import Flask, render_template,redirect,session,request
from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User


@app.route('/shows/new')
def create():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template("new.html", user=User.get_by_id(data))

@app.route('/shows/add',methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        data = {
        "id":session['user_id']
    }
        return render_template("new.html", user=User.get_by_id(data))
    data ={ 
        "title": request.form['title'],
        "description": request.form['description'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "users_id": session['user_id']
    }
    id = Show.save(data)
    return redirect('/dashboard')

@app.route('/delete/show/<int:id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Show.delete(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }    
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_show.html",show=Show.get_by_id(data),user=User.get_by_id(user_data))

@app.route('/edit/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_show.html",show=Show.get_by_id(data),user=User.get_by_id(user_data))

@app.route('/shows/update',methods=['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Show.validate_show(request.form):
        return redirect('/shows/add')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "users_id": session['user_id'],
        "id": request.form['id']
    }
    Show.update(data)
    return redirect('/dashboard')

