# -*- coding: utf-8 -*-
##############################################################################
#
#    weigh_scales module for OpenERP, Allow to manage weigh scales from OpenERP
#    Copyright (C) 2012 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of weigh_scales
#
#    weigh_scales is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    weigh_scales is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from extensions import register

register('openerp.addons.weigh_scales.drivers', 'Adventurer Pro (IP)', 'weigh_scales.drivers.adventurer_pro:adventurer_pro_ip')
register('openerp.addons.weigh_scales.drivers', 'CD11 (IP)', 'weigh_scales.drivers.cd11:cd11_ip')
register('openerp.addons.weigh_scales.drivers', 'CW11 (IP)', 'weigh_scales.drivers.cw11:cw11_ip')
register('openerp.addons.weigh_scales.drivers', 'Cyber (IP)', 'weigh_scales.drivers.cyber:cyber_ip')
register('openerp.addons.weigh_scales.drivers', 'E1105 (IP)', 'weigh_scales.drivers.e1105:e1105_ip')
register('openerp.addons.weigh_scales.drivers', 'Ranger (IP)', 'weigh_scales.drivers.ranger:ranger_ip')
register('openerp.addons.weigh_scales.drivers', 'T31 (IP)', 'weigh_scales.drivers.t31:t31_ip')
register('openerp.addons.weigh_scales.drivers', 'T51 (IP)', 'weigh_scales.drivers.t51:t51_ip')
register('openerp.addons.weigh_scales.drivers', 'T71 (IP)', 'weigh_scales.drivers.t71:t71_ip')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
