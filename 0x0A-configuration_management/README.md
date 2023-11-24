# 0x0A. Configuration Management

## DevOps, SysAdmin, Scripting, CI/CD
*By: Sylvain Kalache*  
*Weight: 1*  
*Project started: Nov 24, 2023, 3:00 AM*  
*Project deadline: Nov 25, 2023, 3:00 AM*  
*Checker released: Nov 24, 2023, 9:00 AM*  
*Auto review launch at the deadline*

## Background Context

When I was working for SlideShare, I developed an auto-remediation tool called Skynet that monitored, scaled, and fixed Cloud infrastructure. I utilized a parallel job-execution system called MCollective, allowing me to execute commands on one or multiple servers simultaneously, applying actions based on filters such as server hostname or other metadata.

A critical bug in my code sent `nil` to the filter method, resulting in two pieces of bad news:

1. MCollective interpreted `nil` as 'all servers.'
2. The action sent was to terminate the selected servers.

This mistake led to the shutdown of 75% of SlideShare's document conversion infrastructure, resulting in users being unable to convert their PDFs, PowerPoints, and videos. Pretty bad!

Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1 hour, which was impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)...

*Obviously, writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.*



## Requirements
### General
- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension `.pp`.

### Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

**Install puppet**
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.

Puppet 5 Docs

### Install puppet-lint

```bash
$ gem install puppet-lint
```
