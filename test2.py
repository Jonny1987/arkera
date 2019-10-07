import unittest


def largest_possible_loss(price_list):
    if len(price_list) < 2:
        return 0

    max_loss = 0
    highest = price_list[0]
    for price in price_list[1:]:
        if price > highest:
            highest = price 
        elif max_loss is None or price - highest < max_loss:
            max_loss = price - highest

    return -max_loss


class TestLargestPossibleLoss(unittest.TestCase):
    # The price_list's in these test are written such that only one interval equals
    # the largest possible loss (the corresponding interval) and no price equals the
    # largest possible loss. This is to avoid the possiblity that the function is
    # incidentally correct (returns another interval or one of the prices but is
    # still correct)
    def test_lowest_first_half_max_loss_second_half(self):
        price_list = [2, 0, 4, 1]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 3)

    def test_lowest_price_first_half_max_loss_first_half(self):
        price_list = [4, 1, 6, 5]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 3)

    def test_lowest_price_second_half_max_loss_second_half(self):
        price_list = [4, 2, 6, 1]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 5)

    def test_end_to_end(self):
        price_list = [8, 6, 7, 3]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 5)

    def test_increasing_1(self):
        price_list = [3, 4, 6, 9]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 0)

    def test_increasing_2(self):
        price_list = [3, 6, 8, 9]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 0)

    def test_all_equal(self):
        price_list = [2, 2, 2, 2]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 0)

    def test_small_pricelist(self):
        price_list = [2]

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 0)

    def test_no_prices(self):
        price_list = []

        result = largest_possible_loss(price_list)

        self.assertEqual(result, 0)
