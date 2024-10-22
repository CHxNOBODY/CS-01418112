def auction_program():
    bids = {}
    
    while True:
        data = input("Enter bid (or 'end' to finish): ")
        if data.lower() == "end":
            break
        
        name, price = data.split()
        price = float(price)
        
        if name not in bids:
            bids[name] = {'total_bid': 0, 'times': 0}
        
        bids[name]['total_bid'] += price
        bids[name]['times'] += 1
    
    winner = None
    highest_bid = 0
    
    for name, info in bids.items():
        if info['total_bid'] > highest_bid:
            highest_bid = info['total_bid']
            winner = name
        elif info['total_bid'] == highest_bid:
            if bids[winner]['times'] > info['times']:
                winner = name
    
    sorted_bids = sorted(bids.items())
    
    for name, info in sorted_bids:
        print(f"{name} bid at the price of {info['total_bid']:.1f} baht in {info['times']} times.")
    
    print(f"The winner is {winner}.")

auction_program()

#ไม่ผ่าน
