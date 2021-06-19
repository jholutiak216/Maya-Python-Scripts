from maya import cmds

def printThis(this):
    print(this)

def setkeyframes(starttime, endtime):
    cmds.currentTime(starttime, edit=True)
    cmds.setKeyframe()
    
    cmds.currentTime(endtime, edit=True)
    cmds.setKeyframe()

def removeoutofrangekeys():
    starttime = cmds.playbackOptions(minTime=True, query=True)
    endtime = cmds.playbackOptions(maxTime=True, query=True)
    
    selection = cmds.ls(selection=True)
    
    for obj in selection:
        keyframes = cmds.selectKey(obj, time=(starttime, endtime))
        printThis(keyframes)
        if keyframes != 0:
            setkeyframes(starttime, endtime)
            keyframes = cmds.selectKey(clear=True)
        cmds.cutKey(time=(starttime-1, starttime-1000), clear=(True))
        cmds.cutKey(time=(endtime+1, endtime+1000), clear=(True))  

removeoutofrangekeys()