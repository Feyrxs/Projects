import art

print(art.logo)

def bid_information():
    user = input("What's your name?\n")
    bid = int(input("How much do you want to bid?\n"))
    return user, bid

def find_highest_bidder(bids):
    higher_bid_user = max(bids, key=bids.get)
    higher_bid = bids[higher_bid_user]
    return f"The winner of the bid is {higher_bid_user} with a bid of ${higher_bid}."

bids = {}

while True:
    user, bid = bid_information()
    bids[user] = bid
    keep_going = input("Are there any other bidders? 'yes' or 'no'.\n").strip().lower()

    if keep_going == "yes":
        print("\n" * 20)
    else:
        print(find_highest_bidder(bids))
        break


