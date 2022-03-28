#-*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError

class PokemonEvolveWizard(models.TransientModel):
    _name = "pokemon.evolve.wizard"

    pokemon_id = fields.Many2one("pokedex.pokemon")
    trainer_id = fields.Many2one("res.partner")
    sure = fields.Boolean()
    evolve_to_id = fields.Many2one("pokedex.pokemon", compute="_get_evolution")

    @api.depends("pokemon_id")
    def _get_evolution(self):
        for ev_wizd in self:
            if len(ev_wizd.pokemon_id.evolution_ids):
                ev_wizd.update({'evolve_to_id': ev_wizd.pokemon_id.evolution_ids[0].id})
            else:
                ev_wizd.update({'evolve_to_id': False})

    def evolve_confirm(self):
        for ev_wizd in self:
            if not ev_wizd.sure:
                raise UserError("You can not confirm to evolve: $s"%(ev_wizd.pokemon_id.name))
            if ev_wizd.pokemon_id not in ev_wizd.trainer_id.pokemon_ids:
                raise UserError("You dont have the next pokemon: %s"%(ev_wizd.pokemon_id.name))
            if not ev_wizd.evolve_to_id:
                raise UserError("%s not have an evolution available."%(ev_wizd.pokemon_id.name))
            ev_wizd.trainer_id.write({'pokemon_ids': [(4, ev_wizd.evolve_to_id.id)]})
            ev_wizd.trainer_id.write({'pokemon_ids': [(3, ev_wizd.pokemon_id.id)]})