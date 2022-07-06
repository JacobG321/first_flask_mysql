from flask_app import app
from flask import render_template, request, redirect
# import the class from friend.py
from flask_app.models.friend import Friend

@app.route("/")
def index():
    #this page shows all friends
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    #put the friend.getall method in a variable that has a list of objects
    return render_template("index.html", all_friends=friends)
            

#invisible route
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

#viewable route
@app.route('/add_friend')
def add_friend():
    return render_template('create.html')

#view one page, viewable route
@app.route('/friends/view/<int:id>')
def view_info(id):
    data = {
        "id" : id #need id for query
    }
    return render_template('view_one_friend.html', this_friend = Friend.get_one_friend(data) )

#edit #visible route
@app.route('/friends/edit/<int:id>')
def edit(id):
    data = {
        "id" : id #need id for query
    }
    return render_template('edit_friend.html', this_friend = Friend.get_one_friend(data) )

#edit #invRoute
@app.route('/friends/<int:id>/edit_friend_in_db', methods=["POST"])
def edit_friend_in_db(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"],
        "id" : id #need this to update this specific zoo
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.edit_friend(data)
    return redirect(f'/friends/view/{id}')


#delete
@app.route('/friends/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Friend.delete_friend(data)
    return redirect('/')
