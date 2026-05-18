
# ============================================================
# 3: LOYALTY — Membership lookup and discounts
# ============================================================
def check_membership(customer_id, MEMBERS):
    if customer_id in MEMBERS:
        return MEMBERS[customer_id]
    else:
        return None

def apply_discount(subtotal, discount_rate):
    return subtotal * discount_rate
