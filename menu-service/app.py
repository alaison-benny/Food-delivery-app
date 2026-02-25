from flask import Flask, jsonify

app = Flask(__name__)

# ഒരു സാമ്പിൾ മെനു ലിസ്റ്റ്
menu = [
    {"id": 1, "item": "Masala Dosa", "price": 60},
    {"id": 2, "item": "Biriyani", "price": 150},
    {"id": 3, "item": "Appam & Stew", "price": 80}
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify({"restaurant_menu": menu})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) # Port 5001-ൽ റൺ ചെയ്യുന്നു