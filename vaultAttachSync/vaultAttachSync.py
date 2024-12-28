import pathlib # Handle File Paths and Globbing
import re # Regular Expressions
import shutil # Handle Copying Files
import codecs # Handle Encoding Bytes
import argparse # Handle CLI Arguements

3 # Intialize argparse
parser = argparse.ArgumentParser(prog="vaultAttachSync",
                                 description="Handles copying attachments from your old Obsidian Vault to your new Obsidian Vault")
# Define CLI Arguements
newVault = parser.add_argument_group('New (Target) Vault', 'Arguments for Vault Currently Missing Attachments')
newVault.add_argument('-n',
                        help="Absolute Path to New Vault where attachments will be copied to",
                        dest='newPathArg', 
                        required=True)
newVault.add_argument('--na', 
                        help="Relative Path to Vault's Attachment Storage (Default=/)",
                        dest="newAttachPath", 
                        default="")
oldVault = parser.add_argument_group('Original (Source) Vault', 'Arguments for Source of Vault Attachments')
oldVault.add_argument('-o',
                        help="Absolute Path to Original Vault where attachments will be copied from",
                        dest="oldPathArg",
                        required=True)
oldVault.add_argument('--oa', 
                        help="Relative Path to Vault's Attachment Storage (Default=/)", 
                        dest="oldAttachPath",
                        default="")

# Store Arguemnts in Program's Namespace:
args = parser.parse_args()
# Necessary Global Namespace Variables
newVaultPath = pathlib.Path(args.newPathArg)
oldVaultPath = pathlib.Path(args.oldPathArg)

def getImages(vaultFile)->list:
    '''Takes WindowsPath object and RegExs on File. Returns Images Found'''
    try:
        images = re.findall(r"\[\[(?:.*?/)(.*?\.png)(?:\|.*?)]]", codecs.decode(vaultFile.read_bytes())) # Return List of Images
        if images: # Ensure Atleast 1 Image
            print(f"[*] From {str(vaultFile)}", end="")
            return images
    except UnicodeDecodeError:
        print(f"[-] Error Decoding {vaultFile.name}'s Contents")
    except Exception as e:
        print(f"[-] RegEx Exited With Error Code: {e}")
    

def copyImages(imageName:str)->bool:
    '''Copies passed image from Old Vault Path to New Vault Path'''
    try:
        # shutil.copy(old/image.png, new/image.png)
        if shutil.copy(oldVaultPath / f"{args.oldAttachPath}" / f"{imageName}", 
                       newVaultPath / f"{args.newAttachPath}" / f"{imageName}"): 
            return True # Retun True if copy succeeded
        else:
            print(f"[-] Failed to Copy: {imageName}")
            return False # Return False if copy failed
    except Exception as e:
        print(f"[-] Error Encountered when processing \"{imageName}\"\nERROR CODE: {e}")


def main():
    # Recursively Go Through All Files and Subdirectories
    for file in newVaultPath.rglob("*"):
        if not file.is_file() or ".md" not in file.name: # Ensure File and Markdown File
            continue
        images = getImages(file) # Get Image Names in File 
        if images:
            print(f" Copying {len(images)} Images [*]") 
            # Copy Image From Old Vault -> New Vault
            for image in images:
                copyImages(image)

# __name__ != __main__ if program imported 
if __name__ == "__main__":
    main()
    print("\n\n[*] All Files Copied - Exiting [*]")

