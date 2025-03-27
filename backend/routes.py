from flask import Blueprint, request, jsonify
from database import collection
from bson import ObjectId
from datetime import datetime

blog_routes = Blueprint("blog_routes", __name__)

# Create Post
@blog_routes.route("/posts", methods=["POST"])
def add_post():
    data = request.json
    
    # Validate required fields
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    if "title" not in data or "content" not in data:
        return jsonify({"error": "Title and content are required"}), 400
    
    # Add metadata
    data['created_at'] = datetime.utcnow().isoformat()
    data['updated_at'] = datetime.utcnow().isoformat()
    
    # Insert post
    result = collection.insert_one(data)
    
    return jsonify({
        "message": "Post added successfully", 
        "post_id": str(result.inserted_id)
    }), 201

# Read All Posts
@blog_routes.route("/posts", methods=["GET"])
def get_posts():
    # Retrieve all posts and convert ObjectId to string
    posts = list(collection.find())
    for post in posts:
        post['_id'] = str(post['_id'])
    
    return jsonify(posts)

# Read Single Post by ID
@blog_routes.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    try:
        # Convert string ID to ObjectId
        post = collection.find_one({"_id": ObjectId(post_id)})
        
        if post:
            post['_id'] = str(post['_id'])
            return jsonify(post)
        
        return jsonify({"error": "Post not found"}), 404
    
    except:
        return jsonify({"error": "Invalid post ID"}), 400

# Update Post
@blog_routes.route("/posts/<post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.json
    
    # Validate input
    if not data:
        return jsonify({"error": "No update data provided"}), 400
    
    # Add update timestamp
    data['updated_at'] = datetime.utcnow().isoformat()
    
    try:
        # Update post
        result = collection.update_one(
            {"_id": ObjectId(post_id)}, 
            {"$set": data}
        )
        
        if result.modified_count:
            return jsonify({"message": "Post updated successfully"}), 200
        
        return jsonify({"error": "Post not found"}), 404
    
    except:
        return jsonify({"error": "Invalid post ID"}), 400

# Delete Post
@blog_routes.route("/posts/<post_id>", methods=["DELETE"])
def delete_post(post_id):
    try:
        # Delete post
        result = collection.delete_one({"_id": ObjectId(post_id)})
        
        if result.deleted_count:
            return jsonify({"message": "Post deleted successfully"}), 200
        
        return jsonify({"error": "Post not found"}), 404
    
    except:
        return jsonify({"error": "Invalid post ID"}), 400