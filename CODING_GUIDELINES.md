# GitPy Codebase Structure

> *Theses are the guidelines for the GitPy codebase structure. It is important to follow these guidelines in order to have a clean and maintainable codebase.*

## Arborescence

These are the directories that I'm actively using in the development:

| Directory | Description |
| --------: | :---------- |
| [gitpy/](gitpy/) | Contains the argument parsing file and the \_\_main\_\_ file of GitPy. |
| [gitpy/assets](gitpy/assets/) | Contains the assets of the tool. Like the icons, images, etc. |
| [gitpy/commands](gitpy/commands/) | Contains the operations of all CLI commands of the tool. |
| [gitpy/configs](gitpy/configs/) | Contains the configuration files of the tool. The main language of the configuration files is Python3 but it can be Yaml too. |
| [gitpy/core](gitpy/core/) | Contains the core files of the tool. Like the CLI arguments. |
| [gitpy/hashes](gitpy/hashes/) | Contains a Yaml file that contain all hashes of all files, except: <br /><br />Folders:<ul><li>`.chglog`</li><li>`.git`</li><li>`.github`</li><li>`.vscode`</li></ul>Files:<ul><li>`.gitattributes`</li><li>`.gitignore`</li><li>`hashes_of_all_files.yml`</li><li>`hashes_of_all_files.yml.hash`</li></ul>
| [gitpy/manuals](gitpy/manuals/) | Contains manpage of the tool (page that you can have by running `man gitpy`) |
| [gitpy/tools](gitpy/tools/) | Contains third party utilities to improve GitPy. If you have a new feature that require a specific third party package version, you can add it here. |
| [gitpy/utils](gitpy/utils/) | Contains utilities of the tool (home made, not third party) |

## Source style and other conventions

### Code style

For this project, I'm actually using the [Black][black_url] and the [Isort][isort_url] Python3 formatter together. These two tools are very useful to keep the code clean and readable. If you use [VScode][vscode_url] or [VScode Insider][vscode-insider_url], you can install the Isort and Black extensions with the following commands:

1. First you need to install Black and Isort on you machine. To do that, you can using [pipx][pipx_url]:

    ```shell
    pipx install isort black
    ```

2. If it say that you don't have [pipx][pipx_url], then run the following command:

   - If you are on a Debian based distro:

        ```shell
        sudo apt update && sudo apt install pipx
        ```

    - If you are on a Arch based distro:

        ```shell
        sudo pacman -Syy python-pipx
        ```

3. Next, open your VScode IDE (basic or Insider) and open the Quick Open dialog with <kbd>CTRL</kbd> + <kbd>p</kbd> and paste the following commands one by one:

    ```vscode
    ext install ms-python.isort
    ext install ms-python.black-formatter
    ```

4. Now create a folder called **.vscode** in the project folder. After, create a file called **settings.json** in it. Open it an paste the following:

    ```json
    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.black-formatter",
            "editor.formatOnSave": true,
            "editor.codeActionsOnSave": {
                "source.organizeImports": true
            },
        },
        "isort.args":["--profile", "black"],
    }
    ```

> [!NOTE]  
> You can add more settings in it if you want. For more information, visit the [settings.json][settings.json-doc] section in the official documentation.

That's it! Now you can code with the Black and Isort formatter! Every time you save a python file (.py) in this project, the formatters will automatically format the code for you!

> [!NOTE]  
> The auto formatting will only do the job in the project folder (Workspace). If you want to auto format globally, you need to add the same content in the user settings.json. You can open it by open it the command palette with <kbd>CTRL</kbd> +  <kbd>SHIFT</kbd> + <kbd>p</kbd> and enter **settings.json**. While typing it, you will see the **Preferences: Open Settings (JSON)** option. Select it and only paste the content between the two curly brackets in the file (those in the begin and the end of the file).

### Branch naming

For the branch naming, I'm using the [GitFlow][gitflow_url] workflow branch naming. Here is the branch naming convention:

| Branch name | Description |
| ----------- | ----------- |
| master | The main branch. It's the branch that is MUST BE STABLE. This branch should always contain the latest stable release of the project. |
| develop | The branch where I working and merge feature/hotfix for the next release. It's also the dev version of the program. |
| feature/\<feature name\> | The branch where I develop a new feature. Each feature should have its own branch, and should be merged into the develop branch when it is complete. |
| hotfix/\<fix name\> | The branch where I fix a bug in the master branch. The hotfix branch should be based on the master branch, and should be merged back into both the master and develop branches when the bug is fixed. |
| release/\<release name\> | The branch where I prepare the next release. It should be based on the develop branch, and should only contain bug fixes and minor changes. Once the release is ready, it should be merged into both the master and develop branches. |

### Commit message

For the commit message, I'm using the [Conventional Commits v1.0.0][conventional_commits] convention. Here is the commit message convention:

```txt
<type>[(optional scope)]: <description>

[optional body]

[optional footer(s)]
```

- The **type** is one of the following:

    | Type | Description |
    | ---: | :---------- |
    | `feat` | Used to indicate the addition of a new feature to the code. |
    | `fix` | Used when you're fixing an existing bug or problem. |
    | `chore` | Commits that are intended for maintenance, refactoring or other tasks that do not add new functionality or fix bugs. They are generally | internal changes that have no direct impact on the software's behavior for users. |
    | `docs` | This type of commit concerns changes to documentation. This can include updates to comments, README files, user guides, etc. |
    | `style` | Used when you make style-related changes to the code, such as changes to spacing, indentation, formatting, etc. This should not affect the | behavior of the code. This should not affect code behavior. |
    | `refactor` | This type of commit is used for code modifications that are neither feature additions nor bug fixes, but involve structural or internal | changes to improve the maintainability or readability of the code. |
    | `perf` | Used when making performance improvements to existing code. |
    | `test` | This type of commit concerns additions or modifications related to unit, integration or other types of testing. |
    | `build` | Used for changes related to the build system, dependency configuration, etc. |
    | `ci` | Commits that are intended for changes to scripts or Continuous Integration (CI) configuration. |
    | `revert` | Used to indicate that a commit reverses the effects of one or more previous commits. The commit message must begin with "Revert" followed by the previous commit message. |

- The **optional scope** is a phrase describing a section of the codebase enclosed in parenthesis, e.g., "feat(parser)".

- The **description** is a short summary of the code changes, e.g., "feat(parser): add support for arrays".

- The **optional body** is a longer description of the code changes. It can be several sentences long.

- The **optional footer** is a place to reference GitHub issues or other PRs that this commit closes.

### Versioning

For the versioning, I'm using the same principe of the [Semantic Versioning][semantic_versioning_url] convention but with 4 digits. Here is the versioning convention:

```txt
<MAJOR>..<MINOR>.<PATCH>.<REVISION>
```

In this versioning scheme, the <major> component typically indicates major releases with significant changes, <minor> is used for important feature additions or substantial updates, <patch> signifies bug fixes and minor updates, and <revision> is occasionally employed for minor revisions, security fixes, or minor adjustments.

[black_url]: https://pypi.org/project/black/
[conventional_commits]: https://www.conventionalcommits.org/en/v1.0.0/
[gitflow_url]: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
[isort_url]: https://pypi.org/project/isort/
[semantic_versioning_url]: https://semver.org/
[vscode_url]: https://code.visualstudio.com/
[vscode-insider_url]: https://code.visualstudio.com/insiders/
[pipx_url]: https://pypa.github.io/pipx/
[settings.json-doc]: https://code.visualstudio.com/docs/getstarted/settings#_settingsjson
