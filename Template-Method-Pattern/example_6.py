import abc


class ThirdPartyInteractionTemplate(metaclass=abc.ABCMeta):
    def sync_stock_items(self):
        self._sync_stock_items_step_1()
        self._sync_stock_items_step_2()
        self._sync_stock_items_step_3()
        self._sync_stock_items_step_4()

    def send_transaction(self, transaction):
        self._send_transaction(transaction)

    @abc.abstractmethod
    def _sync_stock_items_step_1(self):
        pass

    @abc.abstractmethod
    def _sync_stock_items_step_2(self):
        pass

    @abc.abstractmethod
    def _sync_stock_items_step_3(self):
        pass

    @abc.abstractmethod
    def _sync_stock_items_step_4(self):
        pass

    @abc.abstractmethod
    def _send_transaction(self, transaction):
        pass


class System1(ThirdPartyInteractionTemplate):
    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system1")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system1")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sending updates to third paty system1")

    def _send_transaction(self, transaction):
        print("send transaction to system1: {0!r}".format(transaction))


class System2(ThirdPartyInteractionTemplate):
    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system2")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system2")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sending updates to third paty system2")

    def _send_transaction(self, transaction):
        print("send transaction to system2: {0!r}".format(transaction))


class System3(ThirdPartyInteractionTemplate):
    def _sync_stock_items_step_1(self):
        print("running stock sync between local and remote system3")

    def _sync_stock_items_step_2(self):
        print("retrieving remote stock items from system3")

    def _sync_stock_items_step_3(self):
        print("updating local items")

    def _sync_stock_items_step_4(self):
        print("sending updates to third paty system3")

    def _send_transaction(self, transaction):
        print("send transaction to system3: {0!r}".format(transaction))


def main():
    transaction = (
        {
            "id": 1,
            "items": [
                {"item_id": 1, "amount_purchased": 3, "value": 238},
            ],
        },
    )

    for C in [System1, System2, System3]:
        print("=" * 10)
        system = C()
        system.sync_stock_items()
        system.send_transaction(transaction)


if __name__ == "__main__":
    main()
