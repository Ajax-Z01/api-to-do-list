from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Checklist, ChecklistItem

api = Blueprint('api', __name__)

# 3️. Buat Checklist
@api.route('/checklist', methods=['POST'])
@jwt_required()
def create_checklist():
    if not request.is_json:
        print("Error: Request body is not JSON")
        return jsonify({"error": "Request body must be JSON"}), 400

    data = request.get_json()
    print(f"Received data: {data}")

    user_id = get_jwt_identity()
    print(f"User ID: {user_id}")

    if not data or "title" not in data:
        print("Error: Title is missing")
        return jsonify({"error": "Title is required"}), 422

    new_checklist = Checklist(title=data['title'], user_id=user_id)
    db.session.add(new_checklist)
    db.session.commit()

    print(f"Checklist created: {new_checklist.id}, {new_checklist.title}")

    return jsonify({'id': new_checklist.id, 'title': new_checklist.title}), 201


# 4️. Hapus Checklist
@api.route('/checklist/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_checklist(id):
    checklist = Checklist.query.get_or_404(id)
    db.session.delete(checklist)
    db.session.commit()

    return jsonify({'message': 'Checklist deleted'}), 200

# 5️. Tampilkan Semua Checklist
@api.route('/checklist', methods=['GET'])
@jwt_required()
def get_checklists():
    user_id = get_jwt_identity()
    checklists = Checklist.query.filter_by(user_id=user_id).all()
    
    return jsonify([
        {'id': c.id, 'title': c.title} for c in checklists
    ])

# 6️. Detail Checklist
@api.route('/checklist/<int:id>', methods=['GET'])
@jwt_required()
def get_checklist_detail(id):
    checklist = Checklist.query.get_or_404(id)
    
    return jsonify({
        'id': checklist.id,
        'title': checklist.title,
        'items': [{'id': item.id, 'name': item.name, 'is_done': item.is_done} for item in checklist.items]
    })

# 7️. Buat Item dalam Checklist
@api.route('/checklist/<int:checklist_id>/items', methods=['POST'])
@jwt_required()
def create_item(checklist_id):
    data = request.get_json()
    
    new_item = ChecklistItem(name=data['name'], checklist_id=checklist_id)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'id': new_item.id, 'name': new_item.name, 'is_done': new_item.is_done}), 201

# 8️. Detail Item dalam Checklist
@api.route('/items/<int:item_id>', methods=['GET'])
@jwt_required()
def get_item_detail(item_id):
    item = ChecklistItem.query.get_or_404(item_id)
    
    return jsonify({'id': item.id, 'name': item.name, 'is_done': item.is_done})

# 9. Update Item dalam Checklist
@api.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    data = request.get_json()
    item = ChecklistItem.query.get_or_404(item_id)

    item.name = data.get('name', item.name)
    db.session.commit()

    return jsonify({'message': 'Item updated'})

# 10. Ubah Status Item (Done/Undone)
@api.route('/items/<int:item_id>/status', methods=['PATCH'])
@jwt_required()
def toggle_item_status(item_id):
    item = ChecklistItem.query.get_or_404(item_id)

    item.is_done = not item.is_done
    db.session.commit()

    return jsonify({'message': 'Item status updated'})

# 11. Hapus Item dari Checklist
@api.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    item = ChecklistItem.query.get_or_404(item_id)

    db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Item deleted'})
