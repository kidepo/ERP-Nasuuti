# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 13:05:33 2017

@author: SourceQode
"""

import DBconnect
myConnection =DBconnect.getConnection()
sqlString="SELECT VERSION()"
if(myConnection):
 data = DBconnect.fetchData(sqlString)
 print ("Database version : %s " % data.fetchone())
else:
    print("not connected")
#DBconnect.insertData(myConnection,sqlString)
    #######