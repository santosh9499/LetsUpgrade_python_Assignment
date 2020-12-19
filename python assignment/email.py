import emails
html_text = '''<p><span style="font-family: Courier New, courier;"><span style="backgroun
d-color: rgb(247, 218, 100);">HEY THERE,</span>&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;"><br></span></p>
<p><span style="font-family: Courier New, courier;">How are you this is SANTOSH FROM LET
sUpgrade,&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;">I LOVE LETSUPGRADE !!</span></p>
<p><span style="font-family: Courier New, courier;">I made this project hope ull like it,thank you&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;"><br></span></p>
<p><span style="font-family: Courier New, courier;">Regards,&nbsp;</span></p>
<p><strong><span style="font-family: Courier New, courier;">im rowdy,</span></strong><
/p>
<p><span style="font-family: Courier New, courier;"><strong>Santosh Kharpude</strong></
span></p>'''

message = emails.html(html=html_text,subject="Your EMAIL FROM PYTHON SCRIPT",mail_from=('Rowdy LetsUpgrade', 'santosh@xyz.com'))
mail_via_python

def sendMail(email, name):
html_text = '''<p><span style="font-family: Courier New, courier;"><span style="backg
round-color: rgb(247, 218, 100);">HEY Rowdy,'''+ name+'''</span>&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;"><br></span></p>
<p><span style="font-family: Courier New, courier;">How are you this is S
ANTOSH FROM LEtsUpgrade,&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;"> I LOVE LETSUPGRADE !!<
/span></p>
<p><span style="font-family: Courier New, courier;">i made this project
, hope you like this project&nbsp;</span></p>
<p><span style="font-family: Courier New, courier;"><br></span></p>
<p><span style="font-family: Courier New, courier;">Regards,&nbsp;</span
></p>
<p><strong><span style="font-family: Courier New, courier;">Rowdy,
</span></strong></p>
<p><span style="font-family: Courier New, courier;"><strong>Santosh kharpuder</strong></span></p>'''
subject = "Hey Rowdy "+ name + ", you have EMAIL FROM Santosh"
message = emails.html(html=html_text,
subject=subject,
mail_from=('Santosh', 'santosh@xyz.com'))
mail_via_python = message.send(to=email,
smtp={'host': 'smtp.gmail.com',
'timeout': 5,
'port':587,
'user':'santosh@gmail.COM',
'password':'san@1234',
'tls':True})
return mail_via_python.status_code
sendMail("santoshh@gmail.com","Santosh")
