# Design
#   This program has 4 main functions:
#   1) View resume
#       Select a keyword to filter the record and generate a resume.
#       The initial outcome is a resume class that one can specify its format
#       a little before printing out the final outcome.
#   2) Create a new resume entry
#       Create a new entry
#   3) Edit a resume entry
#       Edit an existing entry
#   4) Delete a resume entry
#       Disabling an existing entry to show up in the output.
#       It doesn't permanently delete the entry from the database but set the is_active variable to 0.

import sqlite3
import json
import atexit

conn = sqlite3.connect("resume.db")
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS resume_entries (
            id INTEGER PRIMARY KEY,
            is_active INTEGER,
            start TEXT,
            end TEXT,
            role TEXT,
            organization TEXT,
            street TEXT,
            city TEXT,
            state TEXT,
            zipcode TEXT,
            country TEXT,
            short TEXT,
            medium TEXT,
            long TEXT,
            excellency_short TEXT,
            excellency_medium TEXT,
            excellency_long TEXT,
            problem_short TEXT,
            problem_medium TEXT,
            problem_long TEXT,
            challenge_short TEXT,
            challenge_medium TEXT,
            challenge_long TEXT,
            skillset TEXT,
            salary INTEGER,
            reference TEXT,
            hashtag TEXT
            )
            """)
cur.execute("""
            CREATE TABLE IF NOT EXISTS portfolio_entries (
            id INTEGER PRIMARY KEY,
            is_active INTEGER,
            title TEXT,
            short TEXT,
            medium TEXT,
            long TEXT,
            hyperlink TEXT,
            skillset TEXT
            )
            """)

def close_resume():
    print("resume: Closing cursor and connector")
    cur.close()
    conn.close()

atexit.register(close_resume)

# Create a Resume Entry
def enter_text(key, q, values):
    """
    Accepts a user input from the questionnaire q, store the response in values[key].
    If nothing is provided (an empty string), function either stores the empty string as the value or keep the originally stored value if there's one.
    """
    ans = input("\n" + q + "\n> ")
    if (len(ans) == 0 and key in values):
        pass
    else:
        values[key] = ans

def enter_integer(key, q, values):
    """
    Similar to exter_text(key, q, values) but for integer input
    """
    ans = input("\n" + q + "\n> ")
    if (len(ans) == 0 and key in values):
        pass
    else:
        try:
            values[key] = int(ans)
        except:
            values[key] = 0


def enter_text_multiple(key, q, values):
    """
    Similar to enter(key, q, values), but accepts values of a CSV format and stores it as a list.
    """
    ans = input("\n" + q + "\n>")
    if (len(ans) == 0 and key in values):
        pass
    else:
        ans_list = [word.strip() for word in ans.split(',')]
        values[key] = json.dumps(ans_list)

def enter():
    values = {}
    values['is_active'] = 1
    retry = "n"
    while (retry == "n"):
        print("\n(For leaving any entry empty or keeping the existing value without making any changes, just press enter to skip the entry.\n")

        key = 'role'
        q = "What was the role/title of the position?"
        enter_text(key, q, values)

        key = 'organization'
        q = f"What was the name of the organization that you had the {values['role']} position?"
        enter_text(key, q, values)

        key = 'start'
        q = f"When did you start taking the {values['role']} position at {values['organization']}? (YYYY-MM-DD)"
        enter_text(key, q, values)

        key = 'end'
        q = f"When did you end taking the {values['role']} position at {values['organization']}? (YYYY-MM-DD)"
        enter_text(key, q, values)

        key = 'city'
        q = f"In which city was your workplace in {values['organization']} located?"
        enter_text(key, q, values)

        key = 'street'
        q = f"What was the street address of your workplace in {values['organization']}?"
        enter_text(key, q, values)

        key = 'state'
        q = f"In which state was your workplace in {values['organization']} located?"
        enter_text(key, q, values)

        key = 'zipcode'
        q = f"What was the zipcode of your workplace in {values['organization']}"
        enter_text(key, q, values)

        key = 'country'
        q = f"In which country was your workplace in {values['organization']} located?"
        enter_text(key, q, values)

        key = 'short'
        q = f"Describe your {values['role']} role at {values['organization']} briefly for the version shown in the \"short\" version of your resume:"
        enter_text(key, q, values)

        key = 'medium'
        q = f"Describe your {values['role']} role at {values['organization']} in a medium length for the version shown in the \"medium\" version of your resume:"
        enter_text(key, q, values)

        key = 'long'
        q = f"Describe your {values['role']} role at {values['organization']} in a long length for the version shown in the \"long\" version of your resume:"
        enter_text(key, q, values)

        key = 'excellency_short'
        q = f"Provide the proof of excellency of your {values['role']} role at {values['organization']} briefly for the version shown in the \"short\" version of your resume:"
        enter_text(key, q, values)

        key = 'excellency_medium'
        q = f"Provide the proof of excellency of your {values['role']} role at {values['organization']} in a medium length for the version shown in the \"medium\" version of your resume:"
        enter_text(key, q, values)

        key = 'excellency_long'
        q = f"Provide the proof of excellency of your {values['role']} role at {values['organization']} in a long length for the version shown in the \"long\" version of your resume:"
        enter_text(key, q, values)

        key = 'problem_short'
        q = f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe briefly for the version shown in the \"short\" version of your resume:"
        enter_text(key, q, values)

        key = 'problem_medium'
        q = f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a medium length for the version shown in the \"medium\" version of your resume:"
        enter_text(key, q, values)

        key = 'problem_long'
        q = f"What were some main problems in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a long length for the version shown in the \"long\" version of your resume:"
        enter_text(key, q, values)

        key = 'challenge_short'
        q = f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe briefly for the version shown in the \"short\" version of your resume:"
        enter_text(key, q, values)

        key = 'challenge_medium'
        q = f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a medium length for the version shown in the \"medium\" version of your resume:"
        enter_text(key, q, values)

        key = 'challenge_long'
        q = f"What were some main challenges in your {values['role']} role at {values['organization']} and how did you solve them? Describe in a long length for the version shown in the \"long\" version of your resume:"
        enter_text(key, q, values)

        key = 'skillset'
        q = f"List your relevant skills to the {values['role']} role in {values['organization']} (separated by comma)"
        enter_text_multiple(key, q, values)

        ket = 'salary'
        q = f"What was the salary of the {values['role']} position in {values['organization']} in USD?"
        enter_integer(key, q, values)

        key = 'reference'
        q = f"Provide the reference information if you have one:"
        enter_text(key, q, values)

        key = 'hashtag'
        q = f"List hashtags for this resume entry ({values['role']} at {values['organization']}) separated by commas:"
        enter_text_multiple(key, q, values)

        retry = input(f"Is the information correct? (y/n)\n{values}\n")
    return values

def create():
    """create a new resume entry"""
    values = enter()
    fields = values.keys()
    sql = f"""
    INSERT INTO resume_entries ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in fields])})
    """
    cur.execute(sql, list(values.values()))
    conn.commit()
    print(f"A new resume entry of {values['role']} at {values['organization']} has been successfully created.")

def generate_dicts(cur):
    fields = [d[0] for d in cur.description]
    while True:
        rows = cur.fetchmany()
        if not rows:
            return
        for row in rows:
            yield dict(zip(fields, row))

class resume(object):
    def refresh(self):
        cur.execute("SELECT * FROM resume_entries WHERE is_active = 1")
    def __init__(self):
        self.refresh()
        self.theme = "default"
        self.length = "short"   # medium, long
        self.show_description = True
        self.show_proof_of_excellency = True
        self.show_problems_solved = True
        self.show_most_challenging_experience = True
        self.show_street = True
        self.show_city = True
        self.show_state = True
        self.show_zipcode = True
        self.show_country = True
        self.show_dates = True
        self.show_months = True
        self.show_reference = True
        self.show_skillset = True
    def print(self):
        for row in generate_dicts(cur):
            form = f""
            try:
                form += f"ID: {row['id']}\n"
                form += f"{row['role']}\n"
                form += f"{row['organization']}\n"
                form += f"{row['start']} - {row['end']}\n"
                if (self.show_street):
                    form += f"{row['street']}\n"
                if (self.show_city):
                    form += f"{row['city']}\n"
                if (self.show_state):
                    form += f"{row['state']}\n"
                if (self.show_zipcode):
                    form += f"{row['zipcode']}\n"
                if (self.show_country):
                    form += f"{row['country']}\n"
                if (self.length != "short" and self.length != "medium" and self.length != "long"):
                    print("Length error, setting to short")
                    self.length = "short"
                if (self.show_description):
                    form += "Description:\n"
                    key = self.length
                    form += f"{row[key]}\n"
                if (self.show_proof_of_excellency):
                    form += "Proof of Excellency:\n"
                    key = "excellency_" + self.length
                    form += f"{row[key]}\n"
                if (self.show_problems_solved):
                    form += "Problems Solved:\n"
                    key = "problem_" + self.length
                    form += f"{row[key]}\n"
                if (self.show_most_challenging_experience):
                    form += "Most Challenging Experience:\n"
                    key = "challenge_" + self.length
                    form += f"{row[key]}\n"
                if (self.show_reference):
                    form += f"Refrence: {row['reference']}\n"
                if (self.show_skillset):
                    form += "Skills: "
                    form += ", ".join(json.loads(row['skillset']))
            except:
                print("Error loading a printout form")
            print("\n"+form)
        self.refresh()
