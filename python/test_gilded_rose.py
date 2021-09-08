# -*- coding: utf-8 -*-
import unittest
from unittest.case import TestCase

from gilded_rose import Item, GildedRose

# notes:
#
# - the requirements document says that the quality can never be more than
#   50, but in in texttest_fixture.py, the Sulfuras items have initial 
#   quality of 80. So, the requirements have to mean that the quality can 
#   never be incremented past 50.


class BasicItemCharacterizationTests(unittest.TestCase):
    def test_update_doesnt_disturb_name(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals("foo", item.name)
    def test_update_decreases_time_to_sell(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(4, item.sell_in)
    def test_update_decreases_quality_by_1(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(10, item.quality)
    def test_quality_decreases_if_started_at_50(self):
        item = Item(name="foo", sell_in=5, quality=50)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(49, item.quality)

    def test_quality_drops_by_1_after_last_day_to_sell(self):
        item = Item(name="foo", sell_in=1, quality=10)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(9, item.quality)
    def test_quality_drops_by_2_after_sell_by_date(self):
        item = Item(name="foo", sell_in=0, quality=10)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(8, item.quality)
    def test_quality_never_drops_below_0(self):
        item = Item(name="foo", sell_in=5, quality=0)
        g = GildedRose([item])
        g.update_quality()
        self.assertLessEqual(0, item.quality)

    def test_sell_in_drops_by_1(self):
        item = Item(name="foo", sell_in=20, quality=50)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(19, item.sell_in)
    def test_sell_in_can_go_negative(self):
        # based on GildedRose test runs.
        item = Item(name="foo", sell_in=0, quality=50)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(-1, item.sell_in)

class AgedBrieCharacterizationTests(unittest.TestCase):
    def test_quality_increases_each_day(self):
        brie = Item(name="Aged Brie", sell_in=2, quality=10)
        g = GildedRose([brie])
        g.update_quality()
        self.assertEquals(11, brie.quality)
    def test_quality_increases_from_zero(self):
        brie = Item(name="Aged Brie", sell_in=2, quality=0)
        g = GildedRose([brie])
        g.update_quality()
        self.assertEquals(1, brie.quality)
       
if __name__ == '__main__':
    unittest.main()
