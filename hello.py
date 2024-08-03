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


@app.route("/students2", methods=['GET'])
def get_students2():
    return jsonify(students2)


@app.route("/createstudents2", methods=['POST'])
def create_students2():
    data = request.json
    students2.append(data)
    return jsonify( { 'message': 'Estudiante creado correctamente', 'Todos los estudiantes son : ': students2})
    
#    voy por el minuto 36... del video del profe...
@app.route("/delete-students", methods=['DELETE'])
def delete_all_students():
    print( { 'message': 'Valor de Students antes de borrarlo a todos', 'los estudiantes son : ': students})
    students.clear()
    return jsonify( { 'message': 'Estudiantes borrado correctamente', 'Todos los estudiantes son : ': students})

# Actualiza el primer estudiante de la lista
@app.route("/patch-student" , methods=['PATCH'])
def update_one_student():
    data = request.json
    students2[0].update(data)
    return jsonify( { 'message': 'Estudiantes actualizado correctamente', 'Todos los estudiantes son : ': students2})

#  agregar aqui el minulo 32 del ultimo video

@app.route("/students/<int:student_id>", methods=['GET'])
def get_students_by_id(student_id):
    for student in students2:
        if student.get('id') == student_id:
            return jsonify(student)
    return jsonify( { 'message': 'Estudiantes no econtrado'})

#    voy por el minuto 36... del video del profe...
@app.route("/delete-students2/", methods=['DELETE'])
def delete_student_by_name():
    name = request.args.get('name')
    if name:
        for student in students2:
           if student.get('name')  == name:
               students2.remove(student)
               return jsonify( { 'message': 'Estudiantes borrado correctamente', 'Todos los estudiantes son : ': students2})
        return jsonify( { 'message': 'Estudiantes no encontrado'})
    else:
        return jsonify( { 'message': 'Debes indicar un nombre valido'})
