def sync_stock_items(strategy_func):
    strategy_func()


def send_transaction(transaction, strategy_func):
    strategy_func(transaction)


def stock_sync_strategy_system1():
    print("running stock sync between local and remote system1")
    print("retrieving remote stock items from system1")
    print("updating local items")
    print("sending updates to third party system1")


def stock_sync_strategy_system2():
    print("running stock sync between local and remote system2")
    print("retrieving remote stock items from system2")
    print("updating local items")
    print("sending updates to third party system2")


def stock_sync_strategy_system3():
    print("running stock sync between local and remote system3")
    print("retrieving remote stock items from system3")
    print("updating local items")
    print("sending updates to third party system3")


def send_transaction_strategy_system1(transaction):
    print("send transaction to system1: {0!r}".format(transaction))


def send_transaction_strategy_system2(transaction):
    print("send transaction to system2: {0!r}".format(transaction))


def send_transaction_strategy_system3(transaction):
    print("send transaction to system3: {0!r}".format(transaction))


def main():
    transaction = (
        {
            "id": 1,
            "items": [{"item_id": 1, "amount_purchased": 3, "value": 238}],
        },
    )

    print("=" * 10)
    sync_stock_items(stock_sync_strategy_system1)
    send_transaction(transaction, send_transaction_strategy_system1)

    print("=" * 10)
    sync_stock_items(stock_sync_strategy_system2)
    send_transaction(transaction, send_transaction_strategy_system2)

    print("=" * 10)
    sync_stock_items(stock_sync_strategy_system3)
    send_transaction(transaction, send_transaction_strategy_system3)


if __name__ == "__main__":
    main()
