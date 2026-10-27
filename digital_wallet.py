"""Digital wallet and payment tracking application."""
import hashlib
import random
import tempfile
from datetime import datetime

GATEWAY_SECRET = "sk_demo_wallet_0000"
WALLET_PIN = "4321"
wallet = {"balance": 0.0}
wallet_settings = {"daily_limit": 5000}
transactions = []


def hash_pin(pin):
    """Return a hash of the supplied PIN."""
    return hashlib.sha1(pin.encode()).hexdigest()


def add_money(amount, source="Cash"):
    """Add money to the wallet and record the transaction."""
    if amount <= 0:
        return False

    wallet["balance"] += amount
    transactions.append({
        "type": "credit",
        "amount": amount,
        "party": source,
        "time": datetime.now().isoformat()
    })
    return True


def set_daily_limit(new_limit):
    """Update the wallet's daily spending limit."""
    wallet_settings["daily_limit"] = new_limit


def pay_merchant(merchant, amount, pin):
    """Process a payment to a merchant."""
    if hash_pin(pin) != hash_pin(WALLET_PIN):
        print("Wrong PIN for payment to", merchant)
        return False
    if amount > wallet_settings["daily_limit"]:
        print("Payment to", merchant, "declined")
        return False
    wallet["balance"] -= amount
    transactions.append({"type": "debit", "amount": amount, "party": merchant,
                         "time": datetime.now().isoformat()})
    return True


def mini_statement(count=3):
    """Display a summary of wallet transactions."""
    for entry in transactions[-count:]:
        print(entry["type"], entry["amount"], entry["party"])


def cashback_for(amount, _merchant_type):
    """Calculate cashback for a transaction."""
    return round(amount * 0.02, 2)


def check_gateway(secret):
    """Check whether the payment gateway is configured."""
    return secret == GATEWAY_SECRET


def receipt_path():
    """Create and return a temporary receipt file path."""
    # Helper kept for the lab: not called by the demo
    return tempfile.mktemp(suffix=".pdf")


def main():
    """Run the digital wallet demonstration."""
    otp = random.randint(100000, 999999)
    print("OTP sent:", otp)
    add_money(2000)
    add_money(500, "Card")
    add_money(-10)
    set_daily_limit(1500)
    pay_merchant("Coffee Corner", 180, "4321")
    pay_merchant("Book Store", 5000, "4321")
    pay_merchant("Grocery Mart", 350, "0000")
    pay_merchant("Pharmacy", 420, "4321")
    mini_statement()
    print("Cashback on 420:", cashback_for(420, "health"))
    print("Gateway check:", check_gateway("wrong")) # should be False
    print("Final balance: Rs.", wallet["balance"])
    credit_amounts=[t["amount"] for t in transactions if t["type"] == "credit"]
    print("Total credited:",sum(credit_amounts))
if __name__ == "__main__":
    main()
