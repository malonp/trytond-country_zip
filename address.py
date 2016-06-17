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


from trytond.pool import Pool, PoolMeta
from trytond.pyson import Eval, If, Bool


__all__ = ['Address']


class Address:
    __metaclass__ = PoolMeta
    __name__ = 'party.address'

    @classmethod
    def __setup__(cls):
        super(Address, cls).__setup__()
        cls.subdivision.domain.append(If(Bool(Eval('zip')), [('zips.zip', '=', Eval('zip'))],[]))

    @staticmethod
    def default_country():
        Configuration = Pool().get('party.configuration')
        config = Configuration(1)
        if config.default_country:
            return config.default_country.id
