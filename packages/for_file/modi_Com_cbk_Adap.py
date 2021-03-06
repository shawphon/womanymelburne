"""
Generated by leslie in shanghai, @leadrive.
Version 2.0
name: modi_Com_Cbk_Adap.py
time: 2019年3月20日11:18:17

kep o mvi
"""
from packages.basic.basic_functions import *
from packages.basic.log import Set_Log
from packages.for_file.modi_Com_cfg import *

import os
import sys
import csv
import logging

#创建日志
log_name = 'run_log.log'
log_path = os.path.abspath('.')
log = Set_Log(log_name, log_path, logger_name='com_cbk_log')

def Modi_Com_Cbk_Adap(dbcname, dic):
	"""修改Com_Cbk_Adap.c程序"""
	
	ori_file_name = 'pending_file/Com_Cbk_Adap.c'
	gen_file_name = 'processed_file/Com_Cbk_Adap.c'
	
	if os.path.exists(ori_file_name):
		print("# find and open file " + ori_file_name + " successfully.")
		log.info("# find and open file " + ori_file_name + " successfully.")
		dbclines = Read_File(dbcname)
		idandNameDic = OutIdandName(dbclines)
		
		#读取文件
		lines = Read_File(ori_file_name)
		print("# Read file " + ori_file_name + "successfully.")
		log.info("# Read file " + ori_file_name + "successfully.")
		
		flag = 0
		gathers = []
		#print(dic)
		for key in dic.keys():
			#print(key)
			#print(idandNameDic.values())
			if key in idandNameDic.values():
				
				#获取MCU种类
				gathers.append(dic[key])
				
				#为某些报文配置接收计数代码
				before_code = 'get_'+ key +'();'
				#print(before_code)
				add_code = ['\trxCntVCU2' + dic[key] + '++;']
				lines = Add(lines, add_code, before_code)
				
				#为某些报文配置超时丢失代码
				before_code = 'void Com_RxTimeoutCbk_' + key +'(void)'
				add_code = ['\ttimeoutCntVCU2' + dic[key] + '++;']
				lines = Add(lines, add_code, before_code, offset=1)
				flag = 1
				
		if flag != 1:
			print('spell Error', key)
			log.info('spell Error')
			sys.stdin.readline()
			exit()
		
		
		#添加代码
		add_code = []
		before_code = '#include "Com.h"'	
		for gather in gathers:
			add_code.append('uint32 timeoutCntVCU2' + gather + ';')
		for gather in gathers:
			add_code.append('uint32 rxCntVCU2' + gather + ';')
		Add(lines, add_code, before_code)

		print("# Add code successfully.")
		log.info("# Add code successfully.")
			
		#写入文件
		Write_File(gen_file_name, lines)
		print("# Creat a new file in pending_file folder successfully.")
		log.info("Creat a new file in pending_file folder successfully.")
		#Show_File(gen_file_name)
	else:
		print("没有找到文件！" + ori_file_name)

