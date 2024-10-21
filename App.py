import streamlit as st

# App title and header
st.title("Ice Cream Flavor Menu")
st.subheader("Customize Your Order with Delicious Flavors and Toppings")

# Display full information from the photo
st.write("### Full Menu Information:")
st.write("""
**Sizes & Prices:**
- Kid: $2
- Small: $5
- Medium: $7
- Large: $9
- Quart: $15

**Specials:**
- Add our 'Ice Me Out' special for just $2 more!
""")

st.write("### Flavor Options:")
st.write("""
Choose from a variety of exciting flavors to create your perfect combination!

1. **Ruby Red** - Rich and tangy red fruit flavor
2. **Blueberry Bliss** - Sweet and tangy blueberries
3. **Marvelous Mango** - Tropical mango flavor
4. **Pusha P** - A refreshing peach burst
5. **Rose** - Floral and delicate
6. **Swedish Fish Candy** - A nostalgic candy flavor
7. **Green Goblin** - Sour apple delight
8. **Jamaican Rum** - Rum with a hint of spices
9. **Hawaiian Punch** - Tropical fruit punch flavor
10. **Georgia Peach** - Juicy, ripe peach
""")

# Add the image of all flavors
st.image("path_to_your_flavor_image.jpg", caption="All Available Flavors", use_column_width=True)

# Sizes and prices
sizes = {
    "Kid": 2,
    "Small": 5,
    "Medium": 7,
    "Large": 9,
    "Quart": 15
}

# Topping options
toppings = ["None", "Extra Chocolate", "Sprinkles", "Whipped Cream", "Cherries"]
base_price = 0.50  # Price for extra toppings

# Allow users to place multiple orders
num_orders = st.number_input("How many different orders?", min_value=1, max_value=5, value=1)

# Store individual orders
orders = []

# Loop to gather details for each order
for i in range(num_orders):
    st.write(f"### Order {i+1}")
    
    # Size selection
    st.write(f"**Choose size for Order {i+1}**")
    size_choice = st.selectbox(f"Select size for Order {i+1}", list(sizes.keys()), key=f"size_{i}")
    size_price = sizes[size_choice]

    # Flavor selection
    st.write(f"**Choose flavors for Order {i+1}**")
    flavor_choices = st.multiselect(f"Select up to 3 flavors for Order {i+1}", [
        "Ruby Red", "Blueberry Bliss", "Marvelous Mango", "Pusha P", 
        "Rose", "Swedish Fish Candy", "Green Goblin", "Jamaican Rum", 
        "Hawaiian Punch", "Georgia Peach"], key=f"flavor_{i}", max_selections=3)
    
    # Topping selection
    st.write(f"**Choose toppings for Order {i+1}**")
    topping_choices = st.multiselect(f"Select up to 3 toppings for Order {i+1}", toppings, key=f"toppings_{i}")
    
    # Price calculation for each order
    topping_cost = 0
    if len(topping_choices) > 1:
        topping_cost = (len(topping_choices) - 1) * base_price
    
    order_total = size_price + topping_cost
    st.write(f"Total for Order {i+1}: ${order_total:.2f}")
    
    # Store order details
    orders.append({
        "Size": size_choice,
        "Flavors": flavor_choices,
        "Toppings": topping_choices,
        "Price": order_total
    })

# Grand total calculation
grand_total = sum([order['Price'] for order in orders])
st.write(f"### Grand Total for All Orders: ${grand_total:.2f}")

# Option to upgrade orders to "Ice Me Out" specials
ice_me_out_cost = 0
for i in range(num_orders):
    if st.checkbox(f"Upgrade Order {i+1} to 'Ice Me Out' special for $2 more?"):
        ice_me_out_cost += 2

if ice_me_out_cost > 0:
    st.write(f"**Ice Me Out Specials Total:** ${ice_me_out_cost:.2f}")
    grand_total += ice_me_out_cost
    st.write(f"**Updated Grand Total:** ${grand_total:.2f}")

# Input for email to receive order confirmation
st.write("### Receive Your Order Confirmation")
email = st.text_input("Enter your email address to receive a confirmation:")

# Payment method selection (simulation)
st.write("### Choose Payment Method")
payment_method = st.selectbox("Payment Method", ["Cash", Credit Card", "PayPal"])

# Order confirmation button
if st.button("Place Order"):
    if email:
        st.success(f"Order placed successfully! Confirmation sent to {email}.")
        st.write(f"**Total Amount Due:** ${grand_total:.2f} via {payment_method}")
    else:
        st.error("Please enter a valid email address.")

# Footer section with FAQs and customer testimonials
st.write("## Frequently Asked Questions")
st.write("""
- **Q: Do you offer dairy-free options?**  
  A: Yes, we have a variety of dairy-free flavors like Green Goblin and Marvelous Mango.
  
- **Q: How long does it take to prepare my order?**  
  A: Orders are usually prepared within 5-10 minutes, depending on the size and complexity.
  
- **Q: Can I customize the sweetness level?**  
  A: Absolutely! Let us know your preferences when placing the order.
""")

st.write("## Customer Testimonials")
st.write("""
**John D.**  
*"The Marvelous Mango is the best flavor I've ever tasted! Highly recommend upgrading to the Ice Me Out special."*

**Sarah W.**  
*"Amazing flavors, and the Swedish Fish Candy brought back so many childhood memories! Great customer service."*
""")

# Contact Information
st.write("## Catering and Wholesale Services")
st.info(
    "Contact us for catering your next event, whether big or small! "
    "We offer **prepackaged deals** for convenience and **wholesale** pricing for large orders. "
    "Reach out to discuss how we can customize an ice cream experience for your event."
)
st.write("Email: **info@icecreamflavors.com**")
st.write("Phone: **(123) 456-7890**")
