'''Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

'''

# Time: O(n*m) n for the number for emails and m for the size of the given string

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # initiate a set so we can later pick out the uinque emails
        unique = set()

        # iterate through each email address
        for email in emails:
            # separate by local and domain name
            local, domain = email.split("@")
            # make sure we only store anything that comes before the plus sign
            local = local.split("+")[0]
            # remove all periods from local
            local = local.replace(".", "")

            # once we have the cleaned email, add to the set as pair/tuple
            unique.add((local,domain))
        
        return len(unique)


# Without built-in methods

def numUniqueEmails(emails: List[str]) -> int:
    # initiate a set so we can later pick out the uinque emails
    unique = set()

    # iterate through each email address to
    for email in emails:
        # set our variables
        i,local = 0, ""
        # check if current index is one of the two symbols
        while email[i] not in ["@", "+"]:
            # add every character to local if its not equal to to "."
            if email[i] != ".":
                local += email[i]
                i += 1

        # after getting the local part, we have to also get the domain part of our string
        # this while loop ensures that i still gets incremented in case the while loop above was stopped at a plus sign
        while email[i] != "@":
            i += 1

        # grab everything after the current index of i
        domain = email[i + 1:]
        
        # add to set
        unique.add((local,domain))

    
    return len(unique)