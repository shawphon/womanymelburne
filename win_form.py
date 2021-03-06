'''
Generated by Leslie in shnaghai @leadrive
Time: 2019年4月15日10:53:12

kep o mvi
'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from packages.main import Mainfuction
from packages.for_file.modi_Com_cfg import OutIdandName
from packages.basic.basic_functions import Read_File

import sys 
import os
import csv
import time
import threading
import tkinter as tk

global csvDic
csvDic = {'items':'content'}
name_DBC = ''

#start class BitTime
class BitTime(Toplevel):
	'''BitTime 子窗口'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.ePropSeg = StringVar()
		self.ePSEG1 = StringVar()
		self.ePSEG2 = StringVar()
		self.eSJW = StringVar()
		self.eBRP = StringVar()
		self.CreateWidgets()
		self.flag = 0
		
	def CreateWidgets(self):
		'''为BitTime添加控件'''
		
		self.labPropSeg = tk.Label(self, text='PropSeg')
		self.entryPropSeg = tk.Entry(self, textvariable=self.ePropSeg)
		self.labPSEG1 = tk.Label(self, text='PSEG1')
		self.entryPSEG1 = tk.Entry(self, textvariable=self.ePSEG1)
		self.labPSEG2 = tk.Label(self, text='PSEG2')
		self.entryPSEG2 = tk.Entry(self, textvariable=self.ePSEG2)
		self.labSJW = tk.Label(self, text='SJW')
		self.entrySJW = tk.Entry(self, textvariable=self.eSJW)
		self.labBRP = tk.Label(self, text='BRP')
		self.entryBRP = tk.Entry(self, textvariable=self.eBRP)
		self.btnBitTimeSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)
		
		self.entryPropSeg.insert(10, '5')
		self.entryPSEG1.insert(10, '10')
		self.entryPSEG2.insert(10, '4')	
		self.entrySJW.insert(10, '4')	
		self.entryBRP.insert(10, '4')	
		
		self.labPropSeg.grid(row=0,column=0)
		self.entryPropSeg.grid(row=0,column=1)
		self.labPSEG1.grid(row=1,column=0)
		self.entryPSEG1.grid(row=1,column=1)
		self.labPSEG2.grid(row=2,column=0)
		self.entryPSEG2.grid(row=2,column=1)
		self.labSJW.grid(row=3,column=0)
		self.entrySJW.grid(row=3,column=1)	
		self.labBRP.grid(row=4,column=0)
		self.entryBRP.grid(row=4,column=1)
		self.btnBitTimeSaveExit.grid(row=5, column=1)	
	
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.ePropSeg.get():
			csvDic['PropSeg'] = self.ePropSeg.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='PropSeg不能为空')
		if self.ePSEG1.get():
			csvDic['PSEG1'] = self.ePSEG1.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='PropSeg不能为空')
		if self.ePSEG2.get():
			csvDic['PSEG2'] = self.ePSEG1.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='PSEG2不能为空')
		if self.eSJW.get():
			csvDic['SJW'] = self.eSJW.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='SJW不能为空')
		if self.eBRP.get():
			csvDic['BRP'] = self.eBRP.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='BRP不能为空')
		#print(csvDic)
		if self.flag == 5:
			self.destroy()
#end Class BitTime


#start class Baudrate
class Baudrate(Toplevel):
	'''Baudrate 子窗口'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.flag = 0
		self.eBaudrate = StringVar()
		self.CreateWidgets()
		
	def CreateWidgets(self):
		'''Baudrate添加控件'''
		
		self.labBaudrate = tk.Label(self, text='Baudrate\nbps')
		self.entryBaudrate = tk.Entry(self, textvariable=self.eBaudrate)
		self.btnSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)
		
		self.entryBaudrate.insert(10, '500000')
		
		self.labBaudrate.grid(row=0,column=0)
		self.entryBaudrate.grid(row=0,column=1)
		self.btnSaveExit.grid(row=1, column=1)	
	
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.eBaudrate.get():
			csvDic['baudrate'] = self.eBaudrate.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='Baudrate不能为空')
		#print(csvDic)
		if self.flag==1:
			self.destroy()
# End Class BitTime
 

  
def file_name(file_dir):
	'''获得目录下的的dbc文件名'''
	
	print(os.path.abspath('.'))
	L=[]  
	for root, dirs, files in os.walk(file_dir): 
		for file in files: 
			if os.path.splitext(file)[1] == '.dbc': 
				L.append(file)
	return L

#Start class DBCNmae
class DBCName(Toplevel):
	'''DBCNmae子窗口创建类'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.flag = 0
		self.val = []
		self.val = file_name(os.path.abspath('.'))
		self.eDBCName = StringVar()
		self.CreateWidgets()
		
	def CreateWidgets(self):
		'''为DBCName添加控件'''
		
		self.labDBCName = tk.Label(self, text='DBCName')
		self.cobDBCName = ttk.Combobox(self, values=self.val, textvariable=self.eDBCName)
		self.btnSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)
		
		#设置默认值
		try:
			self.cobDBCName.current(0)
		except:
			pass
		if not self.eDBCName.get():
			tk.messagebox.showwarning(title='Warning', message='请先导入DBC文件，点击确定关闭程序！')
			time.sleep(1)
			exit()
		
		self.labDBCName.grid(row=0,column=0)
		self.cobDBCName.grid(row=0,column=1)
		self.btnSaveExit.grid(row=1, column=1)
		
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.eDBCName.get():
			csvDic['DBCName'] = self.eDBCName.get()
			global name_DBC
			name_DBC = self.eDBCName.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='DBCName不能为空')
		#print(csvDic)
		if self.flag==1:
			self.destroy()
# End class DBCName


#Start Class FrameType
class FrameType(Toplevel):
	'''FrameType子窗口创建类'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.val = IntVar()
		self.flag = 0
		self.CreateWidgets()
		
	def CreateWidgets(self):
		'''为FrameType添加控件'''
		
		frametype = [('STD', 0), ('XTD'), 1]
		
		self.labFrameType = tk.Label(self, text='FrameType:')
		self.radiobtnSTD = tk.Radiobutton(self, text='Standard ID', value=0, variable=self.val)
		self.radiobtnXTD = tk.Radiobutton(self, text='Extended ID', value=1, variable=self.val)
		self.btnSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)
		
		#设置默认值
		self.radiobtnSTD.select()
		
		self.labFrameType.grid(row=0,column=0)
		self.radiobtnSTD.grid(row=1,column=0)
		self.radiobtnXTD.grid(row=2,column=0)
		self.btnSaveExit.grid(row=3, column=1)
		
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.val.get()==0:
			csvDic['FrameType'] = str(self.val.get())
			self.flag += 1
		elif self.val.get()==1:
			csvDic['FrameType'] = str(self.val.get())
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='FrameType选择不能为空')

		#print(csvDic)
		if self.flag==1:
			self.destroy()
#End class FrameType


#start class BSWTimeBase
class BSWTimeBase(Toplevel):
	'''BSWTimeBase子窗口创建类'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.flag = 0
		self.val = ['1', '10']
		self.eBSWTimeBase = StringVar()
		self.CreateWidgets()
		
	def CreateWidgets(self):
		'''为BSWTimeBase窗口添加控件''' 
		
		self.labBSWTimeBase = tk.Label(self, text='BSWTimeBase')
		self.cobBSWTimeBase = ttk.Combobox(self, values=self.val, textvariable=self.eBSWTimeBase)
		self.btnSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)
		
		#设置默认值
		self.cobBSWTimeBase.current(1)
		
		self.labBSWTimeBase.grid(row=0,column=0)
		self.cobBSWTimeBase.grid(row=0,column=1)
		self.btnSaveExit.grid(row=1, column=1)
	
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.eBSWTimeBase.get():
			csvDic['BSWTimeBase'] = self.eBSWTimeBase.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='BSWTimeBase不能为空')
		#print(csvDic)
		if self.flag==1:
			self.destroy()
#end class BSWTimeBase


def OutMsgName():
	'''获得dbc文件中消息名'''
	
	global name_DBC
	msgName = []
	with open(name_DBC) as file_object:
		dbcLines = file_object.readlines()
	idandNameDic = OutIdandName(dbcLines)
	for val in idandNameDic.values():
		msgName.append(val)
	
	return msgName
	
#start class AlaMessage
class AlaMessage(Toplevel):
	'''BSWTimeBase子窗口创建类'''
	
	def __init__(self, master=None):
		'''初始化子窗口'''
		
		tk.Toplevel.__init__(self, master)
		self.eMsgName = StringVar()
		self.eMcuName = StringVar()
		self.flag = 0
		self.val = OutMsgName()
		self.CreateWidgets()
		
	def CreateWidgets(self):
		'''为AlaMessage窗口添加控件'''
		
		self.labMsgName = tk.Label(self, text='Message Name')
		self.cobMsgName = ttk.Combobox(self, values=self.val, textvariable=self.eMsgName)
		self.labMcuName = tk.Label(self, text='MCU Name')
		self.entryMcuName = tk.Entry(self, textvariable=self.eMcuName)
		self.btnSaveExit = tk.Button(self, text='保存/退出', command=self.Answer_btnSaveExit)	
		
		#设置默认值
		self.cobMsgName.current(0)
		
		self.labMsgName.grid(row=0,column=0)
		self.cobMsgName.grid(row=0,column=1)
		self.labMcuName.grid(row=1,column=0)
		self.entryMcuName.grid(row=1,column=1)
		self.btnSaveExit.grid(row=2, column=1)
		
	def Answer_btnSaveExit(self):
		'''回应button btnSaveExit点击事件行为'''
		
		self.flag = 0
		if self.eMsgName.get() and self.eMcuName.get():
			csvDic[self.eMsgName.get()] = self.eMcuName.get()
			self.flag += 1
		else:
			tk.messagebox.showerror(title='Error', message='Message Name和MCU Name均不能为空')
		#print(csvDic)
		if self.flag == 1:
			self.destroy()
#end class AlaMessage	

def create_csv():
	path = "Configuration.csv"    
	with open(path,'w', newline='') as f:
		csv_write = csv.writer(f)
		for key, val in csvDic.items():
			csv_head = [key, val]
			csv_write.writerow(csv_head)

#start MainUI
class MainUI(tk.Frame):
	"""主窗口类"""
	
	def __init__(self, master=None):
		
		tk.Frame.__init__(self, master)
		self.th1 = threading.Thread(target=Mainfuction)
		self.th2 = threading.Thread(target=create_csv)
		self.CreateWidgets()
	
	
	def CreateWidgets(self):
		"""创建相应的控件"""
		
		self.labFrame = tk.LabelFrame(height=100, width=200, text='Select item')
		self.labFrame.pack(side='left', fill='both', expand=True)
		
		self.lb = tk.Listbox(height=500, width=300)
		self.lb.pack()
		
		self.labFrame.btnBitTime = tk.Button(self.labFrame, text='BitTime', padx=50, pady=4, command=self.Answer_btnBitTime)
		self.labFrame.btnBitTime.grid(row=0,column=1)
		
		self.labFrame.btnBaudrate = tk.Button(self.labFrame, text='Baudrate', padx=46, pady=4, command=self.Answer_btnBaudrate)
		self.labFrame.btnBaudrate.grid(row=1,column=1)
		
		self.labFrame.btnDBCNmae = tk.Button(self.labFrame, text='DBCNmae', padx=42, pady=4, command=self.Answer_btnDBCNmae)
		self.labFrame.btnDBCNmae.grid(row=2,column=1)
	
		self.labFrame.btnFrameType = tk.Button(self.labFrame, text='FrameType', padx=40, pady=4, command=self.Answer_btnFrameType)
		self.labFrame.btnFrameType.grid(row=3,column=1)
		
		self.labFrame.btnBSWTimeBase = tk.Button(self.labFrame, text='BSWTimeBase', padx=30, pady=4, command=self.Answer_btnBSWTimeBase)
		self.labFrame.btnBSWTimeBase.grid(row=4,column=1)
		
		self.labFrame.btnAlaMessage = tk.Button(self.labFrame, text='Alarm Message', padx=26, pady=4, command=self.Answer_btnAlaMessage)
		self.labFrame.btnAlaMessage.grid(row=5,column=1)
		
		#创建空白控件
		self.labFrame.lbnuseless1 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless1.grid(row=6,column=1)
		self.labFrame.lbnuseless2 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless2.grid(row=7,column=1)
		
		self.labFrame.btnShowConfig = tk.Button(self.labFrame, text='Show Configuration', padx=14, pady=4, command=self.Answer_btnShowConfig)
		self.labFrame.btnShowConfig.grid(row=8,column=1)
		
		#创建空白控件
		self.labFrame.lbnuseless3 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless3.grid(row=9,column=1)
		self.labFrame.lbnuseless4 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless4.grid(row=10,column=1)
		self.labFrame.lbnuseless5 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless5.grid(row=11,column=1)
		self.labFrame.lbnuseless6 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless6.grid(row=12,column=1)
		self.labFrame.lbnuseless7 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless7.grid(row=13,column=1)
		self.labFrame.lbnuseless8 = tk.Label(self.labFrame, text='   ^    ', padx=54, pady=4)
		self.labFrame.lbnuseless8.grid(row=14,column=1)
		
		self.labFrame.btnGenCSVFile = tk.Button(self.labFrame, text='Generate File\n&Run', padx=33, pady=4, command=self.Answer_btnGenCSVFile)
		self.labFrame.btnGenCSVFile.grid(row=15,column=1)
	
	def Answer_btnBitTime(self):
		'''1回应btnBitTime的行为，创建BitTime子窗口'''
		
		formBitTime = BitTime()
		formBitTime.title('BitTime')
		
	def Answer_btnBaudrate(self):
		'''2回应btnBaudrate的行为，创建Baudrate子窗口'''
		
		formBaudrate = Baudrate()
		formBaudrate.title('Baudrate')
		
	def Answer_btnDBCNmae(self):
		'''3回应btnDBCNmae的行为，创建DBCNmae子窗口'''
		
		formDBCName = DBCName()
		formDBCName.title('DBCName')
		
	def Answer_btnFrameType(self):
		'''4回应btnFrameType的行为，创建FrameType子窗口'''
		
		formFrameType = FrameType()
		formFrameType.title('FrameType')
		
	def Answer_btnBSWTimeBase(self):
		'''5回应btnBSWTimeBase的行为，创建btnBSWTimeBase子窗口'''
		
		formBSWTimeBase = BSWTimeBase()
		formBSWTimeBase.title('BSWTimeBase')
		
	def Answer_btnAlaMessage(self):
		'''6回应btnAlaMessage的行为，创建btnAlaMessage子窗口'''
		
		global name_DBC
		if  name_DBC == '':
			tk.messagebox.showwarning(title='Warning', message='请先选择DBC文件')
			formDBCName = DBCName()
			formDBCName.title('DBCName')
		else:
			formAlaMessage = AlaMessage()
			formAlaMessage.title('Alarm Message')
		
	def Answer_btnGenCSVFile(self):
		'''7生成csv文件并执行文件处理'''
		
		count = 0
		for key in csvDic.keys():
			count += 1
		
		if count >= 11:
			#生成csv文件
			self.th2.start()		
			self.th1.start()
			self.lb.insert(0, "it's Ok,")
			self.lb.insert(1, "but you still need to check the details of the next process,\n\
			 please turn to 'run_log.log' or the 'console'.")
		else:
			tk.messagebox.showerror(title='Error', message='请对比配置参数，寻找缺失部分并补齐！')
		
	def Answer_btnShowConfig(self):
		'''1回应btnShowConfig的行为，创建BitTime子窗口'''
		
		for key, val in csvDic.items():
			if key=="FrameType":
				if val=='1':
					self.lb.insert(0, key+'  :  Extended Frame, '+val)
				else:
					self.lb.insert(0, key+'  :  Standard Frame, '+val)
			else:
				self.lb.insert(0, key+'  :  '+val)
		self.lb.insert(0, '###################################')
		
#End MainUI
	

if __name__=='__main__':
	
	app = MainUI()
	app.master.title('Gen_Configuration_File')
	app.mainloop()






