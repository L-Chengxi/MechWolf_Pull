import re
from warnings import warn

from cirpy import Molecule
from terminaltables import SingleTable
from colorama import Fore

from .component import Component

class Vessel(Component):
    """A generic vessel.

    Attributes:
        description (str): The contents of the Vessel.
        resolve (bool, optional): Whether to resolve the names of chemicals surrounded by :literal:`\`` s into their IUPAC names. Defaults to True.
        warnings (bool, optional): Whether to show the resolved chemicals for manual confirmation. Defaults to False.
    """
    def __init__(self, description, resolve=True, warnings=False):

        # handle the resolver logic
        if resolve:
            # find the tagged chemical names
            hits = list(re.findall(r"`(.+?)`", description))

            try: # in case the resolver is down, don't break
                for hit in hits:
                    M = Molecule(hit)
                    description = description.replace(f"`{hit}`", f"{hit} ({M.iupac_name})" if hit.lower() != M.iupac_name.lower() else hit)

                    # show a warning table
                    if warnings:
                        table = SingleTable([
                            ["IUPAC Name", M.iupac_name],
                            ["CAS", M.cas],
                            ["Formula", M.formula]])
                        table.title = "Resolved: " + hit
                        table.inner_heading_row_border = False
                        print(table.table)
            except:
                warn(Fore.YELLOW + "Resolver failed. Continuing without resolving.")
        super().__init__(name=description)
        self.description = description
