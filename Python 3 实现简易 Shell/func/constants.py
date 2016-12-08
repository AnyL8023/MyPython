#-*- code=utf-8 -*-
import os

# Shell 进程的停止标识
SHELL_STATUS_STOP = 0
# Shell 进程的运行标识
SHELL_STATUS_RUN = 1

# 命令日志的存储路径
# 使用 os.path.expanduser('~') 获取当前操作系统平台的当前用户根目录
HISTORY_PATH = os.path.expanduser('~') + os.sep + '.shiyanlou_shell_history'