"""Extension that generates configuration for GitHub Actions."""
from argparse import ArgumentParser
from typing import List

from pyscaffold import structure
from pyscaffold.actions import Action, ActionParams, ScaffoldOpts, Structure
from pyscaffold.extensions import Extension, include
from pyscaffold.extensions.pre_commit import PreCommit
from pyscaffold.operations import no_overwrite
from pyscaffold.templates import get_template

TEMPLATE_FILE = "elegent_github_ci_workflow"


class ElegentGithubActions(Extension):
    """Add configuration file for GitHub Actions (includes `--pre-commit`)"""

    def augment_cli(self, parser: ArgumentParser):
        """Augments the command-line interface parser.
        See :obj:`~pyscaffold.extension.Extension.augment_cli`.
        """
        parser.add_argument(
            self.flag, help=self.help_text, nargs=0, action=include(PreCommit(), self)
        )
        return self

    def activate(self, actions: List[Action]) -> List[Action]:
        """Activate extension, see :obj:`~pyscaffold.extension.Extension.activate`."""
        return self.register(actions, add_files, after="define_structure")


def add_files(struct: Structure, opts: ScaffoldOpts) -> ActionParams:
    """Add .github/workflows/ci.yml to the file structure

    Args:
        struct: project representation as (possibly) nested :obj:`dict`.
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        struct, opts: updated project representation and options
    """
    ci_workflow = get_template(
        TEMPLATE_FILE, relative_to=__name__
    ).template  # no substitutions

    files: Structure = {
        ".github": {"workflows": {"ci.yml": (ci_workflow, no_overwrite())}}
    }

    return structure.merge(struct, files), opts
