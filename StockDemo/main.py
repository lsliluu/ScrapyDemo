from scrapy import cmdline
from scrapy import spiderloader
from scrapy.utils import project


print('正在初始化数据...')
# 获取项目中所有的spiders列表
settings = project.get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
spiders = spider_loader.list()
# classes = [spider_loader.load(name) for name in spiders]
print('启动程序，退出请输入exit')
while True:
    # 从命令行中获取到要爬取的 spider name
    spider_name = input('请输入要爬取的Spider name：')
    if spider_name == 'exit':
        print('正在退出爬虫程序...')
        break
    if spider_name not in spiders:
        print('未找到输入的Spider name，请重试')
    else:
        # 组装成命令
        my_cmd = u'scrapy crawl ' + spider_name
        print(my_cmd)
        # 执行命令
        cmdline.execute(my_cmd.split())
