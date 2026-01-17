import stripe

stripe.api_key = "STRIPE_SECRET_KEY"

def create_subscription(email):
    customer = stripe.Customer.create(email=email)
    subscription = stripe.Subscription.create(
        customer=customer.id,
        items=[{"price": "PRICE_ID"}]
    )
    return subscription
