"""
Copyright (C) 2020  Centre for Argument Technology (http://arg.tech)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from dgdl.builders import GameBuilder
import json
import ast

class DGDLParser:

    def __init__(self):
        self.parsed = {}

    def parse(self, file=None, input=None):
        self.parsed = GameBuilder().build(**{"file":file, "input":input})
        return self.parsed

    def json(self):
        return json.dumps(ast.literal_eval(str(self.parsed)), indent=2)
