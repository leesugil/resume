# Design
#   This program has 4 main functions:
#   1) View resume
#       Select a keyword to filter the record and generate a resume.
#       The initial outcome is a resume class that one can specify its format
#       a little before printing out the final outcome.
#   2) Enter resume entry
#       Enter a new entry
#   3) Edit resume entry
#       Edit an existing entry
#   4) Delete resume entry
#       Disabling an existing entry to show up in the output.

import sqlite3
import json

conn = sqlite3.connector("resume.db")
cur = conn.cursor()
cur.execute("""create table if not exists resume_entries
            (id integer primary key,
            is_active integer,
            start text,
            end text,
            role text,
            organization text,
            street_address text,
            city text,
            country text,
            short text,         # one-line description of the role
            medium text,        # three-line desciption of the role
            long text,          # indefinite length but be reasonable
            skillset text,
            salary integer,
            hashtag text,       # like 'academia', 'industry', 'tech', 'hobby', 'volunteer'
            """)

# Enter a Resume Entry
def enter():
    role = input("What was the role/title of the position? ")
    organization = input(f"What was the name of the organization that you had the ? ")
    start = input("When was the start of this position? ")
