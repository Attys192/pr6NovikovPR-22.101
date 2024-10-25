from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/users/', methods=['GET'])
def returnUserInfo():
    id = int(request.args.get("id"))
    users = {
       1: {
          "name": "ArtemBH",
          "age": 18
       },
        2: {
          "name": "Artem",
          "age": 18
       },
        3: {
          "name": "Nikita",
          "age": 18
       }
    }
    return jsonify(users[id])     
if __name__ == "__main__":
 app.run(debug=True) 
