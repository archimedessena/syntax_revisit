# Email Slicing from scratch

def main():
    email_address = input("Enter your email address:")
    (username, domain) = email_address.split("@")
    (domain, extension) = domain.split(".")
    print("Your email address is: %s" % email_address)
    print("Your username is: %s" % username)
    print("Your domain is: %s" % domain)
    print("Your extension is: %s" % extension)



#main()

