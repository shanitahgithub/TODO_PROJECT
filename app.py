from flask import Flask,render_template,request,redirect,url_for

# Creating the app instance
app=Flask(__name__,template_folder="templates")

tasks=[]
# Routing
@app.route('/')
def home():
    # The index.html template renders the list of tasks 
    # and provides forms for adding new tasks and deleting existing tasks.
    return render_template("index.html",tasks=tasks)



# Creating a new task
# The /add_task route handles the creation of tasks. When the user Creates a new task, 
# it adds the task to the tasks list and redirects back to the home page.
@app.route('/add_task' , methods=["POST"])
def create_task():
    task = request.form.get("task")
    tasks.append(task)  # Adding task to our list
    return redirect(url_for("home"))

# The /delete_task/<int:task_id> route handles the deletion of tasks.
# When the user clicks the delete button next to a task, it removes the task from the tasks
# list based on the task ID and redirects back to the home page.
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
     del tasks[task_id]
     return redirect(url_for('home'))


@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    updated_task = request.form.get('updated_task')
    if 0 <= task_id < len(tasks):
        tasks[task_id] = updated_task
    return redirect(url_for('home'))


# @app.route('/add_task', methods=["POST"])
# def create_task():
#     # Retrieve task data from the form
#     task = request.form.get("task")
    
#     # Check if the task is already in the list
#     if task in tasks:
#         # If the task exists, update it (if desired)
#         # Example: tasks[tasks.index(task)] = updated_task
#         pass
#     else:
#         # If the task doesn't exist, add it to the list
#         tasks.append(task)
    
#     # Redirect to the home page
#     return redirect(url_for("home"))

# # Route for rendering the home page
# @app.route('/')
# def home():
#     # Render the home page template with the tasks list
#     return render_template("index.html", tasks=tasks)

# Running the Flask app
if __name__ == '__main__':
    app.run(debug=True)


# Enabling the debug mode
if __name__ == '__main__':
    app.run(debug=True)



# <int:task_id>: This is a variable part of the URL.
# It allows you to capture dynamic values from the URL and pass them to your Flask
# view function. In this case, <int:task_id> captures an integer value (hence the <int> part) representing the ID of the task to be deleted.






