from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    order = {
        "order_id": len(orders) + 1,
        "item": data.get("item"),
        "status": "Order Placed"
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"all_orders": orders})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002) # Port 5002-ൽ റൺ ചെയ്യുന്നു