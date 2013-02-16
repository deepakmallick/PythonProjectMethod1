'''Create an html file with  user input (a name) embedded,
and call the default web browser to display the file.'''

# NEW more appropriate name, now that it is a format string
pageTemplate = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>My Python Assignment</title>
</head>
<body style="background-color:Green;">
<h1>Technical Portfolio</h1>
<b>Carrier Objective:</b><br>
<i>{portfolio_headline}</i>

<h3>Personal Details</h3>
<b>{first_name}</b> <b>{last_name}</b><br>
{phone}<br>
Address: {address}<br>
Email id: {email_id}

<h3>Expertise</h3>
Currently Working In <b>{current_employer}</b> as a <i>{designation}</i><br>
Total Experience: {experience}<br>
Key Skills: {key_skills}<br>

<h3>Education</h3>
{basic_graduation} in <i>{specialization}</i><br>
Graduated From <b>{university}</b>
Year Of Passing: {year}

 
</body>
</html>''' 

def main():    # NEW
    portfolio_headline = input("Enter your Carrier Objective: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Phone: ")
    address = input("Enter your address: ")
    email_id = input("email id: ")
    current_employer = input("Current Employer: ")
    designation = input("Designation: ")
    experience = input("Experience: ")
    key_skills = input("Key Skills: ")
    basic_graduation = input("Basic Graduation(B.Tech/BCA/Diploma): ")
    specialization = input("Specialization: ")
    university = input("University/Institute: ")
    year = input("Year of passing: ")
    
    contents = pageTemplate.format(**locals())   
    browseLocal(contents) 

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()
