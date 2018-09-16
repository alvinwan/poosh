# Poosh

Automatically find and update remote copies of your local Git repository.

This small utility allows you sync a local Git repository with a remote Git
repository at an unspecified location on arbitrary server(s), *without git
commits*. This allows you to, say, verify code works on a remote server with
heavyweight GPUs, before committing.

by [Alvin Wan](http://alvinwan.com)

# Usage

To automatically navigate to your server's copy of your local git repository, use

```
poosh go <server>
```

![poosh-demo-go-2](https://user-images.githubusercontent.com/2068077/45601808-e7007f00-b9c7-11e8-85bc-037916fbfe0e.gif)

To push all untracked and modified files to multiple remote servers' copies of your local repository

```
poosh to <server> <server> <server> ...
```

![poosh-demo-to](https://user-images.githubusercontent.com/2068077/45601812-e8ca4280-b9c7-11e8-8b98-c8c13f20cf07.gif)

Note that `poosh`, without the `to <server> <server> <server>...` arguments, will default to the servers listed in its default list of servers.

Use `poosh set`, `poosh list`, `poosh unset`, and `poosh config` to manage your default list of servers. Each server features a working directory setting: this is the root of your working directory on the server. Poosh will search this working directory for a copy of your local git repository.

```
usage: poosh [-h] [--path PATH] {go,to,set,unset,list,config} ...

This small utility allows you sync a local Git repository with a remote Git
repository at an unspecified location on arbitrary server(s), *without git
commits. This allows you to, say, verify code works on a remote server with
heavyweight GPUs, before committing.

positional arguments:
  {go,to,set,unset,list,config}
                        Sub-command help
    go                  Go to location on server
    to                  Push all files to specified server(s)
    set                 Add default server or set value for existing server
    unset               Remove server
    list                List default servers
    config              Edit configuration file

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path to search in
```

# How it Works

Every `.git` directory contains `objects` representing the commit tree for your Git repository. Each object is initially stored *loosely* as files in `.git/objects/<2-character prefix>/<rest of hash>`. Periodically, git then packages sets of objects into `.git/objects/pack/<hash>.{idx,pak}`. Poosh depends on the existence of one or the other in every copy of the Git repository: Poosh first extracts the hash corresponding to the Git repository's first commit, then searches the listed server(s) for a filename with the specified hash. In that regard, Poosh could technically synchronize directories identified by a unique name.
