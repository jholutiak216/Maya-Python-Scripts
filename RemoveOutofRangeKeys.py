from maya import cmds

def removeoutofrangekeys():
    currenttime = cmds.currentTime(query=True)
    starttime = cmds.playbackOptions(minTime=True, query=True)
    endtime = cmds.playbackOptions(maxTime=True, query=True)
    print(currenttime, starttime, endtime)
    
    currenttime = cmds.currentTime(starttime, edit=True)
    cmds.setKeyframe()
    
    currenttime = cmds.currentTime(endtime, edit=True)
    cmds.setKeyframe()
    
    currenttime = cmds.currentTime(query=True)
    selection = cmds.ls(selection=True)
    print(selection)
    
    for obj in selection:
        print(obj)
        cmds.cutKey(time=(starttime-1, starttime-1000))
        cmds.cutKey(time=(endtime+1, endtime+1000))
        
removeoutofrangekeys()