
we use commit types which are in [[Commit standarsds]] note.

Commit comments should start with “#”. If you don’t use the “#” symbol in your commit messages, automated systems like “danger bot” can perceive these messages as incorrect or inappropriate rather than code changes. Therefore, it is important to use the “#” symbol correctly when writing your commit messages.

The Scope should indicate the specific feature or area of the code changes. If it’s not a specific feature, it should provide a broader context, such as ui, data, utils, ai, gameplay, shader. The Scope name should be written in camelCase format and ideally be a single word.

![[Pasted image 20231120162652.png]]

**_Branch Merge_**

When working on a branch and needing to merge the changes from the “develop” branch, conflicts may arise. When resolving this conflict, the commit message should be as follows:

fix(conflict): Resolve conflicts

Merge develop into A branch. Resolve conflicts on GameManager.

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**. The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE> 
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header of the reverted commit. In the body it should say: `This reverts commit <hash>.`, where the hash is the SHA of the commit being reverted.
### Scopes

The `scope` provides additional contextual information.

- Is an **optional** part of the format
- Allowed Scopes depends on the specific project
- Don't use issue identifiers as scopes

### Breaking Changes Indicator

Breaking changes should be indicated by an `!` before the `:` in the subject line e.g. `feat(api)!: remove status endpoint`

- Is an **optional** part of the format

### Description

The `description` contains a concise description of the change.

- Is a **mandatory** part of the format
- Use the imperative, present tense: "change" not "changed" nor "changes"
    - Think of `This commit will...` or `This commit should...`
- Don't capitalize the first letter
- No dot (.) at the end

### Body

The `body` should include the motivation for the change and contrast this with previous behavior.

- Is an **optional** part of the format
- Use the imperative, present tense: "change" not "changed" nor "changes"
- This is the place to mention issue identifiers and their relations

### Footer

The `footer` should contain any information about **Breaking Changes** and is also the place to **reference Issues** that this commit refers to.

- Is an **optional** part of the format
- **optionally** reference an issue by its id.
- **Breaking Changes** should start with the word `BREAKING CHANGES:` followed by space or two newlines. The rest of the commit message is then used for this.



### Examples

```
feat: add email notifications on new direct messages
```

```
feat(shopping cart): add the amazing button
```

```
feat!: remove ticket list endpoint

refers to JIRA-1337

BREAKING CHANGES: ticket enpoints no longer supports list all entites.
```

```
fix(api): handle empty message in request body
```

```
fix(api): fix wrong calculation of request body checksum
```

```
fix: add missing parameter to service call

The error occurred because of <reasons>.
```

```
perf: decrease memory footprint for determine uniqe visitors by using HyperLogLog
```

```
build: update dependencies
```

```
build(release): `bump version to 1.0.0
```

```
refactor: implement fibonacci number calculation as recursion
```

```
style: remove empty line
```

## Specification

1. Commits MUST be prefixed with a type, which consists of a noun, `feat`, `fix`, etc., followed by a colon and a space.
2. The type `feat` MUST be used when a commit adds a new feature to your application or library.
3. The type `fix` MUST be used when a commit represents a bug fix for your application.
4. An optional scope MAY be provided after a type. A scope is a phrase describing a section of the codebase enclosed in parenthesis, e.g., `fix(parser):`
5. A description MUST immediately follow the type/scope prefix. The description is a short description of the code changes, e.g., _fix: array parsing issue when multiple spaces were contained in string._
6. A longer commit body MAY be provided after the short description, providing additional contextual information about the code changes. The body MUST begin one blank line after the description.
7. A footer MAY be provided one blank line after the body (or after the description if body is missing). The footer SHOULD contain additional issue references about the code changes (such as the issues it fixes, e.g.,`Fixes #13`).
8. Breaking changes MUST be indicated at the very beginning of the footer or body section of a commit. A breaking change MUST consist of the uppercase text `BREAKING CHANGE`, followed by a colon and a space.
9. A description MUST be provided after the `BREAKING CHANGE:` , describing what has changed about the API, e.g., _BREAKING CHANGE: environment variables now take precedence over config files._
10. The footer MUST only contain `BREAKING CHANGE`, external links, issue references, and other meta-information.
11. Types other than `feat` and `fix` MAY be used in your commit messages.