"""
Generated by leslie in shanghai, @leadrive.
Version 2.0
name: main.py
time: 2019年3月20日10:18:32

kep o mvi
"""
from packages.for_file.modi_init_mcan_port import Modi_Init_Macan_Port
from packages.for_file.modi_Com_cbk_Adap import Modi_Com_Cbk_Adap
from packages.for_file.modi_PduR_PBcfg import Modi_PduR_PBcfg
from packages.for_file.modi_Can_PBCfg import Modi_Can_PBCfg
from packages.for_file.modi_Can_Cfg import Modi_Can_Cfg
from packages.for_file.modi_CanIf_cfg import Modi_CanIf_cfg
from packages.for_file.modi_Com_cfg import Modi_Com_cfg
from packages.basic.log import Set_Log
from packages.basic.basic_functions import Check_File,Copy_Files

import os
import sys
import csv
import logging

log_name = 'run_log.log'
log_path = os.path.abspath('.')
log = Set_Log(log_name, log_path)

def Mainfuction():
	'''文件处理'''
	
	str_path = 'pending_file\\'
	files_name = ['Can_Cfg.h', 'Can_PBCfg.c', 'CanIf_cfg.h',
		'CanIf_PBcfg.c', 'Com_Cbk.h', 'Com_Cbk_Adap.c',
		'Com_cfg.c', 'Com_cfg.h', 'init_mcan_port.c', 
		'PduR_cfg.h', 'PduR_PBcfg.c', 'rte_com.c',
		'rte_com.h'
		]
	Check_File(files_name, files_path=str_path, logger_path=log_path)
	
	#copy all files
	source_dir = 'pending_file'
	target_dir = 'processed_file'
	Copy_Files(source_dir, target_dir)
	
	# Check and Read CSV file and initial
	try:
		with open('Configuration.csv') as file_object:
			dic = {}
			reader = csv.reader(file_object)
			header_line = ' '
			while header_line:
				try:
					header_line = next(reader)
					key = header_line[0].strip()
					dic[key] = header_line[1].strip()
				except:
					break
			print('\nCSV file is ready.')
	except:
		print('# Configuration.csv file is not found.')
		log.info('# Configuration.csv file is not found.')
		sys.stdin.readline()
		exit()
	
	frame_type = 'FrameType'
	bswtimebase = 'BSWTimeBase'
	dbcname = 'DBCName'
	dbcfile_name = []
	if frame_type not in dic.keys():
		print(dic)
		log.info("Spelling Error in Configuration.csv: Frame type.")
		print("Spelling Error in Configuration.csv: Frame type.")
		sys.stdin.readline()
		exit()	
	str_CAN_mode = dic[frame_type]
	if str_CAN_mode != '0' and str_CAN_mode != '1':
		log.info('FrameType can only be set as 1 and 0 in Configuration.csv. please recheck for it.')
		print('FrameType can only be set as 1 and 0 in Configuration.csv. please recheck for it.')
		sys.stdin.readline()
		exit()
	str_bswtimebase = dic[bswtimebase]
	
	#Check DBC file
	if dic[dbcname]:		
		dbcfile_name.append(dic[dbcname])
	else:
		log.info('no valid dbc file name in CSV file.')
		print('no valid dbc file name in CSV file.')
		sys.stdin.readline()
		exit()
	Check_File(dbcfile_name, logger_path=log_path)
	print(dic[dbcname]+' is ready.')
	
	print("\t****************All Flies are ready.*********************\t\n\n")
	log.info("**********************All Flies are ready.*************************************\n\n")
	
	#modifiy init_mcan_port
	print("#####################Step1: process init_mcan_port.c#######################")
	log.info("#####################Step1: process init_mcan_port.c#########################")
	
	Modi_Init_Macan_Port()
	
	print("**********************End process init_mcan_port.c*************************\n\n")
	log.info("**********************End process init_mcan_port.c*************************************\n\n")
	
	#modify Com_Cbk_Adap
	print("#####################Step2: process Com_Cbk_Adap.c#########################")
	log.info("#####################Step2: process Com_Cbk_Adap.c##########################")
	
	Modi_Com_Cbk_Adap(dic[dbcname],dic)
	
	print("*******************End process Com_Cbk_Adap.c******************************\n\n")
	log.info("**********************End process Com_Cbk_Adap.c***************************\n\n")
	
	#modify PduR_PBcfg
	print("#####################Step3: process PduR_PBcfg.c###########################")
	log.info("#####################Step3: process PduR_PBcfg.c##############################")
	
	Modi_PduR_PBcfg(dic[dbcname])
	
	print("***********************End process PduR_PBcfg.c****************************\n\n")
	log.info("***********************End process PduR_PBcfg.c****************************\n\n")
	
	#modify Can_PBCfg
	print("#####################Step4: process Can_PBCfg.c############################")
	log.info("#####################Step4: process Can_PBCfg.c###############################")
	
	Modi_Can_PBCfg(str_CAN_mode, dic[dbcname])
	
	print("***********************End process Can_PBCfg.c*****************************\n\n")
	log.info("***********************End process Can_PBCfg.c****************************\n\n")
	
	#modify Can_Cfg
	print("#####################Step5: process Can_Cfg.h############################")
	log.info("#####################Step5: process Can_Cfg.h###############################")
	
	Modi_Can_Cfg(str_CAN_mode)
	
	print("***********************End process Can_Cfg.h*****************************\n\n")
	log.info("***********************End process Can_Cfg.h****************************\n\n")
	
	#modify CanIf_cfg
	print("#####################Step6: process CanIf_cfg.h############################")
	log.info("#####################Step6: process CanIf_cfg.h###############################")
	
	Modi_CanIf_cfg(str_CAN_mode)
	
	print("***********************End process CanIf_cfg.h*****************************\n\n")
	log.info("***********************End process CanIf_cfg.h****************************\n\n")
	
	
	#modify Com_cfg.c
	print("#####################Step7: process Com_cfg.c############################")
	log.info("#####################Step7: process Com_cfg.c###############################")
	
	Modi_Com_cfg(str_bswtimebase, dic[dbcname])
	
	print("***********************End process Com_cfg.c*****************************\n\n")
	log.info("***********************End process Com_cfg.c****************************\n\n")
	
	
	print("It's OK.")
	sys.stdin.readline()
