#! /usr/bin/python3
import getpass

# This should not be a problem.
def some_process(u, p) -> None:
    pass

username="Jeff"
password=getpass.getpass(f"Enter password for {username} : ")

some_process(username, password)
