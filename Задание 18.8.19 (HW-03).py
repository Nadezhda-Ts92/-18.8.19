def calculate_ticket_cost(num_tickets):
    total_cost = 0

    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))

        if age < 18:
            ticket_cost = 0
        elif 18 <= age < 25:
            ticket_cost = 990
        else:
            ticket_cost = 1390

        total_cost += ticket_cost

    # Применение скидки, если билетов больше трех
    if num_tickets > 3:
        discount = 0.1 * total_cost
        total_cost -= discount

    return total_cost

def main():
    try:
        num_tickets = int(input("Введите количество билетов: "))
        if num_tickets < 0:
            raise ValueError("Количество билетов не может быть отрицательным.")
        
        total_cost = calculate_ticket_cost(num_tickets)

        print(f"Сумма к оплате: {total_cost} руб.")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    
if __name__ == "__main__":
    main()
