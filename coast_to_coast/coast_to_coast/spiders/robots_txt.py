# -*- coding: utf-8 -*-
import scrapy
import json
import os, glob
import re

class RobotsTxtSpider(scrapy.Spider):
	name = 'robots_txt'
	allowed_domains = ['muttonheadstore.com']
	start_urls = ['https://muttonheadstore.com/']
	folder = "scraped"

	def parse(self, response):
		robot_url = response.url + "robots.txt"
		# prepare output folder
		if not os.path.exists(self.folder):
			os.remove
			os.makedirs(self.folder)
		else:
			filelist = glob.glob("./" + self.folder + "/*")
			for f in filelist:
				os.remove(f)

		if re.search("shopify", response.text, re.IGNORECASE) != None:
			url = response.url + "products.json"
			return scrapy.http.Request(url=url, callback=self.downloadJSON)
		else:
			url = response.url + "sitemap.xml"
			return scrapy.http.Request(url=url, callback=self.downloadXML)

	def downloadJSON(self, response):
		with open(self.folder + "/" + self.domain(response.url), "w") as file:
			data = json.loads(response.text)
			json.dump(data, file, indent=2)
			file.close()

	def downloadXML(self, response):
		filepath = self.folder + "/" + self.domain(response.url)
		with open(filepath, "w") as file:
			file.write(response.text)
			file.close()

	def domain(self, url):
		return url.split("/")[2]