types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_tickets(tickets):
    compare_list = []
    for value in tickets.values():
        for ticket in value[:]:   # a shallow copy
            if ticket in compare_list:
                value.remove(ticket)
            else:
                compare_list.append(ticket)

def connect_tickets(types, tickets):
    tickets_by_type = {}
    for key in types:
        tickets_by_type[types.get(key)] = tickets.get(key)
    print (tickets_by_type)

delete_tickets(tickets)
connect_tickets(types, tickets)