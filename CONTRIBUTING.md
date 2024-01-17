# Contributing Guide

> *Contributing to the GitPy project is fairly easy. This document shows you how to get started.*

## Prerequisites

First of all, thank you for taking the time to contribute for this project! :heart:

Second of all, you must read, agree and follow the [Code of Conduct](CODE_OF_CONDUCT.md) in order to contribute to this project.

And third, here are a few guidelines that you must follow in order to ease the process of getting your contribution merged. See the [Coding Guidelines](CODING_GUIDELINES.md) for more information.

### GPG Signature

We use [GPG][gpg_url] to sign our commits. If you don't know how to sign your commits, please read the [GPG Signing][gpg_signing_url] page. It's important to sign your commits because it's a way to verify that the commit is from you and not from someone else.

## Submitting changes

1. [Fork the repo][fork_repo_url]

2. Check out a new branch based on `develop` and name it to what you intend to do:
    - Example:

      ```shell
      git branch -b  <type_of_you_modification>/<your_feature/fix> develop
      ```

      The `<type_of_you_modification>` must be one of the following:

        - feature
        - hotfix

      > [!NOTE]  
      > See the [Coding Guidelines](CODING_GUIDELINES.md#branch-naming) for more information.

      If you get an error, you may need to fetch it first by using:

      ```shell
      git remote update && git fetch --all
      ```

      > [!IMPORTANT]  
      > Use one branch per feature / hotfix

3. Commit your changes
    > [!IMPORTANT]  
    > Please make sure your commits follow the [Conventional Commits][conventional_commits] conventions. See the [Coding Guidelines](CODING_GUIDELINES.md#commit-message) for more information.
    >
    > You also MUST sign your commits with your GPG key created in the [Prerequisites](#gpg-signature) section.

    - Commit to the forked repository
      - Examples:

        ```shell
        git commit -m 'feat(<scope>): Add a new feature'
        ```

        ```shell
        git commit -m 'fix(<scope>): Fix a bug'
        ```

4. Push your branch into the `develop` branch
    - Example:

      ```shell
      git push origin <type_of_you_modification>/<your_feature/fix>
      ```

5. Make a pull request from the develop branch on you forked repository **to the `develop` branch on the main repository**.

\
If you have followed these instructions, your PR will land pretty safely in the GitPy development branch! :smile:

[conventional_commits]: https://www.conventionalcommits.org/en/v1.0.0/
[fork_repo_url]: https://github.com/dedroot/gitpy/fork
[gpg_signing_url]: https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification
[gpg_url]: https://gnupg.org/
