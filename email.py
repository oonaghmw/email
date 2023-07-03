"""
--- OOP Email Simulator --- 
Simulates email objects and the basic functionality of an inbox. 
When run, creates inbox list and initialises three sample emails. 
Could potentially add methods to view spam folder etc. but currently 
functionality not added to maintain the main menu as described in brief.

Emails are displayed as string formatted as: 
--------------------------------------------------
Subject:    <Subject>
from:       <E-mail address>
------------------message-body--------------------
<E-mail body>
--------------------------------------------------
"""

# --- Email Class --- #

class Email(object):
    """
    Object to simulate email behaviour.
    
    Args for instance variables:
    email_address - string giving email address
    subject_line  - string subject line for email
    email_content - string giving body of email

    Class variables:
    has_been_read - set to False upon initialisation,
                    set to True if email is read.
    """
    has_been_read = False
    
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    def mark_as_read(self):
        """
        Changes 'has_been_read' variable from False to True
        and prints a confirmation message.
        """
        self.has_been_read = True
        print(f"< Email from {self.email_address} marked as read >\n")

    def display_email(self):
        """
        Prints email in readable string style.
        """
        print(f"""
--------------------------------------------------
Subject:    {self.subject_line}
from:       {self.email_address}
------------------message-body--------------------
{self.email_content}
--------------------------------------------------
""")
    
# --- Lists --- #
inbox = [] #store emails

spam = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(email_address, subject_line, contents):
    """
    Creates an instance of the Email object with the email address, 
    subject line and contents, and stores it in the Inbox list. Used 
    at program start to populate inbox list.

    Args:
    email_address - string giving address of sender of email to be 
                    added to inbox
    subject_line  - string giving subject line of email to be added
                    to inbox
    contents      - string body of email to be added to inbox

    Returns:
    None
    """
    email = Email(email_address, subject_line, contents)
    inbox.append(email)


def list_emails():
    """
    Prints subject_line attribute of all emails in inbox, along with a 
    corresponding number.
    """
    for i, email in enumerate(inbox): 
        print(f"{i}\t{email.subject_line}")


def read_email(index):
    """
    Displays a selected email from inbox based on index argument.
    Once displayed calls class method to set its 'has_been_read'
    variable to True.

    Arg:
    index - index of email in inbox to be read 

    Returns:
    None
    """
    selected = inbox[index]
    # Create a function which displays a selected email. 
    selected.display_email()
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    selected.mark_as_read() 
    

def delete_email(index):
    """
    Removes email object from inbox list then deletes it.

    Arg:
    index - index of email in inbox to be read 

    Returns:
    None
    """
    deleted = inbox.pop(index)
    del deleted


def email_action(index):
    """
    For additional functionality after viewing an email - user
    can give input to choose an action (delete or mark as spam) or
    can return to menu. Loops until valid input given. 
    Not case-sensitive.

    Arg:
    Index - the index in inbox of current email being viewed.
    """
    while True:
        try:
            action = input("Would you like to delete (d), mark as spam (s), or return to inbox menu (m)? ").lower()
        except AttributeError: #if input not string
            pass 
        
        if action == "d":
            delete_email(index)
            print("\n< Email deleted >\n")
            return

        elif action == "s":
            spam_email = inbox.pop(index) 
            spam.append(spam_email)
            print("\n< Message moved to spam >\n")
            return

        elif action == "m":
            return

        print("\nInvalid input! \n")


# --- Email Program --- #

# Populate the Inbox for further use in program.
for i in range(3):
    address = f"sample{i}@email.com"
    subject = f"Sample subject {i}"
    content = f"Body of email {i}\nEmail body"

    populate_inbox(address, subject, content)

# Logic for the various menu operations.
menu = True # ?

while True:
    try:
        user_choice = int(input('''
       Would you like to:
    1. Read an email
    2. View unread emails
    3. Quit application 

    Enter selection: ''')) 
    
    #if input cannot be cast to int:
    except ValueError:
        print("\nPlease enter a number! ")
        continue
    

    if user_choice == 1:
        # Read an email
        while True:
            try:
                email_index = int(input("\nWhich email would you like to read? ")) 
                
                if email_index in range(len(inbox)):
                    break

            # if input cannot be cast to int:
            except ValueError:
                pass

            print("Invalid entry!\n") 
        
        read_email(email_index) 
        email_action(email_index)


    elif user_choice == 2:
        # view unread emails (with number for index)
        print()

        #flag so can give message if no unread emails:
        all_read = True

        for i, email in enumerate(inbox):
            if not email.has_been_read:
                print(f"{i}\t{email.subject_line}")
                all_read = False
        
        if all_read:
            print("\nNo unread messages! \n")

    
    elif user_choice == 3:
        # quit application
        print("\n\t- Goodbye! -\n")
        exit()


    else:
        print("\nOops - incorrect input.\n")

