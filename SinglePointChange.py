! _-RunPythonScript (

import rhinoscriptsyntax as rs
#get Curve
curveID=rs.GetObject("Select Curve",4)
sp=rs.CurveStartPoint(curveID)
pointB=rs.GetPoint("Select a point closest to your start point")
param=rs.CurveClosestPoint(curveID,pointB)
rs.CurveSeam(curveID,param)
)