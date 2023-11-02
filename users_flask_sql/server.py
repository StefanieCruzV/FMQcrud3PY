from cgitb import html
from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all() # regresa los valores del metodo get all y almacena todos los datos de lbd
    print(users)
    return render_template("users.html",users=users) 

@app.route("/newuser")
def newuser():
    return render_template("newuser.html")
 
 

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "uname": request.form["uname"],
        "ulastname": request.form["ulastname"],
        "uemail": request.form["uemail"]
        # guarda los valores del formulario
        }
   
    id=User.save(data) # manda llamar al metodo para guardar
    print(id)
   
    return redirect(f"/show_user/{id}")# lo que me regreso de la base al html
        # si es otra pagina 

@app.route('/delete_user/<int:id>')
def delete_user(id):
    print(id)
    data = {
        "id": id
        }
    User.delete(data)
    users = User.get_all()
    return render_template("users.html",users=users)
   


@app.route('/show_user/<int:id>')
def show_user(id):
    print(id)
    data = {
        "id": id,
    
        }
    user_id = User.get_user_by_id(data)
    print(user_id)
    return render_template("showuser.html",user= user_id) # lo que me regreso de la base al html
        # si es otra pagina 

@app.route('/update_user/<int:id>')
def update_user(id):
    print(id)
    data = {
        "id": id
        }
    user_id = User.get_user_by_id(data)
    print(user_id)
    return render_template("updateuser.html",user_id= user_id) # lo que me regreso de la base al html
        # si es otra pagina 

@app.route('/update_user/<int:id>', methods=["POST"])
def update_user_post(id):
    print(id)
    data = {
        "id": id,
        "uname": request.form["uname"],
        "ulastname": request.form["ulastname"],
        "uemail": request.form["uemail"]
        }
    User.update(data)
    print(f"/show_user/{id}")
    return redirect(f"/show_user/{id}") # lo que me regreso de la base al html
        # si es otra pagina 


if __name__ == "__main__":
    app.run(debug=True)

            
