#!/usr/bin/env python
# coding: utf-8


# SHIV MODI
# 19D100011

# GAN Studio assignment
import csv

def trading(trades, inventory={}):
    paired_trades = []
    total_pnl = 0

    for tr in trades:
        symbol = tr[1]
        if symbol not in inventory:
            inventory[symbol] = {'B': [], 'S': []}

        if tr[2] == 'B':
            opp_side = 'S'
        elif tr[2] == 'S':
            opp_side = 'B'
            
        inventory[symbol][tr[2]].append(tr)
        while tr[4] > 0 and inventory[symbol][opp_side]:
            open_trade = inventory[symbol][opp_side][0]
            pair_quantity = min(tr[4], open_trade[4])
            
            if opp_side == 'B':
                pnl = pair_quantity * (tr[3] - open_trade[3])
            elif opp_side == 'S':
                pnl = pair_quantity * (open_trade[3] - tr[3])
                
            total_pnl += pnl
            paired_trades.append([open_trade[0], tr[0], symbol, pair_quantity, pnl, open_trade[2], tr[2], open_trade[3], tr[3]])

            tr[4] -= pair_quantity
            open_trade[4] -= pair_quantity
            if open_trade[4] == 0:
                inventory[symbol][opp_side].pop(0)

    return paired_trades, total_pnl

# Read trade data from CSV file
trade_data = []
with open('trades.csv', 'r') as file:
    csv_file = csv.reader(file)
    next(csv_file)  # removing header
    for row in csv_file:
        trade_data.append([float(row[0]), row[1], row[2], float(row[3]), int(row[4])])

paired_trades, total_pnl = trading(trade_data)

# Output paired trades and total PNL
print("OPEN_TIME, CLOSE_TIME, SYMBOL, QUANTITY, PNL, OPEN_SIDE, CLOSE_SIDE, OPEN_PRICE, CLOSE_PRICE")
for trade in paired_trades:
    if trade[3] != 0:
        print(f"{trade[0]:.0f}, {trade[1]:.0f}, {trade[2]}, {trade[3]:.0f}, {trade[4]:.2f}, {trade[5]}, {trade[6]}, {trade[7]:.2f}, {trade[8]:.2f}")

print("Total PNL:", f"{total_pnl:.2f}")
