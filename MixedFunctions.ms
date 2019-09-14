-- remove all nodes from any layers
-- create new layers based on top-nodes of selections
-- add selected nodes to newly created layers

fn DeleteEmptyLayers =
(
	_defaultlayer = layerManager.getLayer 0
	_defaultlayer.current = true

    try
    (	
        _total_layers = layerManager.count - 1
        _layercount = #()
        _layercount = for i = 1 to _total_layers collect i
        _revlayers = #()
        for i in _layercount.count to 1 by -1 do append _revlayers _layercount[i]

        for j in _revlayers do
        (
            _getlayer = layerManager.getlayer j
            LayerManager.deleteLayerByName _getlayer.name
        )		
    )
    catch()
)

fn CreateLayersFromSelection = 
(
    if selection.count != 0 do
    (
        for o in selection do
        (
            objName = o.name
            if (objLayer = LayerManager.getLayerFromName objName) == undefined then
            (
                objLayer = Layermanager.newLayerFromName objName
                objLayer.addNode o
            )
            else
            (
                objLayer.addNode o
            )
        )
    )
)

fn CreateLayersFromObjBasename =
    (
        objNamesArr = #()
        filterStr = "."
        for o in geometry do 
        (
            namesArr = filterString o.name filterStr
            if namesArr.count > 1 do appendifunique objNamesArr namesArr[1]
        )
     
        for nameStr in objNamesArr do 
        (
            newLayer = if LayerManager.getLayerFromName nameStr == undefined then
                    LayerManager.newLayerFromName nameStr
                else 
                    LayerManager.getLayerFromName nameStr	
     
            for o in geometry where (matchPattern o.name pattern:(nameStr + "*")) do
            (
                newLayer.addNode o
            )
        )
        objNamesArr = undefined
        free objNamesArr
        gc()
    )
--CreateLayersFromSelection()
--DeleteEmptyLayers()
--CreateLayersFromObjects()
