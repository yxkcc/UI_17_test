import logging.handlers


def log_conf():
    # 声明日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 声明处理器 -控制台
    sh = logging.StreamHandler()
    # 声明处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename="./Log/hm.log", when="midnight", interval=1, backupCount=7,
                                                     encoding="utf-8")
    # 格式化字符串
    fmt = "%(asctime)s - %(levelname)s - [%(filename)s - %(funcName)s - %(lineno)d] - %(message)s"
    # 声明格式化器
    formatter = logging.Formatter(fmt)
    # 格式化器 添加到 处理器 -控制台
    sh.setFormatter(formatter)
    # 格式化器 添加到 处理器 -文件
    trfh.setFormatter(formatter)
    # 处理器 -控制台 添加到日志器
    logger.addHandler(sh)
    # 处理器 -文件 添加到日志器
    logger.addHandler(trfh)
