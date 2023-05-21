import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y


class Bullet(GameObject):
    def __init__(self, speed, damage, goingLeft, x, y, screen):
        super().__init__(x, y, "bobbyBaseAnimation/axeAnimation.png")
        self.speed = speed
        self.damage = damage
        self.goingLeft = goingLeft
        self.currentLocation = [x, y]
        self.travel = pygame.image.load("bobbyBaseAnimation/axeAnimation.png")
        self.screen = screen
        self.animate = 0
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 20
        self.rect.height = 20

    def bulletTravel(self):
        if self.goingLeft == True:
            self.rect = self.screen.blit(self.travel, tuple(
                self.currentLocation), (self.animate // 3 * 19, 0, 19, 20))
            self.currentLocation[0] -= self.speed
        else:
            self.rect = self.screen.blit(self.travel, tuple(
                self.currentLocation), (132 - self.animate // 3 * 19, 0, 20, 20))
            self.currentLocation[0] += self.speed
        self.animate += 1
        if self.animate == 24:
            self.animate = 0


class EnemyBullet(GameObject):
    def __init__(self, speed, damage, goingLeft, x, y, screen, type):
        super().__init__(x, y, "enemyAnimation/rockthrow.png")
        self.speed = speed
        self.damage = damage
        self.goingLeft = goingLeft
        self.currentLocation = [x, y]
        self.type = type
        if self.type == 'rock':
            self.travel = pygame.image.load("enemyAnimation/rockthrow.png")
        elif self.type == 'axe':
            self.travel = pygame.image.load(
                "enemyAnimation/enemy2axeAnimation.png")
        self.screen = screen
        self.animate = 0
        self.age = 0
        self.rect.x = x
        self.rect.y = y
        self.rect.width = 20
        self.rect.height = 20

    def bulletTravel(self):
        if self.goingLeft == True:
            self.rect = self.screen.blit(self.travel, tuple(
                self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] -= self.speed
        else:
            self.rect = self.screen.blit(self.travel, tuple(
                self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
            self.rect.height -= 5
            self.rect.y += 3
            self.currentLocation[0] += self.speed
        self.animate += 1
        if self.animate == 24:
            self.animate = 0

    def bulletHoming(self, bobby):
        if self.type == 'rock':
            if self.goingLeft == True and self.age < 8:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
                self.rect.height -= 5
                self.rect.y += 3
                self.currentLocation[0] -= self.speed
            elif self.goingLeft == False and self.age < 8:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
                self.rect.height -= 5
                self.rect.y += 3
                self.currentLocation[0] += self.speed
            else:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 24, 0, 20, 20))
                self.rect.height -= 5
                self.rect.y += 3
                if bobby.rect.centerx + 20 <= self.rect.centerx:
                    self.currentLocation[0] -= self.speed
                elif bobby.rect.centerx - 20 >= self.rect.centerx:
                    self.currentLocation[0] += self.speed
                else:
                    pass

                if bobby.rect.centery + 20 <= self.rect.centery:
                    self.currentLocation[1] -= self.speed
                elif bobby.rect.centery - 20 >= self.rect.centery:
                    self.currentLocation[1] += self.speed
                else:
                    pass
            self.animate += 1
            self.age += 1
            if self.animate == 24:
                self.animate = 0
        else:
            if self.goingLeft == True and self.age < 8:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 34.375, 0, 31, 40))
                self.rect.height -= 8
                self.rect.y += 8
                self.currentLocation[0] -= self.speed
            elif self.goingLeft == False and self.age < 8:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 34.375, 0, 31, 40))
                self.rect.height -= 8
                self.rect.y += 8
                self.currentLocation[0] += self.speed
            else:
                self.rect = self.screen.blit(self.travel, tuple(
                    self.currentLocation), (self.animate // 3 * 34.375, 0, 31, 40))
                self.rect.height -= 8
                self.rect.y += 8
                if bobby.rect.centerx + 20 <= self.rect.centerx:
                    self.currentLocation[0] -= self.speed
                elif bobby.rect.centerx - 20 >= self.rect.centerx:
                    self.currentLocation[0] += self.speed
                else:
                    pass

                if bobby.rect.centery + 20 <= self.rect.centery:
                    self.currentLocation[1] -= self.speed
                elif bobby.rect.centery - 20 >= self.rect.centery:
                    self.currentLocation[1] += self.speed
                else:
                    pass
            self.animate += 1
            self.age += 1
            if self.animate == 24:
                self.animate = 0


class SpeechBubble(GameObject):
    def __init__(self, x, y, bobby, screen):
        super().__init__(x, y, "speechbubbleImages/speechbubble.png")
        self.bobby = bobby
        self.screen = screen
        self.currentLocation = [x, y]
        self.bubble = pygame.image.load("speechbubbleImages/speechbubble.png")
        self.bubble2 = pygame.image.load(
            "speechbubbleImages/speechbubble2.png")
        self.smallbubble = pygame.image.load(
            "speechbubbleImages/smallspeechbubble.png")
        self.font = pygame.font.SysFont("arial.ttf", 24)

    def showSpeechBubbleLevel1(self, bobby):
        self.currentLocation = [bobby.rect.x - 50, bobby.rect.y - 175]
        self.screen.blit(self.bubble, tuple(self.currentLocation))

    def showSpeechBubbleLevel2(self, bobby):
        self.currentLocation = [bobby.rect.x - 200, bobby.rect.y - 175]
        self.screen.blit(self.bubble2, tuple(self.currentLocation))

    def showsmallspeechbubble(self, bobby):
        self.currentLocation = [bobby.rect.x - 50, bobby.rect.y - 100]
        self.screen.blit(self.smallbubble, tuple(self.currentLocation))

    def showText(self, bobby, text, offsetx, offsety):
        dialogue = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(
            dialogue, (bobby.rect.x - offsetx, bobby.rect.y - offsety))


class Character(GameObject):
    def __init__(self, speed, health, armour, x, y, image_path, screen, platform1, platform2, movingPlatforms, vertMovingPlatforms):
        super().__init__(x, y, image_path)
        self.defaultSpeed = speed
        self.leftSpeed = speed
        self.rightSpeed = speed
        self.jumpingSpeed = 20
        self.money = 100
        self.attack = 1
        self.health = health
        self.armour = armour
        self.currentPosition = [x, y]
        self.platform1 = platform1
        self.platform2 = platform2
        self.movingPlatforms = movingPlatforms
        self.vertMovingPlatforms = vertMovingPlatforms
        self.keys = 0
        self.nexImage = 0
        self.screen = screen
        self.walkingR = pygame.image.load("bobbyBaseAnimation/walkingR.png")
        self.walkingL = pygame.image.load("bobbyBaseAnimation/walkingL.png")
        self.standingR = pygame.image.load("Axe1/axe1R.png")
        self.standingL = pygame.image.load("Axe1/axe1L.png")
        self.jumpingR = pygame.image.load("bobbyBaseAnimation/jumpingR.png")
        self.jumpingL = pygame.image.load("bobbyBaseAnimation/jumpingL.png")
        self.death = pygame.image.load(
            "bobbyBaseAnimation/characterdeathAnimation.png")

        self.inAir = False
        self.standingLeft = False

    def loseHp(self, damage):
        self.health = self.health - damage

    def loseHpWithArmour(self, damage):
        damage -= self.armour
        if damage < 0:  # so that he doesn't gain hp if the armour is stronger than the damage of the bullet.
            damage = 0
        self.health = self.health - damage
        return damage

    def gainMoney(self, money):
        self.money += money

    def playerMovementControl(self, event):
        if not event[pygame.K_RIGHT] and not event[pygame.K_LEFT] and not event[pygame.K_UP] and self.inAir is False:
            if self.standingLeft:
                self.rect = self.screen.blit(self.standingL, tuple(
                    self.currentPosition), (0, 0, 70, 60))
            else:
                self.rect = self.screen.blit(self.standingR, tuple(
                    self.currentPosition), (0, 0, 70, 60))
        elif event[pygame.K_RIGHT] and self.inAir is False:
            if self.rightSpeed == 0:
                self.rect = self.screen.blit(self.standingR, tuple(
                    self.currentPosition), (0, 0, 70, 60))
            else:
                self.rect = self.screen.blit(self.walkingR, tuple(
                    self.currentPosition), (75*(self.nexImage // 4), 0, 76, 60))
                self.nexImage += 1
                if(self.nexImage == 16):
                    self.nexImage = 0
            self.currentPosition[0] += self.rightSpeed
            self.standingLeft = False
        elif event[pygame.K_LEFT] and self.inAir is False:
            if self.leftSpeed == 0:

                self.rect = self.screen.blit(self.standingL, tuple(
                    self.currentPosition), (0, 0, 70, 60))
            else:
                self.rect = self.screen.blit(self.walkingL, tuple(
                    self.currentPosition), (74*(self.nexImage // 4), 0, 70, 60))
                self.nexImage += 1
                if(self.nexImage == 16):
                    self.nexImage = 0
            self.currentPosition[0] -= self.leftSpeed
            self.standingLeft = True
        if self.inAir is False and event[pygame.K_UP]:
            self.inAir = True
        if self.inAir is True and event[pygame.K_LEFT]:
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] -= self.leftSpeed
            if self.jumpingSpeed > 0:
                self.rect = self.screen.blit(self.jumpingL, tuple(
                    self.currentPosition), (125, 0, 65, 60))
            else:
                self.rect = self.screen.blit(self.jumpingL, tuple(
                    self.currentPosition), (60, 0, 65, 60))
            self.standingLeft = True

            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10
        elif self.inAir is True and event[pygame.K_RIGHT]:
            self.currentPosition[1] -= self.jumpingSpeed
            self.currentPosition[0] += self.rightSpeed
            if self.jumpingSpeed > 0:
                self.rect = self.screen.blit(self.jumpingR, tuple(
                    self.currentPosition), (150, 0, 65, 60))
            else:
                self.rect = self.screen.blit(self.jumpingR, tuple(
                    self.currentPosition), (215, 0, 65, 60))
            self.standingLeft = False
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10
        elif self.inAir is True:
            self.currentPosition[1] -= self.jumpingSpeed
            if self.standingLeft:
                if self.jumpingSpeed > 0:
                    self.rect = self.screen.blit(self.jumpingL, tuple(
                        self.currentPosition), (130, 0, 65, 60))
                else:
                    self.rect = self.screen.blit(self.jumpingL, tuple(
                        self.currentPosition), (60, 0, 65, 60))
            else:
                if self.jumpingSpeed > 0:
                    self.rect = self.screen.blit(self.jumpingR, tuple(
                        self.currentPosition), (150, 0, 65, 60))
                else:
                    self.rect = self.screen.blit(self.jumpingR, tuple(
                        self.currentPosition), (215, 0, 65, 60))
            self.jumpingSpeed -= 2
            if self.jumpingSpeed < -10:
                self.jumpingSpeed = -10

        self.rect.width -= 40
        self.rect.x += 20
        # colliding with a moving platform:
        movingVertCollisions = pygame.sprite.spritecollide(
            self, self.movingPlatforms, False)
        vertMovingPlatCollisions = pygame.sprite.spritecollide(
            self, self.vertMovingPlatforms, False)
        vertcollisions = pygame.sprite.spritecollide(
            self, self.platform1, False)
        vertcollisions2 = pygame.sprite.spritecollide(
            self, self.platform2, False)
        for platform in vertcollisions2:
            if self.rect.top < platform.rect.bottom and self.rect.top >= platform.rect.bottom - 15 and self.inAir == True:
                self.currentPosition[1] = platform.rect.bottom + 1
                self.jumpingSpeed = 0
        vertcollisions += vertMovingPlatCollisions
        vertcollisions += vertcollisions2
        vertcollisions += movingVertCollisions
        for sprite in vertcollisions:
            if self.rect.bottom > sprite.rect.top and self.rect.bottom <= sprite.rect.top + 15:
                self.inAir = False
                self.currentPosition[1] = sprite.rect.top - 59
                self.jumpingSpeed = 20
        for sprite in vertMovingPlatCollisions:
            if sprite.direction == 1 and self.rect.bottom > sprite.rect.top and self.rect.bottom <= sprite.rect.top + 15 and self.inAir == False:
                self.currentPosition[1] += sprite.speed
                self.rect.bottom += sprite.speed

        for sprite in movingVertCollisions:
            if self.rect.bottom > sprite.rect.top and self.rect.bottom <= sprite.rect.top + 15 and self.inAir == False:
                self.currentPosition[0] += sprite.speed * sprite.direction
                self.rect.x += sprite.speed * sprite.direction
        vertcollisions1 = [sprite for sprite in vertcollisions if self.rect.bottom >
                           sprite.rect.top and self.rect.bottom <= sprite.rect.top + 15]
        if len(vertcollisions1) == 0 and self.inAir is False:
            self.inAir = True
            self.jumpingSpeed = 0
        horizcollisions = pygame.sprite.spritecollide(
            self, self.platform2, False)
        horizcollisions1 = [sprite for sprite in horizcollisions if not (
            self.rect.bottom > sprite.rect.top and self.rect.bottom <= sprite.rect.top + 15)]
        isLeftCollided = False
        isRightCollided = False
        for sprite in horizcollisions1:
            if self.rect.left <= sprite.rect.right and self.rect.left >= sprite.rect.right - 25 and self.rect.bottom in range(sprite.rect.top + 22, sprite.rect.bottom + 10):
                self.leftSpeed = 0
                isLeftCollided = True
            else:
                if isLeftCollided == True:
                    pass
                else:
                    self.leftSpeed = self.defaultSpeed
            if self.rect.right >= sprite.rect.left and self.rect.right <= sprite.rect.left + 25 and self.rect.bottom in range(sprite.rect.top + 22, sprite.rect.bottom + 10):
                self.rightSpeed = 0
                isRightCollided = True
            else:
                if isRightCollided == True:
                    pass
                else:
                    self.rightSpeed = self.defaultSpeed
        if len(horizcollisions1) == 0:
            self.rightSpeed = self.defaultSpeed
            self.leftSpeed = self.defaultSpeed
        return self.rect, self.standingLeft

    def changeLevel(self, platform1, platform2, movingPlatforms, vertMovingPlatforms):
        self.platform1 = platform1
        self.platform2 = platform2
        self.movingPlatforms = movingPlatforms
        self.vertMovingPlatforms = vertMovingPlatforms

    def setLocation(self, x, y):
        self.currentPosition = [x, y]


class Enemy(GameObject):
    def __init__(self, x, y, screen, bulletGroup, type, coins):
        self.isLeft = True
        super().__init__(x, y, "enemyImages/enemyL.png")
        self.attackR = pygame.image.load("enemyAnimation/enemyattackR.png")
        self.attackL = pygame.image.load("enemyAnimation/enemyattackL.png")
        self.screen = screen
        self.currentLocation = [x, y]
        self.animateL = 0
        self.animateR = 0
        self.animateDelay = 10
        self.bulletGroup = bulletGroup
        self.type = type
        if type == "level1":
            self.sightRangex = 400
            self.sightRangey = 100
            self.bulletSpeed = 6
            self.health = 3
            self.maxHealth = 3
            self.attackR = pygame.image.load("enemyAnimation/enemyattackR.png")
            self.attackL = pygame.image.load("enemyAnimation/enemyattackL.png")
            self.animateDelay = 8
        elif type == "level2":
            self.sightRangex = 800
            self.sightRangey = 150
            self.bulletSpeed = 4
            self.health = 5
            self.maxHealth = 5
            self.attackR = pygame.image.load(
                "enemyAnimation/enemy2attackR.png")
            self.attackL = pygame.image.load(
                "enemyAnimation/enemy2attackL.png")
            self.animateDelay = 4
        elif type == "level3":
            self.sightRangex = 1000
            self.sightRangey = 100
            self.bulletSpeed = 8
            self.health = 8
            self.maxHealth = 8
            self.attackR = pygame.image.load(
                "enemyAnimation/enemy3attackR.png")
            self.attackL = pygame.image.load(
                "enemyAnimation/enemy3attackL.png")
            self.animateDelay = 3
        elif type == "startingEnemy":
            self.sightRangex = 200
            self.sightRangey = 100
            self.bulletSpeed = 6
            self.health = 3
            self.maxHealth = 3
            self.attackR = pygame.image.load("enemyAnimation/enemyattackR.png")
            self.attackL = pygame.image.load("enemyAnimation/enemyattackL.png")
            self.animateDelay = 8
        elif type == "boss":
            self.bulletSpeed = 2
            self.health = 20
            self.maxHealth = 20
            self.attackL = pygame.image.load(
                "enemyAnimation/enemyBOSS3attackL.png")
            self.animateDelay = 15
        self.coins = coins
        self.health_bar_length = 40
        self.health_bar_height = 5
        self.health_bar_pos = (self.rect.x + 22, self.rect.y + 5)

    def draw_health_bar(self):
        # current healthbar width
        health_bar_width = int(
            self.health / self.maxHealth * self.health_bar_length)
        # black part of the health bar
        pygame.draw.rect(self.screen, (0, 0, 0), (
            self.health_bar_pos[0], self.health_bar_pos[1], self.health_bar_length, self.health_bar_height))
        # red part of the health bar
        pygame.draw.rect(self.screen, (200, 70, 70), (
            self.health_bar_pos[0], self.health_bar_pos[1], health_bar_width, self.health_bar_height))

    def update(self):
        self.draw_health_bar()

    def handleBehaviour(self, bobby):
        if self.type == "level1" or self.type == "startingEnemy":
            if (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx < self.rect.centerx) or self.animateL != 0:
                self.animateR = 0
                if self.animateL // self.animateDelay == 0:
                    # hard coded cuz animations arent all the same size for some reason
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (295.2, 0, 73.8, 90))

                elif self.animateL // self.animateDelay == 1:
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (215, 0, 73.8, 90))

                elif self.animateL // self.animateDelay == 2:
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (140, 0, 73.8, 90))

                elif self.animateL // self.animateDelay == 3:
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (80, 0, 60, 90))

                elif self.animateL // self.animateDelay == 4:
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (0, 0, 78, 90))

                self.animateL += 1
                if self.animateL == self.animateDelay * 4 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, True, self.rect.x - 16, self.rect.y + 60, self.screen, 'rock'))
                if self.animateL == self.animateDelay * 5:
                    self.animateL = 0
            elif (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx >= self.rect.centerx) or self.animateR != 0:
                if self.animateR // self.animateDelay == 0:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (0, 0, 73.8, 90))

                elif self.animateR // self.animateDelay == 1:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (80, 0, 73.8, 90))

                elif self.animateR // self.animateDelay == 2:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (155, 0, 73.8, 90))

                elif self.animateR // self.animateDelay == 3:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (230, 0, 60, 90))

                elif self.animateR // self.animateDelay == 4:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (290, 0, 78, 90))

                self.animateR += 1
                if self.animateR == self.animateDelay * 4 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, False, self.rect.x + 78, self.rect.y + 60, self.screen, 'rock'))
                if self.animateR == self.animateDelay * 5:
                    self.animateR = 0
            elif bobby.rect.centerx < self.rect.centerx:
                self.rect = self.screen.blit(self.attackL, tuple(
                    self.currentLocation), (295.2, 0, 73.8, 90))
            else:
                self.rect = self.screen.blit(self.attackR, tuple(
                    self.currentLocation), (0, 0, 73.8, 90))
        if self.type == "level2":
            if (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx < self.rect.centerx) or self.animateL != 0:
                self.animateR = 0
                if self.animateL < self.animateDelay * 5:
                    # hard coded cuz animations arent all the same size for some reason
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (606 - (72 * (self.animateL // self.animateDelay)), 0, 71, 80))

                elif self.animateL < self.animateDelay * 9:
                    self.rect = self.screen.blit(self.attackL, tuple(
                        self.currentLocation), (323 - (82 * (self.animateL // self.animateDelay - 4)), 0, 75, 80))

                self.animateL += 1
                if self.animateL == self.animateDelay * 6 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, True, self.rect.x - 16, self.rect.y + 20, self.screen, 'axe'))
                if self.animateL == self.animateDelay * 9:
                    self.animateL = 0

            elif (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx >= self.rect.centerx) or self.animateR != 0:
                if self.animateR < self.animateDelay * 3:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (75 * (self.animateR // self.animateDelay), 0, 75, 80))

                elif self.animateR < self.animateDelay * 5:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (150 + 72 * (self.animateR // self.animateDelay - 2), 0, 71, 80))

                elif self.animateR < self.animateDelay * 9:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (285 + (82 * (self.animateR // self.animateDelay - 4)), 0, 75, 80))
                self.animateR += 1
                if self.animateR == self.animateDelay * 6 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, False, self.rect.x + 78, self.rect.y + 20, self.screen, 'axe'))
                if self.animateR == self.animateDelay * 9:
                    self.animateR = 0

            elif bobby.rect.centerx < self.rect.centerx:
                self.rect = self.screen.blit(self.attackL, tuple(
                    self.currentLocation), (605, 0, 75, 80))
            else:
                self.rect = self.screen.blit(self.attackR, tuple(
                    self.currentLocation), (0, 0, 75, 80))
        if self.type == "level3":
            if (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx < self.rect.centerx) or self.animateL != 0:
                self.animateR = 0
                self.rect = self.screen.blit(self.attackL, tuple(
                    self.currentLocation), (645 - (93 * (self.animateL // self.animateDelay)), 0, 75, 79))
                self.animateL += 1
                if self.animateL == self.animateDelay * 5 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, True, self.rect.x - 16, self.rect.y + 25, self.screen, 'axe'))
                if self.animateL == self.animateDelay * 8:
                    self.animateL = 0
            elif (abs(bobby.rect.centerx - self.rect.centerx) <= self.sightRangex and abs(bobby.rect.centery - self.rect.centery) <= self.sightRangey and bobby.rect.centerx >= self.rect.centerx) or self.animateR != 0:
                if self.animateR < self.animateDelay * 4:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (87 * (self.animateR // self.animateDelay), 0, 80, 79))
                else:
                    self.rect = self.screen.blit(self.attackR, tuple(
                        self.currentLocation), (355 + 90 * (self.animateR // self.animateDelay - 4), 0, 80, 79))
                self.animateR += 1
                if self.animateR == self.animateDelay * 5 + 2:
                    self.bulletGroup.add(EnemyBullet(
                        self.bulletSpeed, 1, False, self.rect.x + 78, self.rect.y + 25, self.screen, 'axe'))
                if self.animateR == self.animateDelay * 8:
                    self.animateR = 0
            elif bobby.rect.centerx < self.rect.centerx:
                self.rect = self.screen.blit(self.attackL, tuple(
                    self.currentLocation), (645, 0, 75, 79))
            else:
                self.rect = self.screen.blit(self.attackR, tuple(
                    self.currentLocation), (0, 0, 75, 79))
        if self.type == "boss":
            self.rect = self.screen.blit(self.attackL, tuple(
                self.currentLocation), (800 - (115 * (self.animateL // self.animateDelay)), 0, 103, 100))
            self.animateL += 1
            if self.animateL == self.animateDelay * 5 + 2:
                self.bulletGroup.add(EnemyBullet(
                    self.bulletSpeed, 1, True, self.rect.x - 16, self.rect.y + 25, self.screen, 'axe'))
            if self.animateL == self.animateDelay * 8:
                self.animateL = 0
        self.rect.x += 15
        self.rect.y += 10
        self.rect.width -= 15
        self.rect.height -= 10
        if self.health <= 0:
            if self.type == "level1" or self.type == "startingEnemy":
                self.coins.add(
                    coin(self.rect.x + 10, self.rect.y + 52, 5, self.screen))
                self.kill()
                del self
            elif self.type == "level2":
                self.coins.add(
                    coin(self.rect.x + 10, self.rect.y + 43, 10, self.screen))
                self.kill()
                del self
            elif self.type == "level3":
                self.coins.add(
                    coin(self.rect.x + 10, self.rect.y + 43, 20, self.screen))
                self.kill()
                del self
            else:
                self.coins.add(
                    coin(self.rect.x + 15, self.rect.y + 65, 100, self.screen))
                self.kill()
                del self

    def loseHp(self, damage):
        self.health = self.health - damage


class PlatForms(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)


class LavaPool(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)


class MovingPlatForms(GameObject):
    def __init__(self, x, y, speed, stopLeft, stopRight, img_path):
        super().__init__(x, y, img_path)
        self.direction = 1
        self.speed = speed
        self.stopLeft = stopLeft
        self.stopRight = stopRight

    def update(self):
        if self.x <= self.stopLeft:
            # start moving right once it has reached the left most position.
            self.direction = 1
        elif self.x >= self.stopRight:
            # start moving left once it has reached the right most position.
            self.direction = -1
        self.x += self.speed * self.direction
        self.rect.x = self.x  # Update the position of the sprite based on the new x value


class VertMovingPlatForms(GameObject):
    def __init__(self, x, y, speed, stopUp, stopDown, img_path):
        super().__init__(x, y, img_path)
        self.direction = -1
        self.speed = speed
        self.stopUp = stopUp
        self.stopDown = stopDown

    def update(self):
        if self.y <= self.stopUp:
            # start moving right once it has reached the left most position.
            self.direction = 1
        elif self.y >= self.stopDown:
            # start moving left once it has reached the right most position.
            self.direction = -1
        self.y += self.speed * self.direction
        self.rect.y = self.y  # Update the position of the sprite based on the new x value


class coin(GameObject):
    def __init__(self, x, y, value, screen):
        super().__init__(x, y, "statsImages/coinAnimation.png")
        self.value = value
        self.animation = pygame.image.load("statsImages/coinAnimation.png")
        self.timer = 0
        self.screen = screen
        self.currentLocation = [x, y]

    def animate(self):
        if self.timer // 3 == 0:
            self.rect = self.screen.blit(self.animation, tuple(
                self.currentLocation), (0, 0, 25, 25))
        elif self.timer // 3 >= 1:
            self.rect = self.screen.blit(self.animation, tuple(
                self.currentLocation), ((self.timer // 3) * 30 - 2, 0, 25, 25))
        self.timer += 1
        if self.timer >= 18:
            self.timer = 0


class Stats(GameObject):
    def __init__(self, x, y, img_path):
        super().__init__(x, y, img_path)
