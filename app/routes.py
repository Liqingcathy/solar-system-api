from crypt import methods
from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, size):
        self.id = id
        self.name = name
        self.description = description
        self.size = size
        
planets = [
    Planet(1, "Mercury", "The smallest planet in our solar system and cloest to the Sun", 4780),
    Planet(2, "Venus", "The second planet from the Sun and is Earth’s closest planetary neighbor.", 12104),
    Planet(3, "Earth", "The only place we know of so far that’s inhabited by living things." , 12756),
    Planet(4, "Mars", "A dusty, cold, desert world with a very thin atmosphere",6780),
    Planet(5, "Jupiter", "Twice as massive than the other planets of our solar system combined.", 139822),
    Planet(6, "Saturn", "Adorned with a dazzling, complex system of icy rings.",116464),
    Planet(7, "Uranus", "An ice giant, the only planet that spins on its side.", 50724 ),
    Planet(8, "Neptune", "The eighth and farthest-known Solar planet from the Sun", 49248)
]

#blueprint 
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    res = []
    for planet in planets:
        res.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "size": planet.size
        })
        
    return jsonify(res)

@planets_bp.route("/<input_planet>", methods=["GET"])
def get_one_planet(input_planet):
    for planet in planets:
        if str(planet.id) == input_planet or planet.name.lower() == input_planet.lower():
            return jsonify({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size
            }), 200
    return jsonify({"message": f"Planet {input_planet} not found."}), 404

#there is a second version to practice 400 code
@planets_bp.route("/<id_planet>", methods=["GET"])
def get_one_planet_by_id(id_planet):
    try:
        id_planet = int(id_planet)
    except ValueError:
        rsp={"message": f"Invalid id: {id_planet}"}
        return jsonify(rsp), 400
    for planet in planets:
        if planet.id == id_planet:
            return jsonify({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "size": planet.size
            }), 200
    return jsonify({"message": f"Planet {id_planet} not found."}), 404
