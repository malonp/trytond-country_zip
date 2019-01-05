##############################################################################
#
#    GNU Condo: The Free Management Condominium System
#    Copyright (C) 2016- M. Alonso <port02.server@gmail.com>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from trytond.model import ModelSQL, fields
from trytond.model import ValueMixin
from trytond.pool import PoolMeta

from trytond.modules.party.configuration import _ConfigurationValue


__all__ = ['Configuration',
            'ConfigurationCountry',
            ]


party_country = fields.Many2One('country.country', 'Party Country')


class Configuration(metaclass=PoolMeta):
    __name__ = 'party.configuration'

    party_country = fields.MultiValue(party_country)


class ConfigurationCountry(_ConfigurationValue, ModelSQL, ValueMixin):
    'Party Configuration Country'
    __name__ = 'party.configuration.party_country'

    party_country = party_country
    _configuration_value_field = 'party_country'
