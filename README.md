# Open Peer Power Release helpers

Some helper scripts to help to make a new release.

This repository needs to have the same parent directory as your checked out Open Peer Power repository.

1. Create a GitHub token with `public_repo` and `read:user` rights and write it to `.token` file in the repository directory.
2. Run `pip3 install -e .`  to install the dependencies.

The package is now installed. Run `opprelease --help` for additional info. Run `opprelease <command> --help` to get information about a particular command.
