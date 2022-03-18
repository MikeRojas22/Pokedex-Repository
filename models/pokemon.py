#-*-coding:utf-8-*-
from msilib import sequence
from odoo import fields,models

class PokedexPokemon(models.Model):
    _name = 'pokedex.pokemon' #modelo odoo
    _inherit = ['image.mixin']
    _order = 'sequence'
    #Como se llama la tabla pokedex_pokemon
    
    name = fields.Char()
    preevolution_id = fields.Many2one('pokedex.pokemon')
    evolution_ids = fields.One2many('pokedex.pokemon', 'preevolution_id')
    sequence = fields.Integer()
    description = fields.Char()
    height = fields.Float()
    weight = fields.Float()
    type_ids = fields.Many2many('pokedex.pokemon.type')
    move_ids = fields.Many2many('pokedex.pokemon.move')
    color = fields.Integer(string='Color Index', default=0)
    
class PokedexPokemonType(models.Model):
    _name = 'pokedex.pokemon.type'
    _inherit =['image.mixin']
    
    name = fields.Char()
    description = fields.Char()
    color = fields.Integer()
    
class PokedexPokemonMove(models.Model):
    _name = 'pokedex.pokemon.move'
    _inherit =['image.mixin']

    name = fields.Char()
    descripion = fields.Char()
    type_id= fields.Many2one('pokedex.pokemon.type')
    power = fields.Char()
    