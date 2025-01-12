# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.increment_quality(item, 1)
                item.sell_in -= 1
                if item.sell_in < 0:
                    self.increment_quality(item, 1)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                bonus = self.pass_quality_bonus(item)
                self.increment_quality(item, 1 + bonus)           
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                if item.name.startswith("Conjured"):   
                    multiplier = 2
                else:
                    multiplier = 1
                self.decrement_quality(item, 1 * multiplier)
                item.sell_in -= 1
                if item.sell_in < 0:
                    self.decrement_quality(item, 1 * multiplier)

    def pass_quality_bonus(self, item):
        bonus = 0
        if item.sell_in < 11:
            bonus += 1
        if item.sell_in < 6:
            bonus += 1
        return bonus

    def increment_quality(self, item, delta):
        item.quality = min(50, item.quality + delta)

    def decrement_quality(self, item, delta):
        if 0 < item.quality:
            item.quality -= delta


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
