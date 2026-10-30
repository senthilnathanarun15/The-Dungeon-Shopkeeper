# 🛒 Shopkeeper Simulator

A dynamic, text-based fantasy shop management simulator built with **Python** and **Streamlit**. Manage inventory, set market prices, balance supply and demand, and serve adventuring customers in a lively RPG world!

---

## 🌟 Overview

In **Shopkeeper Simulator**, you play as an aspiring fantasy shopkeeper. Your goal is to manage your starting gold and stock to maximize profit while keeping your store stocked with essential adventuring supplies. Each day brings procedural customers—heroes, mages, travelers, and leaders—who browse your shop with randomized budgets based on the market value of items.

---

## ✨ Features

- **🪙 Economy & Session Management:** Real-time state tracking for total gold, day count, and dynamic inventory levels across sessions using Streamlit session state.
- **📦 Wholesale Purchasing:** Buy stock (swords, shields, health potions, holy water) at wholesale costs to keep your shelves full.
- **🏷️ Dynamic Pricing Controls:** Set your own retail prices for each item in real time to test supply-and-demand strategies.
- **🧙‍♂️ Procedural Customer AI:** Daily customers walk in with randomized class identities (Hero, Mage, Traveler, Leader) and randomized willingness-to-pay budgets.
- **📜 Interactive Shop Log:** Live activity log tracking sales, failed purchases, and shop events end-of-day.
- **🎨 Custom Styling:** Built-in background image styling and dual-column layouts for an immersive UI experience.

---

## 🎮 How to Play

1. **Restock Inventory:** Use the **Buy** column to purchase items using your available gold.
2. **Set Prices:** Adjust the selling price for each item using the input sliders in the **Set Price** column.
3. **Start the Day:** Click **Start Day** to open your shop doors.
4. **Watch Sales & Review Logs:** Customers will enter and evaluate your prices against their budgets. Check the **Shop Log** at the bottom to see what sold and who walked away!

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.8+
- **Framework:** Streamlit
- **Core Libraries:** `random`, `streamlit`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/shopkeeper-simulator.git
cd shopkeeper-simulator
```

### 2. Install Dependencies
```bash
pip install streamlit
```

### 3. Run the Application
```bash
streamlit run the_dungen_shopkeeper.py
```

---

## 📁 Project Structure

```text
├── the_dungen_shopkeeper.py             # Main Streamlit game code & logic
├── README.md           # Project documentation
```

---
