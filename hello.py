from flask import Flask, jsonify, request
# get, para recupear informacion del servidor
# post, envia datos al servidor
# delete, elimina uno o mas recursos en el servidor
# put , todos-actualizar un recurso en un servidor
# path, uno-para actualizar parcialmente un recurso en el servidor.
app = Flask(__name__)

students = ['Adrian', 'Hiram', 'Reykel', 'Magaly']

students2 =[ 
    {
    'id':1,
    'name':'luis',
    'age':20
    },
     {
    'id':2,
    'name':'Maria',
    'age':25
    }
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/oplesk")
def social_oplesk():
    return "<h1>Hello, from oplesk!</h1>"

@app.route("/students", methods=['GET'])
def get_students():
    return jsonify(students)

@app.route("/createstudents2", methods=['POST'])
def create_students2():
    data = request.json
    students2.append(data)
    return jsonify( { 'message': 'Estudiante creado correctamente', 'Todos los estudiantes son : ': students2})
    
   
@app.route("/delete-students", methods=['DELETE'])
def delete_all_students():
    print( { 'message': 'Valor de Students antes de borrarlo a todos', 'los estudiantes son : ': students})
    students.clear()
    return jsonify( { 'message': 'Estudiantes borrado correctamente', 'Todos los estudiantes son : ': students})

# agregar aqui el minulo 32 del ultimo video

@app.route("/students/<int:student_id>", methods=['PATCH'])
def get_students_by_id(student_id):
    for student in students2:
        if student.get('id') == student_id:
            return jsonify(students2)
    return jsonify( { 'message': 'Estudiantes no econtrado'})
