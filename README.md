# Anonymous Source Code for Automated Container Runtime Bug Analysis

**Replace all the {SourceCodeDir} with the current root code directory for replication**

## Configuration

1. Change the config in config.json for analyzing different projects

2. May require Github token for pulling full commits data (Already saved in Collection/)

3. git submodule update

## Data Processing

1. Run python src/github_issue_full.py

2. Modify config.json and then run python src/filter_comments.py with rules

3. Run python src/read_sample_commits.py to view each comments

For reflect analysis, run python src/reflect_read_commit.py

## Data Statistics

1. Opencontainer/Runc 

All Commits: 6164

End Commit: 25c9e888686773e7e06429133578038a9abc091d

Sorted Commits: 1718

Applied filter words: []

2. Containers/Crun

All Commits: 2577

End Commit: cb1e21b8ae1a64808f3091e9f058158cdf220c02

Sorted Commits: 751

Applied filter words: []

3. Kata-Containers/Kata-Containers

All Commits: 9640

End Commit: e32c023d9618a5e4d8fd09b2e66f21e29a2988a7

Sorted Commits: 3075

Applied filter words: []

4. Google/Gvisor

All Commits: 7238

End Commit: 5b7274a1fc081f038613583e82d17fdb68af6dc3

Sorted Commits: 1366

Applied filter words: []

5. Containers/Youki

All Commits: 2830

End Commit: 17c279b7d774772558caf055ffbc0813044515d1

Sorted Commits: 292

Applied filter words: []

6. Containerd/Containerd

All Commits: 11330

End Commit: 24020812bb1a36b124ec6ac431001d9623e71ecd

Sorted Commits: 2528

Applied filter words: []

6. Cri-O/Cri-O

All Commits: 7377

End Commit: ce3f05f4b4d9fc8e977c80d23e48195b82f9de40

Sorted Commits: 1713

Applied filter words: []

## Utils Files

1. github issue full

All commits from repo on Nov.7 2022

2. github issue with selection

select with keywords 
"fix", "defect", "error", "bug", "issue", "mistake", "incorrect", "fault",  "flaw"

["add", "default"], [], []

## Update Google Doc

The config google_doc_sheet starts from 1

## AST Extraction

Run extact_ast.go for collecting test functions

Then run bug2test.py for comparing the test coverage for bug function implementations