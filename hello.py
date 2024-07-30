from flask import Flask, jsonify, request
# get, para recupear informacion del servidor
# post, envia datos al servidor
# delete, elimina uno o mas recursos en el servidor
# put , todos-actualizar un recurso en un servidor
# path, uno-para actualizar parcialmente un recurso en el servidor.
app = Flask(__name__)

students = ['Adrian', 'Hiram', 'Reykel', 'Magaly']

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/oplesk")
def social_oplesk():
    return "<p>Hello, from oplesk!</p>"

@app.route("/students", methods=['GET'])
def get_students():
    return jsonify(students)

@app.route("/create-students", methods=['POST'])
def create_students():
    data = request.json
    students.append(data)
    return jsonify( { 'message': 'Estudiante creado correctamente', 'Todos los estudiantes son : ': students})
    
# @app.route("/delete-students", methods=['DELETE'])
# def delete_students():
#     data = request.json
#     students.append(data)
#     return jsonify( { 'message': 'Estudiante creado correctamente', 'Todos los estudiantes son : ': students})
    
