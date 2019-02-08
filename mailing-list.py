# READ-ME #
"""
        A simple mailing list generator.

Use this to quickly generate links to pre-populated emails filled
out with the names and email addresses from your "address_book".

The name is inserted to the body of the email and the appropriate address is set.

By clicking the links from your browser, a pre-populated email will appear
for you to review and send.

                -- Important! --
* This was created using Google Chrome as the browser. *
* I have not tested it with other browsers.            *
* Requirements:                                        *
*   1. You must be signed into your email service.     *
*   2. You must have Service Handlers enabled.         *
*   3. Allow your email provider to open email links   *

- more info: https://gsuitetips.com/tips/chrome/configure-chrome-with-service-handlers/

"""

# Allows us to open our Web Browser
import webbrowser

# Sets variable 'b' to open the 'mailinglist.html' doc.
b = open('mailinglist.html', 'w')

# Dict() of Names and Addresses. The "Address Book".
address_book = {"Mr. George Foreman" : "foreman@grills.co",
        "Mr. Monty Python" : "holygrail@came.lot",
        "Ms. Amber Alert" : "amber@report.me",
        "Mr. Steve Brule" : "sweetberrywine1@ch5news.co",
        "Ms. Jane Doe" : "jdoe@mail.com"}

# Your name here.
sender = "Sender"

# Beginning of HTML doc.
part1 = '''<html>
<head></head>
<body><h1>Send those emails!</h1><ul>'''

# And the end.
part2 = '''</ul></body>
</html>'''

# Loop to iterate through address book and add to the HTML doc.
for x in address_book:
    recipient = x
    address = address_book[x]

    # Body of the email. Includes the recipients name.
    email = f'''Dear%20{recipient}%2C%0A%0AThank%20you%20for%20joining%20my%20mailing%20list!%0A%0AHere%20are%20all%20the%20things%20you%20can%20look%20forward%20to%20enjoying%20this%20year.%0A%0A%20%20%E2%80%A2%20My%20new%20book.%0A%0A%20%20%E2%80%A2%20New%20music.%0A%0A%20%20%E2%80%A2%20A%20podcast%20featuring%20yours%20truly.%0A%0AThank%20you%20for%20joining%20my%20cult-like%20following.%0A%0AYours%20truly%2C%0A%0A{sender}'''

    # Builds the link you will be clicking on. Fills in the email address and the recipients name.
    link = f"""<a href="mailto:{address}?Subject=Thank%20You%20for%20Subscribing!&body={email}" target="_blank">{recipient}</a>"""

    # Creates the link as a HTML list item, <li>.
    insert = f'''<li>{link}</li>'''

    # Adds the link to the HTML page.
    part1 += insert

# Conjoins the HTML doc after the list has been added.
content = part1 + part2

# Writes and closes the "mailinglist.html" doc.
b.write(content)
b.close()

# Opens "mailinglist.html" in a new tab of your Default Browser.
webbrowser.open_new_tab('mailinglist.html')
