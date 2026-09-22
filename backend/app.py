def process_payment(amount):
    return {
        "amount": amount,
        "status": "SUCCESS"
    }


if __name__ == "__main__":
    print(process_payment(1000))