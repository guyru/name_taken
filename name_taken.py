#!/usr/bin/python
"""
name_taken - Simple script to tell if a project name is already taken.
Copyright (C) 2013  Guy Rutenberg

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
"""

import urllib
import re

class Resolver:
    def resolve(self, project_name):
        """\
        Resolve a project name.
        """
        raise NotImplementedError


class DebianResolver(Resolver):
    name = "Debian"
    def resolve(self, project_name):
        args = urllib.urlencode({'keywords': project_name})
        request = urllib.urlopen('http://packages.debian.org/search?%s' % args)
        matches = re.findall(r"<h3>Package (.*)</h3>", request.read())
        if any(map(lambda x: x == project_name, matches)):
            return True
        return False

class SourceForgeResolver(Resolver):
    name = "SourceForge"
    def resolve(self, project_name):
        name = urllib.quote(project_name)
        request = urllib.urlopen('http://sourceforge.net/projects/%s' % name)
        if request.read().find('Whoops, we can\'t find that page') == -1:
            return True
        return False

        

def main(project_name):
    resolvers = [DebianResolver(),
                 SourceForgeResolver()]
    
    for r in resolvers:
        if r.resolve(project_name):
            print('%s: Name taken :-(' % r.name)
        else:
            print('%s: Name not taken :-)' % r.name)
            

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("project_name")
    args = parser.parse_args()

    main(args.project_name.lower())
