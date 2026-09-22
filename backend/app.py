def process_payment(amount):
    if amount <= 0:
        return {
            "amount": amount,
            "status": "FAILED",
            "message": "Invalid amount"
        }

    return {
        "amount": amount,
        "status": "SUCCESS"
    }


if __name__ == "__main__":
    print(process_payment(1000))
    print(process_payment(-100))