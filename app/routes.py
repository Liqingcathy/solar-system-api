from flask import Blueprint, jsonify,  make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, size):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.size = size
        
# planets = [
#     Planet(1, "Mercury", "The smallest planet in our solar system and cloest to the Sun", 4780),
#     Planet(2, "Venus", "The second planet from the Sun and is Earth’s closest planetary neighbor.", 12104),
#     Planet(3, "Earth", "The only place we know of so far that’s inhabited by living things." , 12756),
#     Planet(4, "Mars", "A dusty, cold, desert world with a very thin atmosphere",6780),
#     Planet(5, "Jupiter", "Twice as massive than the other planets of our solar system combined.", 139822),
#     Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings.",116464),
#     Planet(7, "Uranus", "An ice giant, the only planet that spins on its side.", 50724 ),
#     Planet(8, "Neptune", "The eighth and farthest-known Solar planet from the Sun", 49248)
# ]

#blueprint 
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET", "POST"])
def create_and_read_planet():
    if request.method == "GET":
        planets = Planet.query.all()
        planet_response = []
        for planet in planets:
            planet_response.append({
                "order_from_sun": planet.order_from_sun,
                "name": planet.name,
                "desc": planet.desc,
                "size": planet.size
            })
        return jsonify(planet_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(order_from_sun=request_body["order_from_sun"] , name = request_body["name"], desc = request_body["desc"], size = request_body["size"])
        db.session.add(new_planet)
        db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

# @planets_bp.route("", methods=["GET"])
# def get_all_planets():
#     res = []
#     for planet in planets:
#         res.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "size": planet.size
#         })
        
#     return jsonify(res)


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


# #@planets_bp.route("/<id_planet>", methods=["GET"])
# def get_one_planet_by_id(id_planet):
#     """
#     Above function handles all errors like 404, 400, etc. 
#     Below function is for practicing seperate 400, 404, 200 error handlings. 
#     Our program doesn't trige the below funciton at all.
#     """
#     try:
#         id_planet = int(id_planet)
#     except ValueError:
#         rsp={"message": f"Invalid id: {id_planet}"}
#         return jsonify(rsp), 400
#     for planet in planets:
#         if planet.id == id_planet:
#             return jsonify({
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "size": planet.size
#             }), 200
#     return jsonify({"message": f"Planet {id_planet} not found."}), 404
