from flask import Blueprint,render_template
from database.cliente import CLIENTS

client_route = Blueprint('client_route',__name__)
"""
client routes
    
    - /clients/(GET)
     - /clients/(POST)
      - /clients/new - render form to create c;ient
       - /clients/<id> - get once client by id
        - /clients/<id>/edit - 
         - /clients/<id>/update (PUT)
          - /clients/<id>/delete -(DELETE) delete client
"""
@client_route.route('/')
def client_list():
    return render_template('clientlist.html',clients=CLIENTS)



@client_route.route('/',methods=['POST'])
#insert on db
def client_insert():
    return {'page':'client insert'}



@client_route.route('/new',methods=['GET'])
#create client
def client_create():
    return render_template('clientform.html')


@client_route.route('/<int:client_id>')
#show client info
def client_details():
    return render_template('clientdetails.html')



@client_route.route('/<int:client_id>/edit')
#edit form client
def client_edit():
    return render_template('clienteditform.html')


@client_route.route('/<int:client_id>/update',methods=['PUT'])
#update client info
def client_update():
    return {'page':'client update'}


@client_route.route('/<int:client_id>/delete')
#delete client
def client_delete():
    return {'page':'client delete'}


