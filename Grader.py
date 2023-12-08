""" barcode: 000000112333333334567899 (#24)
    # 0  = mapCode
    # 1  = gamemodeCode
    # 2  = attackCode   #TODO
    # 3  = version
    # 4  = factionsCode
    # 5  = sizeCode
    # 6  = vehiclesCode
    # 7  = buggedCode
    # 8  = spicyFactorCode  #TODO rename (popularity)
    # 9  = lightingCode
    """
# For now we assume N = 5

from Layer import Gamemode as gm

DEBUG = True

class Grader:
    # context list: First index =  furthest away from input
    @staticmethod
    def gradeLayer(input: int, context: [int]):
        (mapCode, biomeCode, EnviornmentCode, gamemodeCode, attackCode, versionCode, factionsCode, sizeCode, vehiclesCode, buggedCode, spicyFactorCode, lightingCode) = Grader.breakOutMapCode(input)
        (mapCodes, biomeCodes, environmentCodes, gamemodeCodes, attackCodes, versionCodes, factionsCodes, sizeCodes, vehiclesCodes, buggedCodes, spicyFactorCodes, lightingCodes) = Grader.breakOutContextMapCode(context)



        mapSimilarity = Grader.checkMapSimilarity(mapCode, biomeCode, EnviornmentCode, mapCodes, biomeCodes, environmentCodes)
        """gamemodeSimilarity = 
        attackSimilarity = 
        versionSimilarity = 
        factionSimilarity = 
        sizeSimilarity = 
        vehiclesSimilarity = 
        buggedSimilarity = 
        spicyFactorSimilarity = 
        lightingSimilarity = 


        Similarity = """

    @staticmethod
    def breakOutMapCode(layerCode):
        stringLayercode = str(layerCode)
        ls = [*stringLayercode]
        
        mapCode = ls[0:1]
        biomeCode = ls[2:3]
        environmentCode = ls[4:5]
        gamemodeCode = ls[6:7]
        attackCode = ls[8]
        versionCode = ls[9:10]
        factionsCode = ls[11]
        sizeCode = ls[12]
        vehiclesCode = ls[13]
        buggedCode = ls[14]
        spicyFactorCode = ls[15]
        lightingCode = ls[16:17]

        return (mapCode, biomeCode, environmentCode, gamemodeCode, attackCode, versionCode, factionsCode, sizeCode, vehiclesCode, buggedCode, spicyFactorCode, lightingCode)
    
    @staticmethod
    def breakOutContextMapCode(layerCodeList):
        mapCodes = []
        biomeCodes = []
        environmentCodes = []
        gamemodeCodes = []
        attackCodes = []
        versionCodes = []
        factionsCodes = []
        sizeCodes = []
        vehiclesCodes = []
        buggedCodes = []
        spicyFactorCodes = []
        lightingCodes = []
        
        for layer in layerCodeList:
            (mapCode, biomeCode, environmentCode, gamemodeCode, attackCode, versionCode, factionsCode, sizeCode, vehiclesCode, buggedCode, spicyFactorCode, lightingCode) = Grader.breakOutMapCode(layer)
            mapCodes.append(mapCode)
            biomeCodes.append(biomeCode)
            environmentCodes.append(environmentCode)
            gamemodeCodes.append(gamemodeCode)
            attackCodes.append(attackCode)
            versionCodes.append(versionCode)
            factionsCodes.append(factionsCode)
            sizeCodes.append(sizeCode)
            vehiclesCodes.append(vehiclesCode)
            buggedCodes.append(buggedCode)
            spicyFactorCodes.append(spicyFactorCode)
            lightingCodes.append(lightingCode)
            
        return (mapCodes, biomeCodes, environmentCodes, gamemodeCodes, attackCodes, versionCodes, factionsCodes, sizeCodes, vehiclesCodes, buggedCodes, spicyFactorCodes, lightingCodes)
    
    # returns float between 0 and 1
    @staticmethod
    def checkMapSimilarity(mapCode: str, biomeCode: str, enviornmentCode: str, mapCodes: [str], biomeCodes: [str], EnviornmentCodes: [str]) -> float:
        biomeDecayFactor = 0.5 #TODO needs to be parameter setting, Value between 1 and 0
        environmentDecayFactor = 0.2 #TODO needs to be parameter setting, Value between 1 and 0
        mapDecayFactor = 0.2 #TODO needs to be parameter setting, Value between 1 and 0
        mapImportance = 0.1  #TODO needs to be parameter setting, Value between 1 and 0
        biomeImportance = 0.65 #TODO needs to be parameter setting, Value between 1 and 0
        environmentImportance = 0.25 #TODO needs to be parameter setting, Value between 1 and 0
        minMapDistance = 4 #TODO needs to be parameter setting, Value between 0 and N
        # Total importance = 1
        
        rotationDistance = len(mapCodes) - 1
        mapSimilarity = 0
        for map in mapCodes:
            if map == mapCode and rotationDistance < minMapDistance:
                return 1
            elif map == mapCode:
                mapSimilarity += mapDecayFactor**(1 + rotationDistance - minMapDistance)
            rotationDistance -= 1
        if mapSimilarity > 1: mapSimilarity = 1
        
        rotationDistance = len(biomeCodes) - 1
        biomeSimilarity = 0
        for biome in biomeCodes:
            if biomeCode == biome:
                biomeSimilarity += biomeDecayFactor**rotationDistance 
            rotationDistance -= 1
        if biomeSimilarity > 1: biomeSimilarity = 1
        
        rotationDistance = len(biomeCodes) - 1
        environmentSimilarity = 0
        for environment in EnviornmentCodes:
            if enviornmentCode == environment:
                environmentSimilarity += environmentDecayFactor**rotationDistance
            rotationDistance -= 1
        if environmentSimilarity > 1: environmentSimilarity = 1

        totalMapSimilarity = mapImportance* mapSimilarity + biomeImportance * biomeSimilarity + environmentImportance * environmentSimilarity

        return totalMapSimilarity

    # returns float between 0 and 1


    """
    Asuming Small N:

        No 2 asymetric layers right after each other
        Don't have the same team attack on an asymetric layer
    Max 2 asymetrix layers within N
        RAAS: 0 if other game mode in context (0.15)
        AAS: very 'high' decayfactor (0.85)
        TC, Tank, Skirmish: 1 if already in context (0 otherwise) # 0 can be increased if these game modes dominate too much
        Insurgency, Destruction, Seed, TA: always 1
    """
    @staticmethod
    def checkGamemodeSimilarity(gamemodeCode: str, attackCode: str, gamemodeCodes: [str], attackCodes: [str]):
        safeGamemodeScore = 0.15 #TODO needs to be parameter setting, Value between 1 and 0
        spicyGamemodeScore = 0 #TODO needs to be parameter setting, Value between 1 and 0
        unsafeDecayFactor = 0.85 #TODO needs to be parameter setting, Value between 1 and 0
        
        
        asymetricGamemodes = [gm.Invasion, gm.Destruction, gm.Insurgency] #TODO needs to be parameter setting
        spicyGamemodes = [gm.TC, gm.Tank, gm.Skirmish] #TODO needs to be parameter setting
        badGamemodes = [gm.Insurgency, gm.Seed, gm.Destruction, gm.TA] #TODO needs to be parameter setting
        safeGamemodes = [gm.RAAS]
        unsafeGamemodes = [gm.AAS]
        
        if gamemodeCode in badGamemodes:
            return 1
        
        if gamemodeCode in safeGamemodes:
            for gamemode in gamemodeCodes:
                if not gamemode in safeGamemodes:
                    return 0
            
        if gamemodeCode in safeGamemodes:
            return safeGamemodeScore

        if gamemodeCode in spicyGamemodes:
            for gamemode in gamemodeCodes:
                if not gamemode in spicyGamemodes:
                    return spicyGamemodeScore
        if gamemodeCode in spicyGamemodes:
            return 1
            
        if gamemodeCode in unsafeGamemodes:
            rotationDistance = len(gamemodeCodes) - 1
            gamemodeSimularity = 0
            for gamemode in gamemodeCodes:
                if gamemode in unsafeGamemodes:
                    gamemodeSimularity += unsafeDecayFactor**rotationDistance
                rotationDistance -= 1
            if gamemodeSimularity > 1: gamemodeSimularity = 1
            return gamemodeSimularity
        
        if gamemodeCode in asymetricGamemodes:
            previousGamemode = gamemodeCodes[len(gamemodeCodes) -1]
            if previousGamemode in asymetricGamemodes:
                return 1

        if gamemodeCode in asymetricGamemodes:
            rotationDistance = len(gamemodeCodes) - 1
            gamemodeSimularity = 0

            for i in range(len(gamemodeCodes)):
                distance = len(gamemodeCodes) - 1 - i
                gamemode = gamemodeCodes[i]
                if gamemode in asymetricGamemodes and distance == 2:
                    gamemodeSimularity += gamemodeSimularity**rotationDistance
                    attack = attackCodes[i]
                    if attackCode == attack:
                        gamemodeSimularity = 1
                
                if gamemodeSimularity > 1: gamemodeSimularity = 1
            return gamemodeSimularity
    
        if DEBUG:
            print(gamemodeCode, gamemodeCodes)
        
        return 1
