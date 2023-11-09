! _-RunPythonScript (

import rhinoscriptsyntax as rs
#get Curve
curvesID=rs.GetObjects("Select List of Curves",4)
pointB=rs.GetPoint()
for curveID in curvesID: 
    param=rs.CurveClosestPoint(curveID,pointB)
    rs.CurveSeam(curveID,param)

)