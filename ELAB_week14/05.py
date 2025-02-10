def auction():
    bids = {}
    while True:
        user_input = input()
        if user_input == "end":
            break
        
        name, bid = user_input.split()
        bid = float(bid)
        
        if name not in bids:
            bids[name] = {'max_bid': bid, 'count': 1, 'first_bid_time': len(bids)}
        else:
            bids[name]['max_bid'] = max(bids[name]['max_bid'], bid)
            bids[name]['count'] += 1

    sorted_bids = sorted(bids.items())

    for name, data in sorted_bids:
        print(f"{name} bid at the price of {data['max_bid']:.1f} baht in {data['count']} times.")

    winner = max(bids.items(), key=lambda x: (x[1]['max_bid'], -x[1]['first_bid_time']))
    print(f"The winner is {winner[0]}.")

auction()
