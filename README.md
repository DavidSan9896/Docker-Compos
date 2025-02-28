--David Santiago Cubillos Méndez
!!Nota !!
tener en cuenta en qué puerto se van a correr ya que si tenes algo corriendo en el puerto te va afectar
tienen dos opciones uno pausar el proceso del puerto 5432 que es el que se necesita para que funcione el programa ya en tu caso seria verificar com pausar el proceso del servicio que tengas o dos cambiar el número de puerto en los siguientes documentos 

en el app.py 

en la linea 6 en este codigo app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:9896@db:5432/students_db'
 y en el docker-compose.yml 
 en esta parte 
 
   db:
    image: postgres:13
    container_name: students_db
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: 9896
      POSTGRES_DB: students_db
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data



# Docker-Compos
Introducción a Docker Compose y Conexión con una Base de Datos

Primero vamos a entra con el comando cd hast la carpta flask_app tiene que verse asi una ruta 
![image](https://github.com/user-attachments/assets/4ea8a1ef-8397-4c96-a3b1-e6d7e78a4e12)

Cunado ya estemos adentro ejecutamos el sgueinete comando 

sudo docker-compose up -d --build
 
Lo que inicasiar los contenedores 

![image](https://github.com/user-attachments/assets/9430e846-71ad-4a58-b83e-39c5457a5325)

Para verificar que esta corriendo con el comando de enlitaccion que es 
sudo docker ps , tieen que aparecer dos 

![image](https://github.com/user-attachments/assets/e99b63c0-5e2c-4d39-88d7-fa87e96bee97)

eso quiere decir que ya esta funcionando para saber si contien estudiantes vamos a usar el comando 
curl http://localhost:5000/students

si nos sale un [] esta vacio para agrega alguin usamos el sguiente comando 
Podemos ponerle los datos que queramos en micaso fueron esos 

curl -X POST http://localhost:5000/students \
     -H "Content-Type: application/json" \
     -d '{"nombre": "David", "edad": 25, "carrera": "sistemas"}' 

![image](https://github.com/user-attachments/assets/6e5ad708-c849-42aa-a26d-379ce4ebcba7)


ya quedo agregado ahora usaremos el aterior comando de curl http://localhost:5000/students
para ver el estudiante 

![image](https://github.com/user-attachments/assets/80ef5553-fc8f-4cfd-85fa-d723b56a99a3)

ya estaria, pero como sabemos que funciono en la base de datos pues en otra terminal para mayor comodida ponmos lo siguiente 

sudo docker exec -it students_db psql -U myuser -d students_db

ya con eso entramos a la base de datos y bamos hacer una consulta de la lista de las tablas 

  \dt

  ![image](https://github.com/user-attachments/assets/3334e885-0d34-45f1-a2bd-6be7ca413528)

y tenemos nuestra tabla y para ver a un estudiante hacemos la consulta que es 

SELECT * FROM student;

y tenemos a nuestro estudiante 

![image](https://github.com/user-attachments/assets/f22cd3cd-9868-434d-8a47-6431dc19cc28)

para editar

usamos el siguiente comando seguir las recomendacciones segun el ide del estudiante poner .../students/2 su ide correspondinet y sus datos antrento de la llave los cuales se van a cambiar 

curl -X PUT http://localhost:5000/students/2 -H "Content-Type: application/json" -d '{ "id": 2,
"nombre": "David", "edad": 35, "carrera": "Artes" }'

![image](https://github.com/user-attachments/assets/ab82a9a3-a247-4dd0-b776-0b68c19d7dba)

hacemos la consulta en la base de datos cn el comando anterior y tambien con el del curl 
![image](https://github.com/user-attachments/assets/19c83c54-c431-46c2-bd8e-d1cd3a189142)

![image](https://github.com/user-attachments/assets/de065088-d7f6-4363-ac51-c96831948e98)

en los dos casos se actualiso 

Ahora para eliminar 
Usamos el comando y tener en cuenta poner el id como ya menione y los datos a borrar usar la informaccion mas reciente 

curl -X DELETE http://localhost:5000/students/2 -H "Content-Type: application/json" -d '{ "id": 2,
"nombre": "David", "edad": 35, "carrera": "Artes" }'
Parese que si se borro 
![image](https://github.com/user-attachments/assets/c53ea2e0-5980-463c-85cd-4865edf2b671)

ahora vamos a verificar en los dos caasos base y terminal 

![image](https://github.com/user-attachments/assets/1f79cb45-e184-4e9c-b9cb-d68aa45e3a4d)

![image](https://github.com/user-attachments/assets/be23a31c-179f-4a6b-a1fc-7ac112ec0834)

En los dos casos ya no esta


 





 
