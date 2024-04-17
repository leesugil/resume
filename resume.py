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

conn = sqlite3.connect("resume.db")
cur = conn.cursor()
cur.execute("""
            create table if not exists resume_entries (
            id integer primary key,
            is_active integer,
            start text,
            end text,
            role text,
            organization text,
            street text,
            city text,
            country text,
            short text,
            medium text,
            long text,
            excellency_short text,
            excellency_medium text,
            excellency_long text,
            problem_short text,
            problem_medium text,
            problem_long text,
            challenge_short text,
            challenge_medium text,
            challenge_long text,
            skillset text,
            salary integer,
            reference text,
            hashtag text
            )
            """)
cur.execute("""
            create table if not exists portfolio_entries (
            id integer primary key,
            is_active integer,
            title text,
            short text,
            medium text,
            long text,
            hyperlink text,
            skillset text
            )
            """)

# Enter a Resume Entry
def enter():
    values = {}
    values['is_active'] = 1
    values['role'] = input("What was the role/title of the position? \n> ")
    values['organization'] = input(f"What was the name of the organization that you had the {values['role']} position? \n> ")
    values['start'] = input(f"When did you start taking the {values['role']} position at {values['organization']}? (YYYY-MM-DD) \n> ")
    values['end'] = input(f"When did you end taking the {values['role']} position at {values['organization']}? (YYYY-MM-DD) \n> ")
    values['city'] = input(f"In which city was your workplace in {values['organization']} located? \n> ")
    values['street'] = input(f"What was the street address of your workplace in {values['organization']}? \n> ")
    values['country'] = input(f"In which country was your workplace in {values['organization']} located? \n> ")
    values['short'] = input(f"Describe your {values['role']} role at {values['organization']} briefly for the version shown in the \"short\" version of your resume: \n> ")
    values['medium'] = input(f"Describe your {values['role']} role at {values['organization']} in a medium length for the version shown in the \"medium\" version of your resume: \n> ")
    values['long'] = input(f"Describe your {values['role']} role at {values['organization']} in a long length for the version shown in the \"long\" version of your resume: \n> ")
    values['excellency_short'] = input(f"Provide the proof of excellency of your {values['role']} role at {values['organization']} briefly for the version shown in the \"short\" version of your resume: \n> ")
    values['excellency_medium'] = input(f"Provide the proof of excellency of your {values['role']} role at {values['organization']} in a medium length for the version shown in the \"medium\" version of your resume: \n> ")
    values['excellency_long'] = input(f"Provide the proof of excellency of your {values['role']} role at {values['organization']} in a long length for the version shown in the \"long\" version of your resume: \n> ")
    values['problem_short'] = input(f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe briefly for the version shown in the \"short\" version of your resume: \n> ")
    values['problem_medium'] = input(f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a medium length for the version shown in the \"medium\" version of your resume: \n> ")
    values['problem_long'] = input(f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a long length for the version shown in the \"long\" version of your resume: \n> ")
    values['challenge_short'] = input(f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe briefly for the version shown in the \"short\" version of your resume: \n> ")
    values['challenge_medium'] = input(f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a medium length for the version shown in the \"medium\" version of your resume: \n> ")
    values['challenge_long'] = input(f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a long length for the version shown in the \"long\" version of your resume: \n> ")
    skillset_input = input(f"List your relevant skills to the {values['role']} role in {values['organization']} (separated by comma) \n> ")
    skillset_list = [word.strip() for word in skillset_input.split(',')]
    values['skillset'] = json.dumps(skillset_list)
    values['salary'] = int(input(f"What was the salary of the {values['role']} position in {values['organization']} in USD? \n> "))
    values['reference'] = input(f"Provide the reference information if you have one: \n> ")
    hashtag_input = input(f"List hashtags for this resume entry ({values['role']} at {values['organization']}) separated by commas: \n> ")
    hashtag_list = [word.strip() for word in hashtag_input.split(',')]
    values['hashtag'] = json.dumps(hashtag_list)

    fields = values.keys()
    sql = f"insert into resume_entries ({', '.join(fields)}) values ({', '.join(['?' for _ in fields])})"
    cur.execute(sql, list(values.values()))
    conn.commit()
