import imapclient, pyzmail

mail=imapclient.IMAPClient('imap.gmail.com',ssl=True)
mail.login('singhsomesh0@gmail.com','themorningstar')
mail.select_folder('INBOX',readonly=True)
uids=mail.search('SINCE 01-Nov-2017')
raw_mails=mail.fetch(uids,['BODY[]'])
mails=pyzmail.PyzMessage.factory(raw_mails[uids[-1]][b'BODY[]'])
print(mails.get_subject())
print(mails.get_addresses('from'))
print(mails.get_addresses('delivered-to'))
if mails.text_part:
    print(mails.text_part.get_payload().decode('utf-8'))
if mails.html_part:
    print(mails.html_part.get_payload().decode())

mail.logout()
