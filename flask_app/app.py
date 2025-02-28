from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:9896@db:5432/students_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    carrera = db.Column(db.String(100), nullable=False)

@app.route('/students', methods=['GET'])
def list_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'nombre': s.nombre, 'edad': s.edad, 'carrera': s.carrera} for s in students])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'nombre': new_student.nombre, 'edad': new_student.edad, 'carrera': new_student.carrera}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if student:
        data = request.get_json()

        student.nombre = data.get('nombre', student.nombre)
        student.edad = data.get('edad', student.edad)
        student.carrera = data.get('carrera', student.carrera)
        db.session.commit()
        return jsonify({'message': 'Student updated'}), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted'}), 200
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
