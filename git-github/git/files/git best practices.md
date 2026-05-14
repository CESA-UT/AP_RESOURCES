## Make incremental, small changes

Write the smallest amount of code possible to solve a problem. After identifying a problem or enhancement, the best way to try something new and untested is to divide the update into small batches of value that can easily and rapidly be tested with the end user to prove the validity of the proposed solution and to roll back in case it doesn't work without deprecating the whole new functionality.

Committing code in small batches decreases the likelihood of integration conflicts, because the longer a branch lives separated from the main branch or codeline, the longer other developers are merging changes to the main branch, so integration conflicts will likely arise when merging. Frequent, small commits solves this problem. Incremental changes also help team members easily revert if merge conflicts happen, especially when those changes have been properly documented in the form of descriptive commit messages.

## Keep commits atomic

Related to making small changes, atomic commits are a single unit of work, involving only one task or one fix (e.g. upgrade, bug fix, refactor). Atomic commits make code reviews faster and reverts easier, since they can be applied or reverted without any unintended side effects.

The goal of atomic commits isn't to create hundreds of commits but to group commits by context. For example, if a developer needs to refactor code and add a new feature, she would create two separate commits rather than create a monolithic commit which includes changes with different purposes.

## Develop using branches

Using branches, software development teams can make changes without affecting the main codeline. The running history of changes are tracked in a branch, and when the code is ready, it's merged into the main branch.

Branching organizes development and separates work in progress from stable, tested code in the main branch. Developing in branches ensures that bugs and vulnerabilities don't work their way into the source code and impact users, since testing and finding those in a branch is easier.

