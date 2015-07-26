#!/usr/bin/env python
"""
Created on Thu Jul 16 19:57:23 2015

Build a webpage where the inputs are provided by the user
This program runs and matches students to advisors using
the Gale-Shapley deferred acceptance algorithm

@author: swaprava
"""

import cgi
import cgitb
cgitb.enable()

print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head><title>Deferred acceptance matching</title></head>'
print '<body>'

print '<br /><h3>Gale-Shapley deferred acceptance matching advisors to students</h3>'
print 'This application takes individual student\'s and advisor\'s preferences as input.<br />Additionally, it also asks for advisors\' capacities and returns the matching<br />of the students to advisors using the algorithm.'

    
studentAdvisorinfoGiven = False
preferencesGiven = False

form = cgi.FieldStorage()


if form.getvalue('numOfstudents'):
    if form.getvalue('numOfadvisors'):
        numOfstudents = int(form.getvalue('numOfstudents'))
        numOfadvisors = int(form.getvalue('numOfadvisors'))
        
            
        studentAdvisorinfoGiven = True
        
        if not preferencesGiven:
            print '<p><i>Now the fun begins!</i></p>'
            
            print 'Give the preferences:<br />'
            print 'Enter the preferences of the students and advisors in comma separated form<br />'
            print 'Numbers denote both the students and advisors<br />'
            print 'Example: (for 4 advisors) <b>4,3,1,2</b> denotes that the student preference over advisors<br />'
            print 'similarly (for 5 students) <b>3,2,1,5,4</b> denotes that the advisor preference over students<br />'
            
            print '<br/><h4>Students and their preferences</h4>'
            print '<form method="post">'
            for student in xrange(numOfstudents):
                pref = 'studpref' + str(student)
                name = 'studname' + str(student)
                print '<p>Enter name and preference of Student %d:<br /> &emsp; Name: <input type="text" name="%s" required> &nbsp; Preference: <input type="text" name="%s" required></p>' % (student+1, name, pref)
                
            print '<br/><h4>Advisors, their preferences, and capacities</h4>'
            for advisor in xrange(numOfadvisors):
                pref = 'advpref' + str(advisor)
                name = 'advname' + str(advisor)
                capacity = 'advcapa' + str(advisor)
                print '<p>Enter name and preference of Advisor %d:<br /> &emsp; Name: <input type="text" name="%s" required> &nbsp; Preference: <input type="text" name="%s" required> &nbsp; Capacity: <input type="text" size="3" name="%s" required></p>' % (advisor+1, name, pref, capacity)
                
            print '<input type="hidden" name="numOfstudents" value="%s">' % numOfstudents
            print '<input type="hidden" name="numOfadvisors" value="%s">' % numOfadvisors
            print '<br/><input type="submit" formaction="advisor_matching_stud_prop.py" value="Match using student proposing version">'
#            print '&emsp;'
#            print '<input type="submit" formaction="" value="Match using advisor proposing version">'
            print '</form>'

        

if not studentAdvisorinfoGiven:
    print '<form method="post" action=advisor_matching_cgi.py>'
    print '<p>Enter the number of students &emsp; <input type="text" name="numOfstudents" required></p>'
    print '<p>Enter the number of advisors &emsp; <input type="text" name="numOfadvisors" required></p>'
    print '<input type="submit" value="Submit">'
    print '</form>'

print '</body>'
print '</html>'