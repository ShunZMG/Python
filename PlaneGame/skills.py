import pygame, sys
from pygame import *
import os

class Myskills(pygame.sprite.Sprite):
	def  __init__(self, mename):
		pygame.sprite.Sprite.__init__(self)
		
		# 赤机激光
		self.red_skill = pygame.transform.scale(pygame.image.load('./images/ray.png').convert_alpha(), (100, 800))

		# 橙机炮弹
		self.orange_skill = pygame.transform.scale(pygame.image.load('./images/fine.png').convert_alpha(), (800, 400))

		# 黄色战机技能敌方停止移动

		# 绿色战机技能回复生命值

		# 青色战机技能在前方设置屏障
		self.light_green_skill = pygame.transform.scale(pygame.image.load('./images/bullet.png').convert_alpha(), (1500, 20))

		# 蓝色战机护盾技能
		self.blue_skill = pygame.transform.scale(pygame.image.load('./images/bullet.png').convert_alpha(), (250, 250))

		# 技能时间
		self.continue_time = 0
		# 技能判定状态
		self.power = 0
		# 玩家
		self.me = mename
		# 技能判定
		self.judge = False
		# 技能flag
		self.flag = False
		# 默认发射子弹
		self.bullet = True
		# 默认敌机移动
		self.move = True
		# 我方障碍
		self.my_move1 = True
		self.my_move2 = True

	# 破坏3架战机power满
	def skill_status(self):
		if self.power == 3:
			return True
		else:
			return False

	# 赤色战机技能
	def red_skill_way(self, delay, position):
		if not self.flag:
			self.rect = self.red_skill.get_rect()
			self.mask = pygame.mask.from_surface(self.red_skill)
			self.bullet = not self.bullet
			self.flag = not self.flag
		self.rect.midbottom = position
		# 技能时长5秒
		if not delay % 40:
			self.continue_time += 1
			if not self.continue_time % 5:
				self.flag = not self.flag
				self.bullet = not self.bullet
				self.judge = False
		# 清除消灭敌机数量
		self.power = 0

	# 橙色战机技能
	def orange_skill_way(self, delay, position):
		if not self.flag:
			self.rect = self.orange_skill.get_rect()
			self.mask = pygame.mask.from_surface(self.orange_skill)
			self.rect.midbottom = position
			self.flag = not self.flag
		# 炮弹速度
		if not delay % 3:
			if self.rect.bottom >= 0:
				self.rect.top -= 6
			else:
				self.flag = not self.flag
				self.judge = False
		# 清除消灭敌机数量,重置技能值
		self.power = 0

	# 黄色战机技能
	def yellow_skill_way(self, delay):
		if not self.flag:
			self.move = not self.move
			self.flag = not self.flag
		# 技能时长5秒
		if not delay % 40:
			self.continue_time += 1
			if not self.continue_time % 5:
				self.flag = not self.flag
				self.move = not self.move
				self.judge = False
		# 清除消灭敌机数量
		self.power = 0

	# 绿色战机技能
	def green_skill_way(self):
		self.judge = False
		self.power = 0

	# 青色战机技能
	def light_green_skill_way(self, delay, me):
		if not self.flag:
			self.rect = self.light_green_skill.get_rect()
			self.mask = pygame.mask.from_surface(self.light_green_skill)
			self.rect.midbottom = me.rect.midtop
			self.rect.top -= 150
			self.flag = not self.flag
		# 技能
		if self.rect.centery < me.rect.top:
			if self.rect.bottom >= me.rect.top:
				self.my_move1 = False
			else:
				self.my_move1 = True
		if self.rect.centery > me.rect.bottom:
			if self.rect.top <= me.rect.bottom:
				self.my_move2 = False
			else:
				self.my_move2 = True
		# 技能时长5秒
		if not delay % 40:
			self.continue_time += 1
			if not self.continue_time % 8:
				self.flag = not self.flag
				self.judge = False
				self.my_move1 = True
				self.my_move2 = True

		# 清除消灭敌机数量
		self.power = 0

	# 蓝色战机技能
	def blue_skill_way(self, delay, me):
		if not self.flag:
			self.rect = self.blue_skill.get_rect()
			self.mask = pygame.mask.from_surface(self.blue_skill)
			self.flag = not self.flag
		self.rect.centerx, self.rect.centery = me.rect.centerx, me.rect.centery
		# 技能时长5秒
		if not delay % 40:
			self.continue_time += 1
			if not self.continue_time % 8:
				self.flag = not self.flag
				self.judge = False
		# 清除消灭敌机数量
		self.power = 0

	def purple_skill_way(self):
		self.power = 0
		self.judge = False
