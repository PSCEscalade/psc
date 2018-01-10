# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:23:11 2017

@author: pimpim
"""

"""Création des volumes"""

from ode import *

class ClimberModel:
    
    def __init__(self, morphology):
        self.morphology = morphology

    def addToODE(self, simulator, x0, y0, z0):
        word = simulator.getWorld()
        morphology = self.morphology

        self.bodies = {}

        for part in morphology.getParts() :
            self.bodies[part] = Body(world)

        for part in self.bodies :
            self.bodies[part].setMass(morphology.getLength(part))
        
        #on commence par le bas !
        self.bodies['mollet_d'].setPosition(morphology.getLength('largeur')/2, 0, morphology.getLength('mollet')/2 )
        self.bodies['mollet_g'].setPosition(-morphology.getLength('largeur')/2, 0, morphology.getLength('mollet')/2 )
        
        self.bodies['cuisse_d'].setPosition(morphology.getLength('largeur')/2, 0, morphology.getLength('mollet')+morphology.getLength('cuisse')/2 )
        self.bodies['cuisse_g'].setPosition(-morphology.getLength('largeur')/2, 0, morphology.getLength('mollet')+morphology.getLength('cuisse')/2 )
        
        self.bodies['tronc_bassin_bas'].setPosition(0, 0, morphology.getLength('mollet')+morphology.getLength('cuisse')+morphology.getLength('tronc_bassin_bas')/2)
        self.bodies['tronc_bassin_haut'].setPosition(0, 0, morphology.getLength('mollet')+morphology.getLength('cuisse')+morphology.getLength('tronc_bassin_bas')+morphology.getLength('tronc_bassin_baut')/2)
        
        
