# vaultAttachSync
A short Python script created to automate copying attachments from an old obsidian vault to a new vault. The script is built using only standard Python libraries, so no third-party libraries are necessary (is that redundant to say?). 

Currently only works for PNGs, but adding additional attachment cases would not be difficult. Just submit a PR or comment. Reference my [Copying Vault Attachments](ethantomfod.com) blog post for a guide on how to utilize the script and a breakdown of the RegEx employed. 

## Useage:
```
usage: vaultAttachSync [-h] -n NEWPATHARG [--na NEWATTACHPATH] -o OLDPATHARG [--oa OLDATTACHPATH]

Handles copying attachments from your old Obsidian Vault to your new Obsidian Vault

optional arguments:
  -h, --help          show this help message and exit

New (Target) Vault:
  Arguments for Vault Currently Missing Attachments

  -n NEWPATHARG       Absolute Path to New Vault where attachments will be copied to
  --na NEWATTACHPATH  Relative Path to Vault's Attachment Storage (Default=/)

Original (Source) Vault:
  Arguments for Source of Vault Attachments

  -o OLDPATHARG       Absolute Path to Original Vault where attachments will be copied from
  --oa OLDATTACHPATH  Relative Path to Vault's Attachment Storage (Default=/)
```
