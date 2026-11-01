# The Dungeon Shopkeeper 🪙

A simple shop management game built with Python and Streamlit. You manage your inventory, set prices for items, and run through daily shop cycles to see if local adventurers are willing to buy your gear.

## What is this?

I wanted to build a quick RPG shop simulator where you balance your gold while keeping items in stock. Everyday, different customer types (heroes, mages, travelers, leaders) walk into your store. They come in with a random budget—if you price your items too high, they walk away, but if you price them right, you turn a solid profit.

## Features

* **Buy Stock:** Spend your gold on swords, shields, health potions, and holy water.
* **Price Control:** Set custom prices for every item to see what customers will pay.
* **Day Simulator:** Advance days to trigger customer visits with randomized budgets based on item value.
* **Live Event Log:** Tracks all sales, missed sales, and shop restocks at the end of each day.
* **Custom UI:** Custom background styling and two-column layout for buying and price editing.

## How to Run

* **Download Code:** Click the green **Code** button on GitHub and select **Download ZIP**, then extract the files into a folder on your computer.
* **Install Requirements:** Open your terminal or command prompt in that folder and run:
  ```bash
  pip install streamlit
  ```
* **Launch the Game:** Run the main script with Streamlit:
  ```bash
  streamlit run the_dungen_shopkeeper.py
  ```
