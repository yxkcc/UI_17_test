# 导包 日志
import logging

# 定义路径
path = "./aaa.log"
# 格式化字符串
fmt = "%(asctime)s - %(levelname)s - [%(filename)s - %(funcName)s - %(lineno)d] - %(message)s"
# 设置基础日志级别(level) 格式化输出(format) 路径(filename)
logging.basicConfig(level=logging.INFO, format=fmt, filename=path)
"""
level=logging.INFO
        logging.DEBUG
        logging.WARNING
        logging.ERROR
        logging.CRITICAL
"""
# 输出信息 -默认输出到控制台
# 默认只能输出大于等于 warning级别的日志
logging.debug("我是debug")  # 中文会乱码
logging.info("我是info")
logging.warning("我是warning")
logging.error("我是error")
logging.critical("我是critical")
