# G-FAB-Tools
Rhino/Grasshopper helpful for digital manufacturing and fabrication processes

The toolbar contains two tools right now : 
<ol>
  <li>MultipleCurves Change</li>
  <p> Use this icon to change the start point of multiple curves. First, run the command, then select target curves, one by one or using any selection method. RightClick/Enter to proceed and then click on any point on the screen as an attractor point for a change of start points.</p>
  <p>Embeded code of the toolbar icon is : </p>
  <code>
    ! _-RunPythonScript (

import rhinoscriptsyntax as rs
#get Curve
curvesID=rs.GetObjects("Select List of Curves",4)
pointB=rs.GetPoint()
for curveID in curvesID: 
    param=rs.CurveClosestPoint(curveID,pointB)
    rs.CurveSeam(curveID,param)

)
  </code>
  <li>SingleCurve Change</li>
</ol>
