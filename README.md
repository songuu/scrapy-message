# 爬去学校官网的自己的信息
### 使用python scrapy工具

### 操作步骤

#### 安装scrapy 

``` 
使用pip安装 pip install scrapy
```

#### 创建项目

```
scrapy starproject projectname
```
#### 项目主要结构
![项目结构](http://pa5114ths.bkt.clouddn.com/project.jpg)

#### 本项目主要信息配置

1. 配置setting界面内容，
主要是配置mysql的全局信息和配置存储到mysql和json文件的信息，以及爬虫的主要信息
> BOT_NAME = ''  爬虫名字 
SPIDER_MODULES = [''] 爬虫模块
NEWSPIDER_MODULE = '' 爬虫模块

>MYSQL_HOST='localhost'
MYSQL_PORT=3306
MYSQL_USER=''  数据库用户名字
MYSQL_PASSWD='' 数据库用户密码
MYSQL_DBNAME='' 数据库名字

2. 配置主要爬虫界面

初始化爬虫名字，和开始url。
还有根据自己的学校配置子url

3. 配置存储界面

主要是pipelines和middlewares
自己根据提示信息进行配置

#### 开始项目

1. 使用scrapy runspider projectname
2. 使用scrapy crawl project.name


更多的信息配置请查看我的的[宋钰的博客](博客)