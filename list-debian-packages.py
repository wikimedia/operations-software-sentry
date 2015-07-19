#!/usr/bin/env python

debug = False # or True

import apt
import operator
from distutils.version import LooseVersion
from pip.req import InstallRequirement

from requirements_list import install_requires, postgres_requires
from requirements_map import package_map

ops_map = {
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '=': operator.eq,
    '==': operator.eq,
}
cache = apt.Cache()
in_debian = []
failures = []

for line in install_requires + postgres_requires:
    req = InstallRequirement.from_line(line)
    if req.req.extras:
        failures.append('%s - has extras' % req)
        continue
    if not req.name in package_map:
        failures.append('%s - no debian package' % req)
        continue
    pkg = cache[package_map[req.name]]
    debian_version = LooseVersion(pkg.versions[0].version)
    specs_match = True
    for spec in req.req.specs:
        spec_version = LooseVersion(spec[1])
        if not ops_map[spec[0]](debian_version, spec_version):
            specs_match = False
            failures.append('%s - wrong version %s' % (req, spec[1]))
            break
    if specs_match:
        in_debian.append((req, pkg))

if len(in_debian):
    print 'Packages which can be installed via apt:'
    for item in in_debian:
        if debug:
            print "    require_package('%s') # %s %s" % (item[1].name, item[0], item[1].versions[0].version)
        else:
            print "    require_package('%s')" % item[1].name

if debug:
    print '\nsudo apt-get install %s\n' % ' '.join([i[1].name for i in in_debian])
    print '\n'.join(failures)

