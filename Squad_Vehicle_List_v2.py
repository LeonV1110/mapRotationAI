import pandas as pd

def init(path):
    #import CSV
    import_data = pd.read_csv(path)

    #split CSV columns
    layer = pd.DataFrame(import_data, columns=['Layer'])
    faction =pd.DataFrame(import_data, columns=['Faction']).replace(
        ['Australian Defence Force','British Armed Forces','Canadian Armed Forces','United States Army',
         'United States Marine Corps',"People's Liberation Army",'PLA Navy Marine Corps','Russian Ground Forces',
         'Russian Airborne Forces','Middle Eastern Alliance','Turkish Land Forces','Insurgent Forces','Irregular Militia Forces'],
        ['ADF','BAF','CAF','USA','USMC','PLA','PLANMC','RGF','VDV','MEA','TLF','INS','IMF'])
    vehicle = pd.DataFrame(import_data, columns=['Vehicle'])
    count = pd.DataFrame(import_data, columns=['Count'])
    delay = pd.DataFrame(import_data, columns=['Initial Delay Time'])
    return layer, faction, vehicle, count, delay

#Global variables
(LAYER, FACTION, VEHICLE, COUNT, DELAY) = init(r'C:\Users\Thijs\Documents\Python Scripts\squad\squad_vehicle_list.csv')
DATA = pd.read_csv(r'C:\Users\Thijs\Documents\Python Scripts\squad\squad_vehicle_list.csv')
FILTERSTRINGS = ['Jensens', 'TA_', 'Tutorial', 'PacificProvingGrounds_PLANMC-VDV', 'PacificProvingGrounds_USMC-PLA', 'PacificProvingGrounds_USMC-RGF']
VEHICLELIST =  [['Minsk 400'], 
                ['HX60 Logistics', 'MSVS Logistics', 'M939 Logistics', 'CTM131 Logistics', 'KamAZ 5350 Logistics', 'Ural-375D Logistics', 'Armored Ural-375D Logistics', 'Ural-4320 Logistics','BMC-185 Logistics'], 
                ['HX60 Transport', 'MSVS Transport','M939 Transport','KamAZ 5350 Transport', 'Ural-375D Transport', 'Armored Ural-375D Transport', 'Ural-4320 Transport', 'BMC-185 Transport'], 
                ['CTM131 Transport QJZ89','CTM131 Transport QJY88', 'CTM131 QJZ89', 'CTM131 QJY88'], 
                ['LUVW Logistics', 'LUV-A1 Logistics', 'Simir Logi', 'Logistics Pickup Truck', 'Logistics Modern Pickup', 'Armored Logistics Modern Pickup'], 
                ['LUVW Transport', 'LUV-A1 Transport', 'Transport Pickup Truck', 'Transport Modern Pickup', 'Armored Transport Modern Pickup'], 
                ['AAVC-7A1 Logistics', 'ZSD05 Logistics', 'BTR-DG Logistics', 'MT-LB Logistics'], 
                ['BTR-D'], 
                ['RHIB Logistics'],
                ['RHIB Transport'], 
                ['RHIB M2', 'RHIB M240', 'RHIB QJZ89', 'RHIB QJY88', 'RHIB QJZ89', 'RHIB NSV', 'RHIB DShK', 'RHIB PKM', 'RHIB PKP'],
                ['PMV Mag58 x3', 'PMV Mag58', 'LPPV', 'LUVW M2', 'LUVW C6', 'M-ATV M240', 'M-ATV M2', 'MATV M2', 'M1151 M2 Open Doors', 'M1151 M2', 'CSK131 QJZ89', 'CSK131 QJY88', 'Tigr-M Kord', 'Simir MG3', 'Simir Kord', 'Technical M2 HB', 'Technical DShK', 'Technical DShK Shielded', 'Armored Technical DShK', 'Modern Technical M2 HB', 'Modern Technical DShK', 'Armored Modern Technical M2 HB', 'Armored Modern Technical DShK', 'Shitty Technical DShK', 'Cobra II MG3', 'Cobra II M2'], 
                ['PMV RWS M2', 'LPPV RWS', 'TAPV M2', 'TAPV C6', 'M-ATV CROWS M2', 'M-ATV CROWS M240', 'MATV CROWS M2', 'M1151 CROWS M2', 'CSK131 QJC88 RWS', 'BRDM-2', 'Tigr-M RWS Kord', 'Technical ZU-23-2', 'Modern Technical ZU-23-2', 'Cobra II MG3 RWS', 'Cobra II M2 RWS'], 
                ['M-ATV TOW', 'MATV TOW', 'CSK131 HJ8', 'BRDM-2 Spandrel', 'Simir Kornet', 'Technical SPG-9', 'Technical BMP-1', 'Armored Technical SPG-9', 'Modern Technical SPG-9', 'Armored Modern Technical SPG-9'], 
                ['BRDM-2 S8', 'Technical UB-32', 'Modern Technical UB-32', 'Technical Mortar'], 
                ['BM-21 Grad'], 
                ['Ural-375D ZU-23-2'], 
                ['BTR-ZD', 'MT-LB ZU-23-2', 'BMP-1 ZU-23-2'], 
                ['FV432', 'M113A3 M2', 'M113A3 C6', 'ZSD05', 'BTR-D Kord', 'BTR-D PKM', 'ACV-15 MG3', 'ACV-15 M2'], 
                ['FV432 RWS', 'M113A3 TLAV', 'AAVP-7A1', 'MT-LBM 6MA', 'MT-LB VMK', 'BTR-MDM', 'MT-LBM 6MA S8', 'MT-LB PKT'], 
                ['ZSL10'], 
                ['LAV III M2 RWS', 'LAV III C6 RWS', 'M1126 CROWS M240', 'M1126 CROWS M2', 'BTR-80', 'PARS III Mk19 RWS', 'PARS III MG3 RWS', 'PARS III M2 RWS'], 
                ['Coyote'], 
                ['FV107'], 
                ['ASLAV', 'LAV 6', 'LAV-25', 'ZBL08 HJ73C', 'ZBL08', 'BTR-82A', 'PARS III 25mm'], 
                ['FV510', 'FV510 UA', 'FV520 CTAS40', 'M2A3', 'ZBD04A', 'ZBD05 HJ73C', 'ZBD05', 'BMP-2', 'BMD-4M', 'BMD-1M', 'BMP-1', 'MT-LBM 6MB', 'ACV-15 25mm'], 
                ['ZTD05', 'Sprut-SDM1'], 
                ['M1A1', 'FV4034', 'Leopard 2A6M CAN', 'M1A2', 'ZTZ99A', 'T-72B3', 'T-72S', 'T-62', 'M60T'], 
                ['UH-60M', 'MRH-90', 'SA330', 'CH-178', 'CH-146', 'UH-1Y', 'Z-8G', 'Z-8J', 'Mi-8', 'Mi-17', 'UH-1H']]
                #anything undefined
VEHICLECLASS = ['Motorbike', 
                'Truck_Logistics', 
                'Truck_Transport', 
                'Truck_ArmedTransport', 
                'Jeep_Logistics', 
                'Jeep_Transport', 
                'Tracked_Logistics', 
                'Tracked_Transport', 
                'Boat_Logistics',
                'Boat_Transport', 
                'Boat_Armed',
                'Jeep_Light', 
                'Jeep_Heavy', 
                'Jeep_AntiTank', 
                'Jeep_Artillery', 
                'Truck_Artillery', 
                'Truck_AntiAir', 
                'Tracked_AntiAir', 
                'Jeep_Tracked', 
                'Tracked_APC', 
                'Wheeled_OpenAPC', 
                'Wheeled_APC', 
                'Wheeled_Recon', 
                'Tracked_Recon', 
                'Wheeled_IFV', 
                'Tracked_IFV', 
                'Tracked_MGS', 
                'Tracked_Tank', 
                'Helicopter_Transport']

#########################################
######### Read and parse data ###########
#########################################

#Return True if the layer should be filtered, False otherwise
def filterLayers(layerName): 
    for filter in FILTERSTRINGS:
        if filter in layerName:
            return True
    return False

#Returns a list of index numbers of the layers in the DATA CSV
def getLayerIndex(df):
    filter = df.notna()
    index = filter[filter.Layer].index.to_numpy().tolist()
    return index

#Returns a list of index numbers of the factions in the DATA CSV
def getFactionIndex(df):
    filter = df.notna()
    index = filter[filter.Faction].index.to_numpy().tolist()
    return index

#Creates a dictionary with the 2 factions on a layer
def getLayerDict(layerIndex, faction2Index, endIndex):
    fac1 = getFactionDict(layerIndex, faction2Index)
    fac1Name = FACTION._get_value(layerIndex, 'Faction')
    fac2 = getFactionDict(faction2Index, endIndex)
    fac2Name = FACTION._get_value(faction2Index, 'Faction')
    return {fac1Name: fac1, fac2Name: fac2}

#Creates a dictionary of vehicles and how often those appear within a layer and what their class is
def getFactionDict(startIndex, endIndex):
    res = {}
    for i in range(startIndex, endIndex):
        vicClass = "Unknown"
        key = DATA._get_value(i, 'Vehicle')
        try:
            dataCount = int(DATA._get_value(i, 'Count'))
        except Exception as e:
            print(f"There is a problem on line: {i} in the squad_vehicle_list.csv")
            # print(e)
        #delay = int(DATA._get_value(i, 'Initial Delay Time'))
        for j in range(len(VEHICLELIST)):
            for k in range(len(VEHICLELIST[j])):
                if VEHICLELIST[j][k] == key:
                    vicClass = VEHICLECLASS[j]
        if key in res:
            count  = int(res[key][0]) + dataCount
        else: 
            count = int(dataCount)
        res[key] = count, vicClass
    # print(res)
    return res

#Creates a dictionary of all layers and in it the factions of the layer
def getAllLayerDicts(layerIndexes: [int], factionIndexes: [int]):
    dict = {}

    for i in range(len(layerIndexes)):
        layerIndex = layerIndexes[i]
        faction2Index = factionIndexes[2*i+1]
        if i == len(layerIndexes)-1: 
            endIndex = DATA.shape[0]-1
        else: 
            endIndex = layerIndexes[i+1]-1

        layerDict = getLayerDict(layerIndex, faction2Index, endIndex)
        layerName = DATA._get_value(layerIndex, 'Layer')
        if not filterLayers(layerName):
            dict[layerName] = layerDict
        # print(layerName)
        # print('')
        # print(layerDict)
        # print('')
        # print('')
            
    return dict

#########################################
########### Create new format ###########
#########################################

def getLargestSet(layers):
    count = 0
    # res = 0, "Did not work"
    for layer in layers:
        # print(layer)
        for faction in layers[layer]:
            # print(faction)
            length = len(layers[layer][faction].keys())
            if count < length:
                count = length
                res = length, layer
    return res

#Adding empty spaces within the rows that are not filled by anything
def addEmptySpace(ls, tableHeight):
    return ls + (tableHeight+1 - len(ls))*['']

#Creates a DataFrame for each layer with the corresponding info in it
def createLayer(layerName: str, layer, tableHeight = 16):
    # print(layerName)
    # print(layer)
    # print('')
    # print(list(layer.keys()))
    # print('')
    # print('')
    fac1Name = list(layer.keys())[0]
    fac2Name = list(layer.keys())[1]
    
    nameCol = pd.Series(addEmptySpace([layerName], tableHeight))
    fac1Col = pd.Series([fac1Name])
    fac2Col = pd.Series([fac2Name])

    fac1VicCol, fac1CountCol, fac1ClassCol = createLayerInfoCol(layer[fac1Name])
    fac2VicCol, fac2CountCol, fac2ClassCol = createLayerInfoCol(layer[fac2Name])

    dict= {
        'Layer' : nameCol,
        'Faction_1_Name': fac1Col,
        'Faction_1_Count' : fac1CountCol,
        'Faction_1_Vehicles' : fac1VicCol,
        'Faction_1_Vehicles_Class' : fac1ClassCol,
        'Faction_2_Name': fac2Col,
        'Faction_2_Count' : fac2CountCol,
        'Faction_2_Vehicles' : fac2VicCol,
        'Faction_2_Vehicles_Class' : fac2ClassCol
    }

    df = pd.DataFrame(dict)
    #converting to DF converts count col from int to float, fixed with the 2 lines below
    df['Faction_1_Count'] = df['Faction_1_Count'].astype('Int64')
    df['Faction_2_Count'] = df['Faction_2_Count'].astype('Int64')
    
    return df

def createLayerInfoCol(faction):
    vics = []
    counts = []
    vicClass = []
    for i in range(len(VEHICLECLASS)):
        for vic in faction.keys():
            if faction[vic][1] == VEHICLECLASS[i]:
                vics.append(vic)
                counts.append(faction[vic][0])
                vicClass.append(faction[vic][1])
    return pd.Series(vics), pd.Series(counts), pd.Series(vicClass)

def createAllLayers(layers, tableHeight):
    ls = []
    
    for layerName in layers.keys():

        try:
            layerFrame = createLayer(layerName, layers[layerName], tableHeight)
            ls.append(layerFrame)
        except IndexError as err:
            print(err)
    df = pd.concat(ls)
    return df

################################
########### Run code ###########
################################


def run():
    layerIndexes = getLayerIndex(LAYER)
    factionIndexes = getFactionIndex(FACTION)
    layers = getAllLayerDicts(layerIndexes, factionIndexes)
    tableHeight, layerName = getLargestSet(layers)
    print('')
    print("Layer with the largest unique vehicle set for a faction:",layerName)
    print("The required table height for this =", tableHeight+1)
    print('')
    df = createAllLayers(layers, tableHeight)
    return df

df = run()
df.to_csv('Result.csv')