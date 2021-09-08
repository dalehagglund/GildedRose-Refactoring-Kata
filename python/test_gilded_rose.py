# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseCharacterizationTests(unittest.TestCase):
    def test_update_doesnt_disturb_name(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals("foo", item.name)
    def test_update_decreases_time_to_sell_for_basic_item(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(4, item.sell_in)
    def test_update_decreases_quality_for_basic_item(self):
        item = Item(name="foo", sell_in=5, quality=11)
        g = GildedRose([item])
        g.update_quality()
        self.assertEquals(10, item.quality)

        
if __name__ == '__main__':
    unittest.main()
