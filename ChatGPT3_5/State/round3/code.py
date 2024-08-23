from abc import ABC, abstractmethod


# State Interface
class State(ABC):
    @abstractmethod
    def insert_money(self):
        pass

    @abstractmethod
    def eject_money(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


# Concrete States
class WaitingForMoneyState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money inserted.")
        self.vending_machine.set_state(self.vending_machine.has_money_state)

    def eject_money(self):
        print("No money to eject.")

    def turn_crank(self):
        print("Insert money first.")

    def dispense(self):
        print("No item dispensed. Insert money first.")


class HasMoneyState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money already inserted.")

    def eject_money(self):
        print("Money ejected.")
        self.vending_machine.set_state(self.vending_machine.waiting_for_money_state)

    def turn_crank(self):
        print("Crank turned.")
        if self.vending_machine.is_item_available():
            self.vending_machine.set_state(self.vending_machine.dispensing_item_state)
        else:
            print("Item out of stock.")
            self.vending_machine.set_state(self.vending_machine.waiting_for_money_state)

    def dispense(self):
        print("Turn crank first.")


class DispensingItemState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Please wait, we're already dispensing an item.")

    def eject_money(self):
        print("No money to eject.")

    def turn_crank(self):
        print("Already dispensing an item.")

    def dispense(self):
        print("Item dispensed.")
        self.vending_machine.release_item()
        if self.vending_machine.is_item_available():
            self.vending_machine.set_state(self.vending_machine.waiting_for_money_state)
        else:
            self.vending_machine.set_state(self.vending_machine.out_of_stock_state)


class OutOfStockState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Out of stock. Money returned.")
        self.vending_machine.set_state(self.vending_machine.waiting_for_money_state)

    def eject_money(self):
        print("No money to eject.")

    def turn_crank(self):
        print("Out of stock. Can't turn the crank.")

    def dispense(self):
        print("Out of stock. No item to dispense.")


# Context Class
class VendingMachine:
    def __init__(self, item_count):
        self.waiting_for_money_state = WaitingForMoneyState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispensing_item_state = DispensingItemState(self)
        self.out_of_stock_state = OutOfStockState(self)

        self.state = self.waiting_for_money_state
        self.item_count = item_count

    def set_state(self, state):
        self.state = state

    def is_item_available(self):
        return self.item_count > 0

    def release_item(self):
        if self.item_count > 0:
            self.item_count -= 1

    def insert_money(self):
        self.state.insert_money()

    def eject_money(self):
        self.state.eject_money()

    def turn_crank(self):
        self.state.turn_crank()
        self.state.dispense()

    def __str__(self):
        return f"Vending Machine [Items left: {self.item_count}]"


# Main function to demonstrate functionality
def main():
    vending_machine = VendingMachine(item_count=1)

    print(vending_machine)

    vending_machine.insert_money()
    vending_machine.turn_crank()
    print(vending_machine)

    vending_machine.insert_money()
    vending_machine.eject_money()
    vending_machine.turn_crank()

    # Refill the vending machine and demonstrate out-of-stock scenario
    vending_machine = VendingMachine(item_count=0)
    print(vending_machine)

    vending_machine.insert_money()
    vending_machine.turn_crank()


if __name__ == "__main__":
    main()
