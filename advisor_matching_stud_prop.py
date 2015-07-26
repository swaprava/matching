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

form = cgi.FieldStorage()

print '<h4>Implementing the student proposing matching</h4>'

numOfstudents = int(form.getvalue('numOfstudents'))
numOfadvisors = int(form.getvalue('numOfadvisors'))


studentNames = []
studentPreferences = []

for student in xrange(numOfstudents):
    
    prefInd = 'studpref' + str(student)
    nameInd = 'studname' + str(student)
    
    pref = form.getvalue(prefInd)
    name = form.getvalue(nameInd)
    
    studentNames.append(name)
    
#    print 'Preference of %s: %s <br />' % (name, pref)
    prefSplit = pref.split(',')
    tempList = []
    for i in xrange(len(prefSplit)):
        tempList.append(int(prefSplit[i])-1) # for 0 to n-1 normalization
        
    studentPreferences.append(tempList)

#print studentPreferences


advisorNames = []
advisorPreferences = []
advisorLimit = []

for advisor in xrange(numOfadvisors):
    prefInd = 'advpref' + str(advisor)
    nameInd = 'advname' + str(advisor)
    capacityInd = 'advcapa' + str(advisor)
    
    pref = form.getvalue(prefInd)
    name = form.getvalue(nameInd)
    capacity = form.getvalue(capacityInd)
    
    advisorNames.append(name)
    advisorLimit.append(int(capacity))
    
#    print 'Preference of %s: %s, Capacity = %s <br />' % (name, pref, capacity)
    prefSplit = pref.split(',')
    tempList = []
    for i in xrange(len(prefSplit)):
        tempList.append(int(prefSplit[i])-1) # for 0 to n-1 normalization
        
    advisorPreferences.append(tempList)

#print advisorPreferences
    
# printing the preferences
print '<h5>Students</h5>'

for student in xrange(numOfstudents):
    print 'Preference of <b>%s</b>: ' % studentNames[student]
    for advisor in studentPreferences[student]:
        print '<i>%s</i>;' % advisorNames[advisor]
    print '<br />'
    
print '<h5>Advisors</h5>'

for advisor in xrange(numOfadvisors):
    print 'Preference of <b>%s</b>: ' % advisorNames[advisor]
    for student in advisorPreferences[advisor]:
        print '<i>%s</i>;' % studentNames[student]
        
    print ' Capacity =', advisorLimit[advisor]
    print '<br />'
    
students = range(numOfstudents)
advisors = range(numOfadvisors)

# initial match - empty

match = []
for i in xrange(numOfadvisors):
    match.append([])

studentMatched = []
for j in xrange(numOfstudents):
    studentMatched.append(False)


print '<h4>Algorithm iterations</h4>'

change = True

while change:
    
    change = False
    
    for student in students:
        
        if not studentMatched[student]:
            
            # advisor in the student list
            for advisorIndex in studentPreferences[student]: 
                
                if studentMatched[student]:
                    break
                    
                print 'Student<b>', studentNames[student], '</b>approaches Advisor<b>', advisorNames[advisorIndex], '</b><br />'
#                    print 'match[advisorIndex] =', match[advisorIndex], 'advisorLimit[advisorIndex] =', advisorLimit[advisorIndex]
                
                if len(match[advisorIndex]) < advisorLimit[advisorIndex]:
                    
                    print 'Advisor<b>', advisorNames[advisorIndex], '</b>tentatively accepts Student<b>', studentNames[student], '</b><br />'
                    match[advisorIndex].append(student)
#                        advisorLimit[advisorIndex] = advisorLimit[advisorIndex] - 1
                    change = True
                    studentMatched[student] = True
                    
                else:
                    
                    for alreadyMatched in match[advisorIndex]:
                        
                        if studentMatched[student]:
                            break
                        
                        if advisorPreferences[advisorIndex].index(student) < advisorPreferences[advisorIndex].index(alreadyMatched):
                            
                            print 'Advisor<b>', advisorNames[advisorIndex], '</b>rejects Student<b>', studentNames[alreadyMatched], '</b>and tentatively accepts Student<b>', studentNames[student], '</b><br />'
                            rejectedStudent = match[advisorIndex].pop(match[advisorIndex].index(alreadyMatched))
                            match[advisorIndex].append(student)
                            change = True
                            studentMatched[student] = True
                            studentMatched[rejectedStudent] = False
                            
                if not studentMatched[student]:
                    print 'Advisor<b>', advisorNames[advisorIndex], '</b>rejects Student<b>', studentNames[student], '</b><br />'
                
print '<h4>Final assignment:</h4>'

for advisor in advisors:
    
    s = ''
    for student in match[advisor]:
        s = s + '<b>' + studentNames[student] + '</b>; '
    
    print 'Advisor<b>', advisorNames[advisor], '</b>gets', s, '<br />'

print '<form method="post" action=advisor_matching_cgi.py>'
print '<p>Like this? Want more matching? <input type="submit" value="Let\'s go!"></p>'
print '<div class="fb-like" data-href="advisor_matching_cgi.py" data-layout="standard" data-action="like" data-show-faces="true" data-share="true"></div>'
print '</form>'

print '</body>'
print '</html>'