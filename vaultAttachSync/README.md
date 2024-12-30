# vaultAttachSync
A short Python script created to automate copying attachments from an old obsidian vault to a new vault. The script is built using only standard Python libraries, so no third-party libraries are necessary (is that redundant to say?). 

Reference my [Syncing Vault Attachments](https://ethantomford.com/Sync-Obsidian-Attachments-When-Copying-Vault-Folders) blog post for a guide on how to utilize the script and a breakdown of the RegEx employed. Currently only works for PNG/JPG/GIF, but adding additional attachment cases is not difficult and outlined in my blog post.  

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
