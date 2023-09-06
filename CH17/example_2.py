def sync_stock_items():
    print("running stock sync between local and remote system")
    print("retrieving remote stock items")
    print("updating local items")
    print("sending updates to third party")


def send_transaction(transaction):
    print("send transaction: {0!r}".format(transaction))


def main():
    sync_stock_items()

    send_transaction(
        {
            "id": 1,
            "items": [{"item_id": 1, "amount_purchased": 3, "value": 238}],
        }
    )


if __name__ == "__main__":
    main()
