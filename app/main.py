import sys
import gitInit
import hashObjects

def main():
    try:
        commandList = []
        for cmd in sys.argv:
            commandList.append(cmd)
        if commandList[1] == "init":
            gitInit.createGitRepos()
        elif (commandList[1] == "cat-file") and (commandList[2] == "-p"):
            hashObjects.readBlob(commandList[3])
        else:
            raise RuntimeError(f"Unknown git command")
    except IndexError: 
        print("No git cmd line argument found", file=sys.stderr)

if __name__ == "__main__":
    main()
