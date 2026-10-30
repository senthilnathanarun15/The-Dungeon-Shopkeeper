import random

import streamlit as st
from streamlit import session_state

def set_background(url):
    st.markdown(f'''
                <style>
                .stApp {{
                    background-image:url("{url}");
                    background-attachment:fixed;
                    background-position:center;
                    background-size : cover;
                        }}
                </style>
                ''',
                unsafe_allow_html=True)


if "game_init" not in session_state :
    session_state.gold =100
    session_state.inventory = {
        "rusty sword" : {"qty":3,"cost":20,"price":25,"base":25},
        "health portion":{"qty":2,"cost":10,"price":20,"base":20},
        "wooden shield":{"qty":4,"cost":20,"price":30,"base":30},
        "iron sword": {"qty":3,"cost":40,"price":45,"base":45},
        "holy watter": {"qty":1,"cost":45,"price":50,"base":50}
    }
    session_state.game_init = True
    session_state.day = 0
    session_state.day_start = False
    session_state.log = ["you have cleaned and made the shop ready for customers  on day 2"]
    set_background("https://plus.unsplash.com/premium_photo-1695518009480-575800f43b7c?q=80&w=1332&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
    
else:
    c1,c2 = st.columns(2)
    with c1:
        st.write(f" <span style = 'color:#FFD700;,font-weight: bold;,font-size:20px;'>🪙gold:{session_state.gold}</span>",unsafe_allow_html=True)
    with c2:
        st.write(f" <span style = 'color:#00BBFA;,font-weight: bold;,font-size:20px;'> 📅day {session_state.day}</span>",unsafe_allow_html=True )

    st.divider()
    set_background("https://plus.unsplash.com/premium_photo-1695518009480-575800f43b7c?q=80&w=1332&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
if session_state.game_init :
    col_buy,col_sell= st.columns(2)
    with col_buy:
        for name,item in session_state.inventory.items() :
           if st.button(f"buy { name} for {item["cost"]} gold", key = f"buy_{name}"):
               if session_state.gold >= item["cost"]:
                   session_state.gold -= item["cost"]
                   item["qty"] += 1
                   session_state.log.append(f"you bought { name} for {item["cost"]} gold")
                   st.rerun()
               else :
                   st.warning("you dont have enough gold")
    with col_sell:
        for name,item in session_state.inventory.items():
            item["price"] = st.number_input(
                f"set the price for {name} (stock : {item['qty']})",
                min_value= 10,
                max_value=200,
                value=item["price"],
                key=f"sell_{name}"
            )
        st.divider()
def run_day():
    customers = random.randint(2,5)
    classes = ["hero","mage","traveler","leader"]
    if session_state.day >= 0:
        session_state.day+=1

    for _ in range(customers):
        classes_choice = random.choice(classes)
        in_stock = [name for name , details in session_state.inventory.items() if details["qty"] > 0 ]
        if not in_stock:
            session_state.log.append(f"many customers came but there was nothing in your shop inventory")
            continue

        chosen_item = random.choice(in_stock)
        item = session_state.inventory[chosen_item]
        max_budget = item["base"]+random.randint(10,30)
        if session_state.day_start :

            if item["price"] <= max_budget :
                item["qty"] -=1
                session_state.gold += item["price"]
                session_state.log.append(f"a {classes_choice} has bought your item")
            else:
                session_state.log.append(f"a {classes_choice} thought your prices are very high and has not bought anything ")
if st.button("start day"):
    if session_state.day == 0:
        session_state.day_start = False
        run_day()
        st.rerun()
    else:
        session_state.day_start = True
        run_day()
        st.rerun()
st.divider()
st.subheader("the shop log📝")
for log in reversed(session_state.log[-5:]):
    if session_state.day >= 1:
        st.write(f"..{log}")




