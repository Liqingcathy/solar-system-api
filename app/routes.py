from os import abort
from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("about", methods=["GET", "POST"])
def about():
    return "The Solar System Project by: Nina, Lin and Liqing. Ada Developers Academy, 2022"

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))

    return planet


@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(order_from_sun=request_body["order from sun"] , name = request_body["name"], desc = request_body["description"], size = request_body["size"])
        
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query=request.args.get("name")
    if name_query:
        planets =Planet.query.filter_by(name=name_query)
    else:
        planets=Planet.query.all()

    res = []
    for planet in planets:
        res.append({
            "id": planet.id,
            "order from sun":planet.order_from_sun,
            "name": planet.name,
            "description": planet.desc,
            "size": planet.size
        })
        
    return jsonify(res)


# @planets_bp.route("/<input_planet>", methods=["GET"])
# def get_one_planet(input_planet):
#     """ 
#        handles all erros wihtout explicitly define 400 message.
#        input examples: /planets/1, /planets/earth, /planets/one ...
#     """
#     for planet in planets:
#         if str(planet.id) == input_planet or planet.name.lower() == input_planet.lower():
#             return jsonify({
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "size": planet.size
#             }), 200
#     return jsonify({"message": f"Planet {input_planet} not found."}), 404


@planets_bp.route("/<id_planet>", methods=["GET"])
def get_one_planet_by_id(id_planet):
    planet=validate_planet(id_planet)
    return {
        "id": planet.id,
        "order from sun":planet.order_from_sun,
        "name": planet.name,
        "description": planet.desc,
        "size": planet.size
        }
    
@planets_bp.route("/<id_planet>", methods=["PUT"])
def update_planet(id_planet):
    planet = validate_planet(id_planet)

    request_body = request.get_json()

    planet.order_from_sun = request_body["order from sun"]
    planet.name = request_body["name"]
    planet.desc = request_body["description"]
    planet.size = request_body["size"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

@planets_bp.route("/<id_planet>", methods=["DELETE"])
def delete_planet(id_planet):
    planet = validate_planet(id_planet)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted")