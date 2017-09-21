# Background / Why we're using GitHub
1. The information contained in this project is text, which would mean that normally the way to distribute contributions to it would be through a wiki format.
1. However, with wikis you need to worry about the quality of the contributions of the people you allow to make changes to the wiki.
    - There may be a way around this but I'm not aware of it.
1. The advantage of using a version-control system like git (which is the technology underlying GitHub) is that all changes can be reviewed before being allowed. This means that we don't need to limit the suggestion of changes to a selected team of people to ensure that the quality of the changes remains high.
1. A potential future problem is that if a lot of people are submitting a lot of potential changes, and the changes are generally good ones, then the review process may become an unnecessary burden.

# Step-by-step instructions
1. Create a GitHub account.
1. Fork this project
    - In other words: make a copy of this project. "Fork" is a git term that basically means "copy". A more-precise definition of a fork is "a remote, server-side copy of a repository, distinct from the original" ([Source](https://www.atlassian.com/blog/git/git-branching-and-forking-in-the-enterprise-why-fork)).
    - How: Click the button in the top-right that says "Fork".
    - See [GitHub Guides - Fork the repository](https://guides.github.com/activities/forking/#fork)
1. (Optional) If you want, clone the project to your computer.
    - In other words: make a copy of your copy on your computer. "Clone" is a git term which basically means "copy". A more-precise definition of a clone is "a local copy of some remote repository" ([Source](https://www.atlassian.com/blog/git/git-branching-and-forking-in-the-enterprise-why-fork)).
    - This is only helpful if you want to use text-editing software that's on your computer instead of GitHub's online text-editor.
1. Make the change you want to make to *your copy* of the project.
    - Online steps:
        1. Click on the file.
        1. Click the pencil icon in the top-right of the file.
        1. You should be redirected to a GitHub page with an in-browser editor showing the document as un-formatted Markdown (.md) text.
        1. Make the change to the file that you want to make.
        1. Scroll to the bottom of the page and click the green 'Commit changes' / 'Commit new file' button.
1. Submit a "pull request" (in other words: click a button asking us to accept your change).
    - See [GitHub Guides - Making a Pull Request](https://guides.github.com/activities/forking/#making-a-pull-request)
1. We will examine your change and either accept it or ask you to change something about it.
