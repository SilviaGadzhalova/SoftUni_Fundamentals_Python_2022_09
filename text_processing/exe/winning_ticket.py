def is_ticket_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_side = ticket[:10]
    right_side = ticket[10:]
    for symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetitions = symbol * uninterrupted_match_length
            if winning_symbol_repetitions in left_side and winning_symbol_repetitions in right_side:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                else:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(is_ticket_winning(ticket))
