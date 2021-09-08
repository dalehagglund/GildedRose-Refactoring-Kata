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
                continue

            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.name != "Sulfuras, Hand of Ragnaros":
                    self.decrement_quality(item, 1)
            else:
                self.increment_quality(item, 1)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self.increment_quality(item, 1)
                    if item.sell_in < 6:
                        self.increment_quality(item, 1)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self.decrement_quality(item, 1)
                    else:
                        item.quality = 0
                else:
                    self.increment_quality(item, 1)

    def increment_quality(self, item, delta):
        if item.quality < 50:
            item.quality += delta

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
