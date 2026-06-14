from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

    
app = Flask(__name__)
mysql = MySQL(app)

#configurar jwt
app.config['JWT_SECRET_KEY'] = '123'
jwt = JWTManager(app)

#Conexion a la BD tienda_db
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "gestionbecas_db"

#------------------------Paginas HTML------------------
@app.route('/')
def inicio():
    return render_template("index.html") 
@app.route('/becas_html')
def becas_html():
    return render_template("becas.html") 
@app.route('/consultas_html')
def consultas_html():
    return render_template("consultas.html") 
@app.route('/documentos_html')
def documentos_html():
    return render_template("documentos.html") 
@app.route('/estudiantes_html')
def estudiantes_html():
    return render_template("estudiantes.html") 
@app.route('/postulaciones_html')
def postulaciones_html():
    return render_template("postulaciones.html") 

#---------------------------------login---------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'admin' and password == '123':
        token = create_access_token(identity = username)
        return jsonify(access_token=token)
    return jsonify({"error":"credenciales incorrectas"}), 401
#--------------------------------GET------------------------
@app.route('/becas', methods=['GET'])
def listar_becas():
    cursor = mysql.connection.cursor()
    sql = "select id_beca, nombre_beca, descripcion, gestion, promedio_minimo from becas"
    cursor.execute(sql)
    datos = cursor.fetchall()

    beca = []
    for fila in datos:
        beca.append(
            {
                "id_beca": fila[0],
                "nombre_beca":fila[1],
                "descripcion":fila[2],
                "gestion":fila[3],
                "promedio_minimo":fila[4]
            }
        )
    cursor.close()
    return jsonify(beca)

@app.route('/documentos', methods=['GET'])
def listar_ducumento():
    cursor = mysql.connection.cursor()
    sql = "select id_documento, id_postulacion, tipo_documento, url_archivo from documentos "
    cursor.execute(sql)
    datos = cursor.fetchall()

    documento = []
    for fila in datos:
        documento.append(
            {
                "id_documento": fila[0],
                "id_postulacion":fila[1],
                "tipo_documento":fila[2],
                "url_archivo":fila[3]
            }
        )
    cursor.close()
    return jsonify(documento)

@app.route('/estudiantes', methods=['GET'])
def listar_estudiante():
    cursor = mysql.connection.cursor()
    sql = "select id_estudiante, nombres, apellidos, carrera,promedio_acumulado from estudiantes "
    cursor.execute(sql)
    datos = cursor.fetchall()

    estudiante = []
    for fila in datos:
        estudiante.append(
            {
                "id_estudiante": fila[0],
                "nombres":fila[1],
                "apellidos":fila[2],
                "carrera":fila[3],
                "promedio_acumulado":fila[4]
            }
        )
    cursor.close()
    return jsonify(estudiante)

@app.route('/postulaciones', methods=['GET'])
def listar_postulacion():
    cursor = mysql.connection.cursor()
    sql = "select id_postulacion, id_estudiante,id_beca,fecha_postulacion, estado , observaciones from postulaciones "
    cursor.execute(sql)
    datos = cursor.fetchall()

    postulacion = []
    for fila in datos:
        postulacion.append(
            {
                "id_postulacion": fila[0],
                "id_estudiante":fila[1],
                "id_beca":fila[2],
                "fecha_postulacion":fila[3],
                "estado":fila[4],
                "observaciones":fila[5]
            }
        )
    cursor.close()
    return jsonify(postulacion)
#-----------------------------POST-----------------------------
@app.route('/becas', methods=['POST'])
@jwt_required()
def insertar_beca():
    data = request.get_json()
    nombre_beca = data["nombre_beca"]
    descripcion = data["descripcion"]
    gestion = data["gestion"]
    promedio_minimo = data["promedio_minimo"]
    
    #insertar en la tabla categoria
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO becas(nombre_beca,descripcion, gestion, promedio_minimo )
            VALUES(%s,%s,%s,%s)"""
    cursor.execute(sql, (nombre_beca,descripcion, gestion, promedio_minimo,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "beca registrada con exito"}),201

@app.route('/documentos', methods=['POST'])
@jwt_required()
def insertar_documendos():
    data = request.get_json()
    id_postulacion= data["id_postulacion"]
    tipo_documento = data["tipo_documento"]
    url_archivo = data["url_archivo"]
    
    #insertar en la tabla categoria
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO documentos (id_postulacion, tipo_documento,url_archivo )
            VALUES(%s,%s,%s)"""
    cursor.execute(sql, (id_postulacion,tipo_documento,url_archivo,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "documendos registrada con exito"}),201

@app.route('/estudiantes', methods=['POST'])
@jwt_required()
def insertar_estudiante():
    data = request.get_json()
    id_estudiante=data["id_estudiante"]
    nombres= data["nombres"]
    apellidos = data["apellidos"]
    carrera= data["carrera"]
    promedio_acumulado=data["promedio_acumulado"]
    
    #insertar en la tabla categoria
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO estudiantes (id_estudiante ,nombres, apellidos, carrera ,promedio_acumulado )
            VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (id_estudiante,nombres,apellidos,carrera,promedio_acumulado,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "estudiante registrada con exito"}),201

@app.route('/postulaciones', methods=['POST'])
@jwt_required()
def insertar_postulacion():
    data = request.get_json()
    id_estudiante= data["id_estudiante"]
    id_beca = data["id_beca"]
    fecha_postulacion= data["fecha_postulacion"]
    estado=data["estado"]
    observaciones=data["observaciones"]
    
    #insertar en la tabla categoria
    cursor = mysql.connection.cursor()
    sql = """INSERT INTO postulaciones (id_estudiante, id_beca, fecha_postulacion, estado,observaciones )
            VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(sql, (id_estudiante,id_beca,fecha_postulacion,estado,observaciones))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "postulacion registrada con exito"}),201
#------------------------------------PUT----------------------------
@app.route('/becas/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_becas(id):
    
    data = request.get_json()
    nombre_beca = data["nombre_beca"]
    descripcion = data["descripcion"]
    gestion = data["gestion"]
    promedio_minimo = data["promedio_minimo"]

    cursor = mysql.connection.cursor()
    sql = """UPDATE becas
              SET nombre_beca = %s,   descripcion= %s,  gestion= %s, promedio_minimo = %s
              WHERE id_beca = %s"""

    cursor.execute(sql, (nombre_beca,descripcion,gestion,promedio_minimo, id,))

    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Beca actualizado correctamente"}), 200
@app.route('/documentos/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_documendo(id):
    
    data = request.get_json()
    id_postulacion= data["id_postulacion"]
    tipo_documento = data["tipo_documento"]
    url_archivo = data["url_archivo"]

    cursor = mysql.connection.cursor()
    sql = """UPDATE documentos
              SET id_postulacion = %s, tipo_documento= %s,  url_archivo= %s
              WHERE id_documento = %s"""

    cursor.execute(sql, (id_postulacion,tipo_documento,url_archivo, id,))

    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "documendos actualizado correctamente"}), 200
@app.route('/estudiantes/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_estudiante(id): 
    data = request.get_json()
    id_estudiante=data["id_estudiante"]
    nombres= data["nombres"]
    apellidos = data["apellidos"]
    carrera= data["carrera"]
    promedio_acumulado=data["promedio_acumulado"]
    cursor = mysql.connection.cursor()
    sql = """UPDATE estudiantes
              SET id_estudiante=%s, nombres = %s, apellidos= %s,  carrera= %s, promedio_acumulado= %s
              WHERE id_estudiante = %s"""

    cursor.execute(sql, (id_estudiante,nombres,apellidos,carrera,promedio_acumulado, id,))

    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "estudiante actualizado correctamente"}), 200

@app.route('/postulaciones/<int:id>', methods=['PUT'])
@jwt_required()
def actualizar_postulacion(id): 
    data = request.get_json()
    id_estudiante= data["id_estudiante"]
    id_beca = data["id_beca"]
    fecha_postulacion= data["fecha_postulacion"]
    estado=data["estado"]
    observaciones=data["observaciones"]
    cursor = mysql.connection.cursor()
    sql = """UPDATE postulaciones
              SET id_estudiante = %s, id_beca= %s,  fecha_postulacion= %s, estado= %s, observaciones=%s
              WHERE id_postulacion = %s"""

    cursor.execute(sql, (id_estudiante,id_beca,fecha_postulacion,estado,observaciones, id,))

    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "postulacion actualizado correctamente"}), 200
#-------------------------------------------DELETE----------------------------
@app.route('/becas/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_beca(id):
    cursor = mysql.connection.cursor()
    #BUSCAR EL CATEGORIA
    sql = """SELECT * FROM becas WHERE id_beca = %s"""
    cursor.execute(sql, (id,))
    datos = cursor.fetchone()

    if datos is None:
        return jsonify({"mensaje": "la beca no existe!"})
    
    #cursor = mysql.connection.cursor()
    sql = """DELETE FROM becas
            WHERE id_beca = %s"""
    cursor.execute(sql,(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "beca Eliminada"}),200

@app.route('/documentos/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_documento(id):
    cursor = mysql.connection.cursor()
    #BUSCAR EL CATEGORIA
    sql = """SELECT * FROM documentos WHERE id_documento = %s"""
    cursor.execute(sql, (id,))
    datos = cursor.fetchone()

    if datos is None:
        return jsonify({"mensaje": "el documendo no existe!"})
    
    #cursor = mysql.connection.cursor()
    sql = """DELETE FROM documentos
            WHERE id_documento = %s"""
    cursor.execute(sql,(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "documento Eliminada"}),200
@app.route('/estudiantes/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_estudiante(id):
    cursor = mysql.connection.cursor()
    #BUSCAR EL CATEGORIA
    sql = """SELECT * FROM estudiantes WHERE id_estudiante = %s"""
    cursor.execute(sql, (id,))
    datos = cursor.fetchone()

    if datos is None:
        return jsonify({"mensaje": "el estudiante no existe!"})
    
    #cursor = mysql.connection.cursor()
    sql = """DELETE FROM estudiantes
            WHERE id_estudiante = %s"""
    cursor.execute(sql,(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "estudiantes Eliminada"}),200

@app.route('/postulaciones/<int:id>', methods=['DELETE'])
@jwt_required()
def eliminar_postulacion(id):
    cursor = mysql.connection.cursor()
    #BUSCAR EL CATEGORIA
    sql = """SELECT * FROM postulaciones WHERE id_postulacion = %s"""
    cursor.execute(sql, (id,))
    datos = cursor.fetchone()

    if datos is None:
        return jsonify({"mensaje": "la postulacion no existe!"})
    
    #cursor = mysql.connection.cursor()
    sql = """DELETE FROM postulaciones
            WHERE id_postulacion = %s"""
    cursor.execute(sql,(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "postulacion  Eliminada"}),200

#------------------------------CONSULTAS LOPEZ-----------------------------

@app.route('/consultas/pendientes', methods=['GET'])
def consulta_pendientes():
    cursor = mysql.connection.cursor()
    sql = """
        SELECT 
            p.id_postulacion,
            e.nombres,
            e.apellidos,
            b.nombre_beca,
            p.fecha_postulacion,
            p.estado
        FROM postulaciones p
        JOIN estudiantes e ON p.id_estudiante = e.id_estudiante
        JOIN becas b ON p.id_beca = b.id_beca
        WHERE p.estado = 'Pendiente'
        ORDER BY p.fecha_postulacion ASC
    """
    cursor.execute(sql)
    datos = cursor.fetchall()

    resultado = []
    for fila in datos:
        resultado.append({
            "id_postulacion": fila[0],
            "nombres": fila[1],
            "apellidos": fila[2],
            "nombre_beca": fila[3],
            "fecha_postulacion": str(fila[4]),
            "estado": fila[5]
        })
    cursor.close()
    return jsonify(resultado)
#------------------------------CONSULTAS LOPEZ-----------------------------

if __name__ == '__main__':
    app.run(debug=True)