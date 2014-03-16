import re
i = 'Re: Compositing two movies'
if re.search('spam',i) or re.search('SPAM',i):
   print 1
