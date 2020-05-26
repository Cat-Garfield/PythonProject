本内容包含一些爬虫的操作记录  
Scrapy基本命令：  
&emsp;1.创建Scrapy项目：scrapy startproject 项目名  
&emsp;2.创建爬虫  
&emsp;&emsp;1.切换到Scrapy项目目录：cd grab_moe_image  
&emsp;&emsp;2.创建爬虫：scrapy genspider example example.com  
&emsp;3.启动爬虫  
&emsp;&emsp;1.项目命令：scrapy crawl spidername  
&emsp;&emsp;2.全局命令：scrapy runspider <example.py>  
&emsp;&emsp;3.启动所有爬虫：scrapy crawl all  
项目结构：  
&emsp;|____scrapy.cfg  
&emsp;|____test  
&emsp;&emsp;| |______init__.py  
&emsp;&emsp;| |____items.py  
&emsp;&emsp;| |____middlewares.py  
&emsp;&emsp;| |____pipelines.py  
&emsp;&emsp;| |____settings.py  
&emsp;&emsp;| |____spiders  
&emsp;&emsp;| | |______init__.py  