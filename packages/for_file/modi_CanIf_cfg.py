"""
Geerated by Leslie in shanghai @leadrive
Time: 2019年4月10日12:38:15
Version：2.4

Kep o mvi
"""

from packages.basic.basic_functions import *
from packages.for_file.modi_Can_Cfg import Frame_change

import logging
import time
import os

#创建日志
log_name = 'run_log.log'
log_path = os.path.abspath('.')
log = Set_Log(log_name, log_path, logger_name='CanIf_cfg')

def Modi_CanIf_cfg(str_CAN_mode):
	"""对文件中帧类型依据CSV文件中的帧格式进行配置"""
	if str_CAN_mode == '1':
		ori_file_name = 'pending_file\\CanIf_cfg.h'
		new_file_name = 'processed_file\\CanIf_cfg.h'
		
		#read file
		lines = Read_File(ori_file_name)
		log.info("# Read source file successfully:" + ori_file_name)
		print("# Read source file successfully:" + ori_file_name)
		
		#change the type of frame according to parameters in CSV file
		lines = Frame_change(lines,str_sear_code='#define CANIF_EXTENDED_ID')
		log.info("# Frame Type is changed correctly.")
		
		#Write file
		Write_File(new_file_name, lines)
		log.info("# Creat a new file in pending_file folder successfully.")
		print("# Creat a new file in pending_file folder successfully.")
		
	else:
		log.info("# Stardard mode, file, 'CanIf_cfg.h' is no need to be modified.")
		print("# Stardard mode, file, 'CanIf_cfg.h' is no need to be modified.")
	
