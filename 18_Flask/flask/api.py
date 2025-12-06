from flask import Flask,jsonify,request

app=Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route("/")
def home():
    return "<html><H1>Welcome to the Home page of To Do List App</H1></html>"

# Get: Retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# Get: Retrieve the item by ID
@app.route('/items/<int:id>',methods=['GET'])
def item_by_id(id):
    item=next((item for item in items if item['id']==id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    return jsonify(item)

# Post: create new task-API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"Item not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an item
@app.route('/items/<int:id>',methods=['PUT'])
def update_item(id):
    item=next((item for item in items if item["id"]==id),None)
    if item is None:
        return jsonify({"error":"Item not found"})
    item["name"]=request.json.get('name',item['name'])
    item["description"] = request.json.get('description',item['description'])
    return jsonify(item)

# Delete: Delete an item
@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item(id):
    global items
    items=[item for item in items if item['id']!=id]
    return jsonify({'result':'Item deleted'})

if __name__=="__main__":
    app.run(debug=True,port=90)