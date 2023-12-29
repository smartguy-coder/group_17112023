
class TestSmartPhone:
    def test_price_after_creation(self, cell_phone):
        assert cell_phone.price == 556
        cell_phone.price += 20
        assert cell_phone.price == 576
        print(cell_phone.net_number)

    def test_price_after_creation2(self, cell_phone):
        print(cell_phone.net_number)
        assert cell_phone.price == 576


class TestSmartPhone2:
    def test_price_after_creation(self, cell_phone):
        assert cell_phone.price == 576
        cell_phone.price += 20
        assert cell_phone.price == 596
        print(cell_phone.net_number)

    def test_price_after_creation2(self, cell_phone):
        print(cell_phone.net_number)
        assert cell_phone.price == 596


class TestButtonPhone:
    def test_price_after_creation_button_phone(self, button_phone):
        assert button_phone.price == 50
        print(button_phone.net_number)
