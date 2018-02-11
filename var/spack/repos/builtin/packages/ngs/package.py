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


class Ngs(Package):
    """NGS is a new, domain-specific API for accessing reads, alignments
       and pileups produced from Next Generation Sequencing."""

    homepage = "https://github.com/ncbi/ngs"
    url      = "https://github.com/ncbi/ngs/archive/1.3.0.tar.gz"

    version('1.3.0', 'fafe59ed156e8a7a4834d73984bc05a2')

    depends_on('jdk')

    # TODO (optional): ngs-python

    def install(self, spec, prefix):
        configure(
            '--prefix=%s' % self.spec.prefix,
            '--build-prefix=%s' % join_path(self.spec.prefix, 'outdir'),
        )
        make('-C', 'ngs-sdk', 'install')
        make('-C', 'ngs-java', 'install')
