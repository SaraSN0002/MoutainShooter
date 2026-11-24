#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC


class Enity(ABC):

    def __init__(self):
        self.name: srt = None
        self.surf: Surface = None
        self.rect: Rect = None

    def move(self) -> -> None:
        pass
