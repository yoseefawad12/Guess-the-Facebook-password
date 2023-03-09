import mechanize
br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-Agent','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36')]

br.open('https://www.facebook.com/')
br.select_form(nr=0)
id=input("enter email : ")
ps=input("enter pasword : ")
br.form['email']= id
br.form['pass']= ps
sub=br.submit()
print(sub.geturl())
if 'https://m.facebook.com/recover/initiate/?privacy_mutation_token=eyJ0eXBlIjo1LCJjcmVhdGlvbl90aW1lIjoxNjc4MzUwMzAyfQ%3D%3D&ars=m_lara_first_password_failure&ram=email&_rdr' in sub.gturl():
    print('check your passeord or email')
elif "welcome" or "https://m.facebook.com"  in sub.gturl():
    print('acess granted')
