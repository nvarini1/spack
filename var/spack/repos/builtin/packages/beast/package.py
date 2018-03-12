##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Beast(Package):
    """BEAST 2 is a cross-platform program for Bayesian phylogenetic analysis
       of molecular sequences."""

    homepage = "https://www.beast2.org"
    url      = "https://github.com/CompEvol/beast2/releases/download/v2.4.8/BEAST.v2.4.8.Linux.tgz"

    version('2.4.8', '1f829b3cb2cd0e89dd2ff6a6916c632e')

    depends_on('jdk@8:')

    def install(self, spec, prefix):
        collection = ['bin', 'examples', 'images', 'lib', 'templates']
        for folder in collection:
            install_tree(join_path(self.stage.source_path, folder),
                         join_path(self.spec.prefix, folder))
