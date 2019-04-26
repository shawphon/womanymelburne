"""
Generated by leslie in shanghai, @leadrive.
Version 2.0
name: modi_init_mcan_port.py
time: 2019年3月20日10:18:32

kep o mvi
"""

from packages.basic.basic_functions import*
from packages.basic.log import Set_Log

import os
import logging

def Modi_Init_Macan_Port():
	"""修改init_mcan_port.c程序代码"""
	
	#创建日志
	log_name = 'run_log.log'
	log_path = os.path.abspath('.')
	init_log = Set_Log(log_name, log_path, logger_name='init_log')
	
	file_name = 'pending_file/init_mcan_port.c'
	gen_file_name = 'processed_file/init_mcan_port.c'
	
	comm_out_code = '#include "pinmapper/aurix_pin_mappings.h"'	#需注释的代码
	before_code = '#include "MultiCAN/Std/IfxMultican.h"'	#前一段代码
	add_code = (	
		'\n// can0_node0',
		'#define IFXCFG_MULTICAN0_0_RXD                  IfxMultican_RXD0G_P34_2_IN',
		'#define IFXCFG_MULTICAN0_0_RXD_MODE             IfxPort_InputMode_pullUp',
		'#define IFXCFG_MULTICAN0_0_RXD_PAD_DRIVER       IfxPort_PadDriver_cmosAutomotiveSpeed1',
		'#define IFXCFG_MULTICAN0_0_TXD                  IfxMultican_TXD0_P34_1_OUT',
		'#define IFXCFG_MULTICAN0_0_TXD_MODE             IfxPort_OutputMode_pushPull',
		'#define IFXCFG_MULTICAN0_0_TXD_PAD_DRIVER       IfxPort_PadDriver_cmosAutomotiveSpeed4',
		' ',
		'// can0_node1',
		'#define IFXCFG_MULTICAN0_1_RXD                  IfxMultican_RXD1B_P14_1_IN',
		'#define IFXCFG_MULTICAN0_1_RXD_MODE             IfxPort_InputMode_pullUp',
		'#define IFXCFG_MULTICAN0_1_RXD_PAD_DRIVER       IfxPort_PadDriver_cmosAutomotiveSpeed1',
		'#define IFXCFG_MULTICAN0_1_TXD                  IfxMultican_TXD1_P14_0_OUT',
		'#define IFXCFG_MULTICAN0_1_TXD_MODE             IfxPort_OutputMode_pushPull',
		'#define IFXCFG_MULTICAN0_1_TXD_PAD_DRIVER       IfxPort_PadDriver_cmosAutomotiveSpeed4',
		)	#添加代码
	
	if os.path.exists(file_name):
		print("# find and open file " + file_name + " successfully.")
		init_log.info("# find and open file " + file_name + " successfully.")
		
		lines = Read_File(file_name)
		print("# Read file " + file_name + " successfully.")
		init_log.info("Read file " + file_name + " successfully.")
		
		lines = Comm_Out(lines, comm_out_code)
		print("# Comment out code successfully.")
		init_log.info("Comment out code successfully.")
		
		lines = Add(lines, add_code, before_code)
		Write_File(gen_file_name, lines)
		print("# Creat a new file in pending_file folder successfully.")
		init_log.info("Creat a new file in pending_file folder successfully.")
		
		#Show_File(gen_file_name)
	else:
		print("# Not find the file " + file_name + ".")
	
