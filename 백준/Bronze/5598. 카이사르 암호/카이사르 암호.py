word = input()
password = {'A':'D','B':'E','C':'F','D':'G','E':'H','F':'I','G':'J','H':'K','I':'L','J':'M','K':'N','L':'O','M':'P','N':'Q','O':'R',
'P':'S','Q':'T','R':'U','S':'V','T':'W','U':'X','V':'Y','W':'Z','X':'A','Y':'B','Z':'C'}

password_rev = {v:k for k,v in password.items()}
        
for letter in word:
    print(password_rev[letter], end='')