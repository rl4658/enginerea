import GameObject
import pygame
import os


class Shop:
    def __init__(self, screen, playerObject):
        self.screen = screen
        self.bobby = playerObject
        self.isOpen = False

        #fonts and backgrounds
        self.UpgradeFrame = pygame.image.load("shopImages/UpgradePage.png")
        self.playerFrame = pygame.image.load("shopImages/PlayerViewPage.png")
        self.shopBackground = pygame.image.load("shopImages/ShopBg.png")
        self.font = pygame.font.Font("Fonts/titles.otf", 35)
        self.Statsupgrades_label = self.font.render('Stats', True, (255, 226, 183))
        self.Equipmentupgrades_label = self.font.render('Equipment', True, (255, 226, 183))
        self.player_label = self.font.render("Bobby", True, (255, 226, 183))
        self.LeftStatsFont = pygame.font.Font("Fonts/titles.otf", 24)

        #Statsbuttons and fonts
        self.attackBtn = GameObject.GameObject(950, 190, "Buttons/AttackUpgradeBtn.png")
        self.healthBtn = GameObject.GameObject(890, 325, "Buttons/HealthUpgradeBtn.png")
        self.speedBtn = GameObject.GameObject(1020, 325, "Buttons/SorcShoesUpgradeBtn.png")
        self.StatsFont = pygame.font.SysFont("Fonts/Stats.ttf", 20)
        self.HealthTitle = self.StatsFont.render("Health +1", True, (0, 0, 0))
        self.DamageTitle = self.StatsFont.render("Damage +1", True, (0, 0, 0))
        self.SpeedTitle = self.StatsFont.render("Speed +1", True, (0, 0, 0))

        # Icon Images
        self.healthIcon = GameObject.GameObject(420, 30, "statsImages/heart.png")
        self.attackIcon = GameObject.GameObject(499, 30, "statsImages/strength.png")
        self.armourIcon = GameObject.GameObject(580, 30, "statsImages/shieldIcon.png")
        self.SpeedIcon = GameObject.GameObject(660, 30, "statsImages/SpeedIcon.png")
        self.moneyIcon = GameObject.GameObject(740, 30, "statsImages/coin.png")

        self.WoodTitle2 = self.StatsFont.render("Armour +3", True, (0, 0, 0))
        self.AxeTitle2 = self.StatsFont.render("Damage +6", True, (0, 0, 0))
        self.SteelTitle2 = self.StatsFont.render("Armour +5", True, (0, 0, 0))
        # Equipment Button
        self.axeBtn = GameObject.GameObject(140, 190, "Buttons/AxeButton.png")
        self.shield1Btn = GameObject.GameObject(70, 325, "Buttons/Shield1Button.png")
        self.shield2Btn = GameObject.GameObject(200, 325, "Buttons/Shield2Button.png")
        self.axeBtnNotPushed = True
        self.shield1BtnNotPushed = True
        self.shield2BtnNotPushed = True

        # character
        self.axeType = "1"
        self.shieldType = "0"

        # Sound Effects
        self.success_sound = pygame.mixer.Sound("SoundEffects/successful.wav")
        self.success_sound.set_volume(0.2)
        self.unsuccessful_sound = pygame.mixer.Sound("SoundEffects/unsuccessful.wav")
        self.unsuccessful_sound.set_volume(0.2)

    def renderShop(self):
        pygame.display.set_caption("Shop Menu")
        while self.isOpen:
            for event in pygame.event.get():
                self.WorkingBobbyImageInShop = GameObject.GameObject(500, 260, "ShopImages/ShopUpgradeImages/StandingAxe"+self.axeType+"Shield"+self.shieldType+"L.png")
                self.bobby.walkingR = pygame.image.load("ShopImages/WalkingR/WalkingAxe"+self.axeType+"Shield"+self.shieldType+"R.png")
                self.bobby.walkingL = pygame.image.load("ShopImages/WalkingL/WalkingAxe"+self.axeType+"Shield"+self.shieldType+"L.png")
                self.bobby.standingL = pygame.image.load("ShopImages/StandingL/StandingAxe"+self.axeType+"Shield"+self.shieldType+"L.png")
                self.bobby.standingR = pygame.image.load("ShopImages/StandingR/StandingAxe"+self.axeType+"Shield"+self.shieldType+"R.png")

                if event.type == pygame.QUIT:
                    self.isOpen = False
                    return self.bobby
                if event.type == pygame.MOUSEBUTTONDOWN and self.healthBtn.rect.collidepoint(event.pos):
                    if self.bobby.money >= 10:
                        self.bobby.money -= 10
                        self.bobby.health += 1
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and self.attackBtn.rect.collidepoint(event.pos):
                    if self.bobby.money >= 10:
                        self.bobby.money -= 10
                        self.bobby.attack += 1
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and self.speedBtn.rect.collidepoint(event.pos):
                    if self.bobby.money >= 10 and self.bobby.defaultSpeed < 10:
                        self.bobby.money -= 10
                        self.bobby.defaultSpeed += 1
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and self.axeBtn.rect.collidepoint(event.pos) and self.axeBtnNotPushed:
                    if self.bobby.money >= 50:
                        self.bobby.money -= 50
                        self.axeBtnNotPushed = False
                        self.axeType = "2"
                        self.bobby.attack += 6
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                elif not self.axeBtnNotPushed and event.type == pygame.MOUSEBUTTONDOWN and self.axeBtn.rect.collidepoint(event.pos):
                    self.unsuccessful_sound.play()

                if event.type == pygame.MOUSEBUTTONDOWN and self.shield1Btn.rect.collidepoint(event.pos) and self.shield1BtnNotPushed:
                    if self.bobby.money >= 30:
                        self.bobby.money -= 30
                        self.shield1BtnNotPushed = False
                        self.shieldType = "1"
                        self.bobby.armour = 3
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                elif not self.shield1BtnNotPushed and event.type == pygame.MOUSEBUTTONDOWN and self.shield1Btn.rect.collidepoint(event.pos):
                    self.unsuccessful_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and self.shield2Btn.rect.collidepoint(event.pos) and self.shield2BtnNotPushed:
                    if self.bobby.money >= 40:
                        self.bobby.money -= 40
                        self.shield2BtnNotPushed = False
                        self.shieldType = "2"
                        self.bobby.armour = 5
                        self.success_sound.play()
                    else:
                        self.unsuccessful_sound.play()
                elif not self.shield2BtnNotPushed and event.type == pygame.MOUSEBUTTONDOWN and self.shield2Btn.rect.collidepoint(event.pos):
                    self.unsuccessful_sound.play()

                # Backgrounds
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.shopBackground, (0, -12))
                self.screen.blit(self.UpgradeFrame, (1, 15))
                self.screen.blit(self.UpgradeFrame, (810, 15))
                self.screen.blit(self.playerFrame, (445, 100))
                self.screen.blit(self.Equipmentupgrades_label, (117, 60))
                self.screen.blit(self.Statsupgrades_label, (965, 60))
                self.screen.blit(self.player_label, (550, 130))
                # Buttons
                self.screen.blit(self.shield1Btn.image, self.shield1Btn.rect)
                self.screen.blit(self.shield2Btn.image, self.shield2Btn.rect)
                self.screen.blit(self.axeBtn.image, self.axeBtn.rect)
                self.screen.blit(self.attackBtn.image, self.attackBtn.rect)
                self.screen.blit(self.speedBtn.image, self.speedBtn.rect)
                self.screen.blit(self.healthBtn.image, self.healthBtn.rect)
                self.screen.blit(self.HealthTitle, (920, 305))
                self.screen.blit(self.DamageTitle, (980, 170))
                self.screen.blit(self.SpeedTitle, (1055, 305))
                # Shields and Axe Upgrade Buttons
                self.screen.blit(self.WoodTitle2, (100, 305))
                self.screen.blit(self.AxeTitle2, (170, 170))
                self.screen.blit(self.SteelTitle2, (225, 305))

                # Value of Stats
                self.health = self.LeftStatsFont.render(str(self.bobby.health), True, (0, 0, 0))
                self.attack = self.LeftStatsFont.render(str(self.bobby.attack), True, (0, 0, 0))
                self.money = self.LeftStatsFont.render(str(self.bobby.money), True, (0, 0, 0))
                self.armour = self.LeftStatsFont.render(str(self.bobby.armour), True, (0, 0, 0))
                self.speed = self.LeftStatsFont.render(str(self.bobby.defaultSpeed), True, (0, 0, 0))

                # image of bobby
                self.screen.blit(self.WorkingBobbyImageInShop.image, self.WorkingBobbyImageInShop.rect)
                self.renderShopStats()
                pygame.display.flip()

    def renderShopStats(self):
        self.screen.blit(self.healthIcon.image, self.healthIcon.rect)
        self.screen.blit(self.attackIcon.image, self.attackIcon.rect)
        self.screen.blit(self.moneyIcon.image, self.moneyIcon.rect)
        self.screen.blit(self.armourIcon.image, self.armourIcon.rect)
        self.screen.blit(self.SpeedIcon.image, self.SpeedIcon.rect)
        self.screen.blit(self.health, (470, 30))
        self.screen.blit(self.attack, (554, 30))
        self.screen.blit(self.armour, (630, 30))
        self.screen.blit(self.speed, (710, 30))
        self.screen.blit(self.money, (780, 30))