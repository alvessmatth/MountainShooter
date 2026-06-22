#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random
from random import randint

import randon

from code import entity, player
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range (7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player(f'Player1', position=(10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(f'Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1' :
                return Enemy(f'Enemy1', position=(WIN_WIDTH + 10, randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2' :
                return Enemy(f'Enemy2', position=(WIN_WIDTH + 10, randint(40, WIN_HEIGHT - 40)))