source : [here](https://acompiler.com/git-best-practices/)

# git commit best practices

## #1. Atomic Commit

When you do an atomic commit, you're committing only one change. It might be across many files, but it's one single change. 

#### What is atomic commit in Git?

The smallest, most important improvement you can make in your source code. It's large enough to add value but tiny enough to be manageable.

Atomic commit = one commit for one change.

Your commit should be atomic. Each commit should be able to get built. If any commit is breaking the build, it should be reversible.

Here is an example of atomic commit -

![Atomic commit in Git](https://cdn.shortpixel.ai/spai/w_650+q_glossy+ret_img/acompiler.com//wp-content/uploads/2021/01/What-is-atomic-commit-in-git.png "What is Atomic commit in Git")

#### How you can achieve atomic commit 

- By working on one thing at a time
- Keep your changes small

#### Benefits of atomic commits 

- They are easier to read.
- Atomic commit is easier to track.
- And easier to review.

## #2. Commit early, Commit often

It would be best if you commit your changes early and often.  Early commit helps to cut the risk of conflicts between two concurrent changes.

Additionally, having periodic checkpoints means that you can understand how you broke something.

Recently we did a [study of 1 million Git commits](https://acompiler.com//git-commits-analysis/). And we found frequent committers tend to have more positive sentiment scores.

I prefer to commit early, just after my single change. 

You can commit locally "all the time," and you need to push when everything is working. 

If you do small commits, it allows you to use useful tools like git-bisect.

#### Benefits of frequent commits

- Your message will be clear and focused.
- And easy for other developers to understand the code history.


## #3. Do not commit generated files

You should commit your code to your repository. If you're checking in generated files, you're doing something wrong. It's more hassle than it's worth to save it in source control.

Generated files can not help with your repository size. So it would be best if you did not commit anything that can be regenerated.

#### Benefits 

- Your code repository stays clean and organized.
- The size of the storage remains under control.


## #4. Do not commit dependencies

Your Git repository is to manage your source code. It's not to store the dependencies. Also, committing your dependencies will significantly increase the size of the project repository.

Instead of using Git, use a useful build/dependency tool.

There is one out there for (almost) every software stack.

A few examples are:

- Maven for Java
- Npm for node apps
- Bower for JavaScript
- NuGet for .NET

These package managers can manage your project dependencies. Package managers download your project dependencies in each build for you.

#### Benefits of using dependency tool (instead of Git)

- Your repository stays organized.
- You will not be worried about updating your project dependencies (Your dependency tool will do the job).


## #5. Do not commit local configuration files

You should not commit your local config files into the source control for many good reasons. 

Config files might hold secrets or personal preferences. And configuration files might change from environment to environment. 

For example, QA and Production environments have different configuration files.

#### Benefits to hold local config file outside Git Repo

- Different users have different local settings.
- Config files might contain secrets like passwords, API keys. So if you will not check them inside your Git repo, you are protecting them.


## #6. Do not commit broken code

What is the nasty thing you can do as a developer?

Block other developers from working on their tasks. (with broken code)

Are you eager to commit because you need a clean working copy?

Practically, when you are in a hurry?

You should wait...

You should not commit broken code in the repository before leaving the office at the end of the day. 

You can consider [Git’s “Stash” feature](https://acompiler.com//git-commands/) instead of Git commit & push. 

#### Benefits 

- Your code repository will stay stable.
- At any given time, there is no risk of halting the team's productivity because of the broken code.


## #7. Test Your changes before committing

It's always good to test your changes before you commit them to your local repository. 

Testing is essentially an extra layer of security before you commit. It allows you to identify mistakes and bugs quicker before they go to your production server.

As a software developer, you should spend time doing the right thing in the first place. Instead of relying on the QA team to find every bug, a good developer tests his code.

#### Benefits of testing (before you commit)

- Dev testing helps to decrease software faults.
- Save the expense of the project in the long term.


## #8. Write useful commit messages

There are two most important parts of a commit message.

- The commit message should be straightforward.
- And it should be meaningful.

Creating useful commit messages is one of the best things you can do every day.

The right commit message helps other developers in many ways. They can understand the code better even without looking at it.  

In the commit message, you can try to explain why and what. Usually, you can use the first line to summarize (up to 72 characters) of your change.

#### Benefits of a useful commit messages

- Good commit messages act as documentation for other developers.
- Useful commit Messages help maintain the project in the long run.

read [[commit standards]] to know how to write good commit messages

## #9. Review your commit (code review)

In general, you as a developer have no permission to commit or push your changes directly in the main branch. Dev team checks the sets of modifications before merging in the main branch. 

The [GitHub pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) model is a simple but successful model. 

Quality always pays less in the long term.

And it will not take more than a few minutes if you review your work before committing.

#### Benefits of code review

- Code review helps keep the company's coding style intact.
- Finding bugs early, when it is cheap to patch them.


## #10. Use reference number with your commit

For writing commit messages, all teams have different expectations. So it isn't easy to achieve one size which fits all the commit messages.

Using a reference number with your commit messages is a good idea.

The reference may be an external bug tracker reference number or your VSTS task number, or any other. 

When you use a reference number with your Git message, it helps in many ways.

#### Benefits

- It adds clarity to why you made some changes.
- It helps others to review your code.


## #11. Refer a commit by hash

Sometimes you need to refer to a Git commit for some reason.

For example, to change an old commit or remove a commit. In those cases, you can use commit SHA for reference.

In Git, a hash is 40 digits log hex-decimal number. Every time a commit is added to a Git repository, a hash string is generated.

And in Git, you should use a hash to identify a commit uniquely.

You can view a commit with a basic [git command](https://acompiler.com//git-commands/).

``$ git show <hash>``

#### Benefits

- Each commit ID is unique, based on the commit message.

## #12. VCS does not substitute for a good backup

Version control is to manage **_many versions_** of your source code. And backup is to copy the _**latest version**_ of your source code to a safe place.

Version control and backups are independent concepts. These both should be used together. Your version control is not a backup system. 

It would be best if you still had backups. One is not a replacement for another.

# git workflow best practices

## #13. Use a workflow

Workflows are the paths for you and your team. A Git Workflow is a guideline for a reliable and efficient way of using Git to conduct work.

Git offers a lot of flexibility, and there is not any specific workflow for everyone.

Workflow heavily depends on the size of your team and the skill of developers. You should pick a style that best suits your project and team.

#### Benefits of using a workflow

- Git Workflows can boost productivity for your team.
- Git Workflow describes one crucial thing - How something goes from being undone to done.


## #14. Enforce standards

In any team, having standards is good. Enforcing standards will improve the code quality and productivity.

For example, using a gitignore file will keep your repository clean. Another example - You can enforce a commit message template. It will help each commit message follow a particular format.

You can enforce the standards by server-side or client-side hooks.

#### Benefits of adopting standards

- It will improve your coding standards.
- Code repository will stay healthy & Stable.

## #15. Integrate with external tools

Many teams use an external system like Jira, an open-source bug tracker. These external tools improve communication. And without any doubt, communication is the key. 

It is beneficial if your customer can raise the bug by using the external tool. And you can use that reference number in your commit message. And finally, update your customer once the issue is fixed.

#### Benefits of integrating external tool

- Easy to track the issues.
- It will increase communication and transparency.


# git pull request best practices

Pull Requests are vital as they help ensure that quality code. Short **pull requests** allow developers to review and quickly merge code into the main branch efficiently.

## #16. Use Pull Request

The use of pull requests based development is good to have. 

The main branch of your project repository becomes a production-ready branch. And the only commits on the main branch come from pull requests.

Also, pull requests help others to review your changes. It improves the quality and helps to make sure only stable code is going into the master branch. 

#### Benefits of Pull Request

- Enough testing and it improves the stability of your codebase.
- Also, pull request help in reducing conflicts.

## #17. For one concern - One Pull Request

It is necessary for a pull request to be atomic. 

It does not mean a pull request is a single commit. It can either be a construct of one or several atomic commits.

When you raise a pull request, make sure it's only and only for one feature. 

#### Benefits of atomic Pull Request

- it's easy to review and much faster to get approved
- And team productivity and quality boost.


## #18. Do not delay in Pull Request

If you delay in attending the pull requests, the code quality gets reduced. There's no way back to the bad code. It is like a virus, it is. It will spread, and the standard of your code will forever be gone.

Pull requests should not be unattended for a long time. Also, this delay will increase the chances of more conflicts. 

So It is important to review the pull request soon for any merge or to deploy. It will fast and smooth the process.


## #19. Complete your work before a Pull Request

Pull requests must be atomic in nature. First stuff first. It's the job of the author to make the code review quick. 

You need to present the code changes in a pleasant way. So do not create a Pull request for your broken code. 

And in case of a large pull request, split by features. Tidy up your work and all commits before a pull request.

## #20. Useful comments with Pull Request

As a Pull Request reviewer, you should try to add valuable comments for the author.

Before even attempting to propose an alteration, you can first understand the code.

This helps to achieve a few important things

- You're learning more about the code.
- You might be able to help the author find a little bug they didn't note.
- You are judging the code itself, not its author.

#### Benefits of useful comments with Pull Request

- It guides the author.
- Fast the Pull Request process.


# git best practices for small teams

## #21. Define code owners

Useful code review is crucial for any successful project. But sometimes it's not clear who should review it.

And this practice depends from team to team.  You can assign owners for different codebases.

GitHub also has this feature.
#### Benefits of defining code owner

- An extra layer of security for your code
- Review Process become more effective

## #22. Use gitignore file

Gitignore is a text file that tells Git which files or directories in a project should be ignore.

You should use a .gitignore file in each repository. 

Why?

It helps to ignore predefined files and directories. It may be config files, user settings, and other unwanted files. 

You can choose a relevant template from Gitignore.io to get started quickly.

#### Benefits of using gitignore file

- This file helps to keep your repository clean.
- Also it ensures files that are not monitored by git remain untracked.

## #23. Use Rebase

As you continue to grow your feature branch, rebase it frequently against the main. 

This means routinely performing the following steps:

```
$ git checkout main  
$ git pull  
$ git checkout your-feature-branch  
$ git rebase main
```

All the commits to your feature branch will appear sequentially in the Git log. Also, this time best to deal with merge conflicts since it only affects your feature branch.

#### Benefits of Rebasing

- A cleaner project history, and it's easier to review.
- Commit history remains stacked up as an exact sequence.

## #24. Keep your codebase healthy

Git is powerful, and it provides some out of the box functionality.

You can use git commands to keep your repository healthy. And you can perform a few maintenance tasks occasionally with git-gc and git-prune.

git-gc: It cleans the unwanted files and optimizes your local repository.

git-prune: It helps to prune all unreachable objects.

#### Benefits of keeping your codebase healthy

- Easy to maintain your project repository by using these internal housekeeping commands.


## #25. Use Diff

You should review every single change before you commit.  

The Diff command takes two inputs and shows differences. Also, it's not necessary for these inputs to only be files. It can be different commits, branches, working trees, commits, and more.

For example, let's say you have already added a few changes to staging. Now you can confirm them before you commit with Git diff like - 

`$ git diff --staged`
#### Benefits of using git diff

- It helps you to understand what precisely the new changes are.
- Also, diff commands help in deciding if it is appropriate to rebase or merge.

## #26. Use Git Stash with a message

You can stash your uncommitted modifications (both staged and unstaged) for later usage. You can use them back from your working copy.

Git stash is excellent for storing changes temporarily.

You should use Git stash with a meaningful message. 

_$ git stash save “Your meaningful stash message”._

#### Benefits of using git stash with a meaningful message

- It helps you to keep track of what’s what easily!

## #27. Tag your Releases

It is also a good practice - when you make a release,

Tags are a distinct feature of Git - meaning you can mark unique release versions of the code. 

A tag lets you keep track of your project's version number. Also, when you are communicating with other team members, refer to the release number.

It acts as an extra piece of documentation that can be extremely helpful.

#### Benefits of tagging releases

- It helps you to compare changes of different releases.
- Easy to rollback a release, update the environment with a specific release, etc.


## #28. Don't mix "refactoring" with a new feature

The worst thing new developers do - refactoring and adding a new feature in the same commit.

It's simply against git best practices. And, It is not suitable for many reasons. 

It will increase the chance of having conflicts that might be harder to resolve.

#### Benefits of NOT mixing "refactoring" with a new feature

- Your code becomes easy to review.
- Team productivity will Increase.


# git branch best practices

## #29. Use Branches

The most important feature of git is its branching model. These branches are more like a new copy of your code's current state.  

It would help if you used branches. Here are few cases

- A new git branch for a new feature.
- Another git branch for bug fixes.
- A new git branch for some LIVE issue, and so on.

#### Benefits of using branches

- The use of branches lets you manage the workflow more quickly and easily.

## #30. Branch naming convention

A branching strategy is, in simple words, a collection of rules. You can practice these rules and naming conventions to build a new branch, flow, etc.

Three are more in the next chapter about the git branch naming conventions.

#### Benefits of using branch naming convention

- It helps to keep your repository organized.
- The right branch name helps in avoiding confusion.

## #31. Delete stale branches

Without the possibility of losing any code, you can securely remove a git branch.

And You should remove old git branches that are no longer in use.

For example - you completed a feature and merged your branch with master.  Now you do not need your feature branch.

If you do not delete old branches, you may end up with many stale-branches, and it's become hard to manage.

#### Benefits of removing unwanted branches

- Help in keeping your repository clean.
- Avoid confusion with having few branches in use.

## #32. Keep your branches up to date

You should make sure you are correctly using pull and push.

And you should consistently merge your base branch into your current branch as you work.

It's beneficial if it's a long-outstanding branch.

This practice will help you to save your time and energy.

Otherwise, you will spend your time resolving an unnecessary amount of merge conflicts.

#### Benefits of keeping your branches up to date

- It will help you save time and resources.

## #33. Do not rewrite history

In practice, each commit is unique. If you rewrite history, new commits will be there in the project history.

You can think of it as cutting off a tree's branches and then forming new ones instantly. They might even look the same, but they do not.

You should not rewrite history on any shared branch.

- If you are rewriting history, you are making life harder for everyone else working on that branch.
- The biggest problem with rewriting a branch's history has to do with git merge.

## #34. Protect your main branch 

What is the most crucial branch in your Git repository?

main (before known as the master)

By protecting the main branch, nobody should make a direct check in to the main branch. Or can rewrite the history of the main branch. 

Also, only merge requests should be allowed in master after a code review process. So no git push straight to the main branch. 

#### Benefits of protecting your main branch

- It's your production code, ready for the world to roll out.
- The main branch always stays in stable mode.


## #35. Test before you push

Test your code changes before you push is a good practice. In fact, it's part of my favorites - AFTER technique. (which I will share in the Bonus section)

Instead of depending on QA to find any bug or issues, a successful developer checks their code.

If you did not test your code and property, it has a knockout effect.  You might block the entire development team. (and it might happen)

So it's always worth spending a few minutes to test your code before you push.


# git branch naming convection


## #36. Use group word in the branch name

The idea is to use group words, so any developer can tell the branch's purpose by looking at it.

for example - 

- wip - the prefix wip indicates work in progress.
- exp - experimental branch for dev purpose.
- feature - adding a new feature.

Whatever you like, use those group words to match your workflow.

#### Benefits of group word in the branch name

- These group words add more clarity.
- And it becomes easy to organize your branches.

## #37. Use Separators

You can use a separator in your branch name.

Many developers use slash, and others use hyphens or underscores. Which one to use depends on the needs of both you and your team.

example of branch name with a separator

feature-sso-implemented  
bug_login_page_redirect

My view is that hyphens or underscore make the name easier to interpret.

#### Benefits of using separators

- It makes the branch name easier to read.
- It helps in avoiding confusion.

## #38. Do not use only numbers

As part of the branch naming convention, do not use only numbers.

It's hard to know from these numbers what this branch is about.  If you have to associate an external bug tracker reference, then use more details.

Here are few examples 

cr-12312  
bug-0912  
feature/tfs/12013

## #39. Avoid too long names

When you are viewing the list of all branches, long branch names can be beneficial. 

But as the branch names can take up much of the single line. It can be problematic when looking at decorated one-line logs.

Also, short and meaningful git branch names are more helpful. For example, if you have to merge two branches.

**With long branch name:**

merge branch 'bug_fix_billing-module-is crashing-when-string-date-has-some-invalid-character-in-it'

**With short and meaningful branch name:**

merge branch 'bug_billing_module.'  
or  
merge branch 'bug_ID_17213'

## #40. Avoid the use of all naming conventions

The best practice is not to mix and match all the Git branch naming conventions. It just causes uncertainty and complicates the general process.

A team should decide and adhere to the naming conventions that should be used once on the job. The most important thing is continuity.

