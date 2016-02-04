from paraview.simple import *
coun = range(0,51)
names = [0]*51
rad = [0]*51

for i in coun:
    rad[i] = 0.05 + 0.01*i
    if i < 10:
        names[i] = "cone0"+str(i)
    else:
        names[i] = "cone"+str(i)
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    # create a new 'Cone'
    cone1 = Cone()
    # Properties modified on cone1
    cone1.Radius = rad[i]
    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # show data in view
    cone1Display = Show(cone1, renderView1)
    # trace defaults for the display properties.
    cone1Display.ColorArrayName = [None, '']
    cone1Display.GlyphType = 'Arrow'
    cone1Display.SetScaleArray = [None, '']
    cone1Display.ScaleTransferFunction = 'PiecewiseFunction'
    cone1Display.OpacityArray = [None, '']
    cone1Display.OpacityTransferFunction = 'PiecewiseFunction'
    cone1Display.SelectInputVectors = [None, '']
    cone1Display.WriteLog = ''
    # reset view to fit data
    renderView1.ResetCamera()
    # current camera placement for renderView1
    renderView1.CameraPosition = [0.0, 0.0, 5.464101578361145]
    renderView1.CameraParallelScale = 1.414213552854608
    # get layout
    viewLayout1 = GetLayout()
    # save screenshot
    SaveScreenshot('C:/Users/Meghan/Code/Paraview/cones/{0}.png'.format(names[i]), layout=viewLayout1, magnification=1, quality=100)
    # destroy renderView1
    Delete(renderView1)
    del renderView1
    # destroy cone1
    Delete(cone1)
    del cone1

#notes
#there's a True showing up for some reason
#not animated yet