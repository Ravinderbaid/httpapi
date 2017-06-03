On one terminal you can start the django app and in another terminal run this command to get the desired output.

curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/team/ -d '{"first_name": "ravinder", "last_name": "baid", "phone": "9879879870", "email": "x@gmail.com"}'

curl -H "Content-Type: application/json" -X PUT http://127.0.0.1:8000/team/1/ -d '{"phone": "9878585500"}'

curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/team/

curl -H "Content-Type: application/json" -X GET http://127.0.0.1:8000/team/1/

curl -X DELETE http://127.0.0.1:8000/team/1/

requirements.txt contains all the libraries I have used to make this repo.
