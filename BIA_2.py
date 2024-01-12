from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

app = Flask(__name__) 
api = Api(app) 

# making a class for a particular resource 
class Hello(Resource): 

	def get(self): 

		return jsonify({'message': 'Hello, World!'}) 

	# Corresponds to POST request 
	def post(self): 
		
		data = request.get_json()	  
		return jsonify({'data': data}), 201


# another resource to calculate the addition of a number by 10 
class addition(Resource): 

	def get(self, num): 

		return jsonify({'addition': num+10}) 


# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(addition, '/addition/<int:num>') 

# Run the Flask application
if __name__ == '__main__': 

	app.run(debug = True) 
