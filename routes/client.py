from flask import Blueprint,render_template

client_route = Blueprint('client_route',__name__)
"""
client routes
    
    - /clients/
"""
@client_route.route('/')
def client_list():
    return render_template('teste.html')

@client_route.route('/<int:client_id>')
def client_once(client_id):
    # print(client_id)
    return render_template('teste.html')