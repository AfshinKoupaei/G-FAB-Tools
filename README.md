# G-FAB-Tools
Rhino/Grasshopper helpful for digital manufacturing and fabrication processes

The toolbar contains two tools right now : 
<ol>
  <li>MultipleCurves Change</li>
  <p> Use this icon to change the start point of multiple curves. First, run the command, then select target curves, one by one or using any selection method. Right-click/Enter to proceed and then click on any point on the screen as an attractor point for a change of start points.</p>
  <p>Embeded code of the toolbar icon is : </p>
  <p></p><code>! _-RunPythonScript (
import rhinoscriptsyntax as rs
#get Curve
curvesID=rs.GetObjects("Select List of Curves",4)
pointB=rs.GetPoint()
for curveID in curvesID: 
    param=rs.CurveClosestPoint(curveID,pointB)
    rs.CurveSeam(curveID,param))</code></p>
  
  <li>SingleCurve Change</li>
    <p> Use this icon to change the start point of a single curve. First, run the command, then select the target curve.Right-click/Enter to proceed and then click on any point on the screen as an attractor point for a change of start points.</p>
  <p>Embeded code of the toolbar icon is : </p>
  <p></p><code>! _-RunPythonScript (
import rhinoscriptsyntax as rs
#get Curve
curveID=rs.GetObject("Select Curve",4)
sp=rs.CurveStartPoint(curveID)
pointB=rs.GetPoint("Select a point closest to your start point")
param=rs.CurveClosestPoint(curveID,pointB)
rs.CurveSeam(curveID,param))</code></p>
</ol>
<p> Watch the following video on my Youtube channel for more information and if you have problems installing or employing the toolbar.</p>
[G-FABTOOLS](https://www.youtube.com/AfshinKoupaei)https://www.youtube.com/AfshinKoupaei
