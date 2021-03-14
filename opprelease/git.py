import subprocess

from .core import OppReleaseError


def get_opp_version(branch):
    """Get the HA version of a branch."""
    process = subprocess.run(
        "git show {branch}:openpeerpower/const.py".format(branch=branch),
        shell=True,
        cwd="../core",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    if process.returncode != 0:
        text = (
            "Failed getting OPP version of branch - Does open-peer-power repo exist at "
            "../core? - Does branch {} exist?".format(branch)
        )
        raise OppReleaseError(text)

    locals = {}
    exec(process.stdout, {}, locals)
    return locals["__version__"]


def get_log(branch):
    process = subprocess.run(
        "git log origin/master...{branch} "
        "--pretty=format:'- %s (%ae)' --reverse".format(branch=branch),
        shell=True,
        cwd="../core",
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    if process.returncode != 0:
        text = (
            "Failed getting log - Does open-peer-power repo exist at "
            "../core? - Does branch {} exist?".format(branch)
        )
        raise OppReleaseError(text)

    output = process.stdout.decode("utf-8")
    last = None

    for line in output.split("\n"):
        # Filter out duplicate lines (I don't git very well)
        if line == last:
            continue
        last = line
        yield line


def fetch(repo):
    process = subprocess.run("git fetch", shell=True, cwd=repo)

    if process.returncode != 0:
        text = (
            "Updating Open Peer Power repo failed - Does open-peer-power repo exist at "
            "../core?"
        )
        raise OppReleaseError(text)


def cherry_pick(sha, cwd="../core"):
    process = subprocess.run("git cherry-pick {}".format(sha), shell=True, cwd=cwd)

    if process.returncode != 0:
        text = (
            "Cherry picking {} failed - Does open-peer-power repo exist at "
            "../core?".format(sha)
        )
        raise OppReleaseError(text)


def is_dirty(repo):
    """Test if repo is dirty."""
    return (
        subprocess.run(
            "git diff --stat", capture_output=True, shell=True, cwd=repo
        ).stdout
        != b""
    )
