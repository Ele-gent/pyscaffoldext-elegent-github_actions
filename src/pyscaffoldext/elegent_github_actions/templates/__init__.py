from functools import partial

from pyscaffold.templates import ScaffoldOpts, get_template

from .. import __version__ as elegent_githubactions_version

template = partial(get_template, relative_to=__name__)


def ci_yaml(opts: ScaffoldOpts) -> str:
    """Adds the ci file

    Args:
        opts: given options, see :obj:`create_project` for an extensive list.

    Returns:
        file content as string
    """
    opts["pkg"] = opts["package"].ljust(19)
    opts["elegent_githubactions_version"] = elegent_githubactions_version
    return template("elegent_github_ci_workflow").safe_substitute(opts)
