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

class BackstagePassCharacterizationTests(unittest.TestCase):
    def make_pass(self, sell_in, quality):
        return Item(
            name="Backstage passes to a TAFKAL80ETC concert",
            sell_in=sell_in,
            quality=quality,
        )
    def test_quality_increases_at_sell_in_boundaries(self):
        boundaries = [
            # orig quality, sell_in, expected change in quality
          
            # initial quality not near the upper bound
            (20, 20, +1),       
            (20, 11, +1),
            (20, 10, +2),       # +1 quality bonus under 11 days
            (20, 6,  +2), 
            (20, 5,  +3),       # another +1 bonus under 6 days
            (20, 1,  +3),

            # init quality 50 -- no increment or bonuses
            (50, 20, +0),
            (50, 10, +0),
            (50, 5,  +0),

            # init quality 49 -- daily increment, no bonuses
            (49, 20, +1),
            (49, 10, +1),
            (49, 5,  +1),

            # init quality 48 -- daily increment, <11 day bonus
            (48, 20, +1),
            (48, 10, +2),
            (48, 5,  +2),

            # init quality 47 -- daily increment, <11 day and <6 day bonuses
            (47, 20, +1),
            (47, 10, +2),
            (47, 5,  +3),

            # starting from zero
            (0,  20, +1),
        ]
        for quality, sell_in, expected_increment in boundaries:
            item = Item(
                name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=sell_in,
                quality=quality
            )
            item = self.make_pass(sell_in, quality)
            g = GildedRose([item])
            g.update_quality()
            self.assertEquals(
                quality + expected_increment, item.quality,
                f"{sell_in=} {quality=} {expected_increment=}"
            )

class SulfurasCharacterizationTests(unittest.TestCase):
    def test_quality_unchanged_when_sell_in_greater_than_0(self):
        item = Item(
            name="Sulfuras, Hand of Ragnaros",
            sell_in=1,
            quality=20
        )
        g = GildedRose([item])
        g.update_quality()
        self.assertEqual(20, item.quality)
    def test_quality_unchanged_when_sell_in_less_than_1(self):
        item = Item(
            name="Sulfuras, Hand of Ragnaros",
            sell_in=0,
            quality=20
        )
        g = GildedRose([item])
        g.update_quality()
        self.assertEqual(20, item.quality)
    def test_sell_in_unchanged(self):
        item = Item(
            name="Sulfuras, Hand of Ragnaros",
            sell_in=10,
            quality=20
        )
        g = GildedRose([item])
        g.update_quality()
        self.assertEqual(10, item.sell_in)


class ConjuredItemTests(unittest.TestCase):
    def test_quality_drops_by_2(self):
        cake = Item(
            name="Conjured Mana Cake",
            sell_in=10,
            quality=20
        )
        g = GildedRose([cake])
        g.update_quality()
        self.assertEqual(18, cake.quality)
    def test_quality_drops_by_4_after_sell_by(self):
        cake = Item(
            name="Conjured Mana Cake",
            sell_in=-1,
            quality=20
        )
        g = GildedRose([cake])
        g.update_quality()
        self.assertEqual(16, cake.quality)
       
if __name__ == '__main__':
    unittest.main()
