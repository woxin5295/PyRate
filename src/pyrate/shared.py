'''
Created on 12/09/2012

@author: bpd900
'''


ROI_PAC_HEADER_FILE_EXT = "rsc"



class IfgConstants(object):
	"""Collection of constants for items in ROI_PAC header files (*.rsc)"""
	WIDTH = "WIDTH"
	FILE_LENGTH = "FILE_LENGTH"
	XMIN = "XMIN"
	XMAX = "XMAX"
	YMIN = "YMIN"
	YMAX = "YMAX"
	RLOOKS = "RLOOKS"
	ALOOKS = "ALOOKS"
	X_FIRST = "X_FIRST"
	X_STEP = "X_STEP"
	X_UNIT = "X_UNIT"
	Y_FIRST = "Y_FIRST"
	Y_STEP = "Y_STEP"
	Y_UNIT = "Y_UNIT"
	TIME_SPAN_YEAR = "TIME_SPAN_YEAR"
	COR_THRESHOLD = "COR_THRESHOLD"
	ORBIT_NUMBER = "ORBIT_NUMBER"
	VELOCITY = "VELOCITY"
	HEIGHT = "HEIGHT"
	EARTH_RADIUS = "EARTH_RADIUS"
	WAVELENGTH = "WAVELENGTH"
	DATE = "DATE"
	DATE12 = "DATE12"
	HEADING_DEG = "HEADING_DEG"
	RGE_REF1 = "RGE_REF1"
	LOOK_REF1 = "LOOK_REF1"
	LAT_REF1 = "LAT_REF1"
	LON_REF1 = "LON_REF1"
	RGE_REF2 = "RGE_REF2"
	LOOK_REF2 = "LOOK_REF2"
	LAT_REF2 = "LAT_REF2"
	LON_REF2 = "LON_REF2"
	RGE_REF3 = "RGE_REF3"
	LOOK_REF3 = "LOOK_REF3"
	LAT_REF3 = "LAT_REF3"
	LON_REF3 = "LON_REF3"
	RGE_REF4 = "RGE_REF4"
	LOOK_REF4 = "LOOK_REF4"
	LAT_REF4 = "LAT_REF4"
	LON_REF4 = "LON_REF4"
	
	# store type for each of the header items
	INT_HEADERS = [WIDTH, FILE_LENGTH, XMIN, XMAX, YMIN, YMAX ]
	STR_HEADERS = [X_UNIT, Y_UNIT, ORBIT_NUMBER, DATE, DATE12 ]
