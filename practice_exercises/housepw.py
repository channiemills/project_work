def housepw(data):
    """
    Check passwords for security
    :param data: 
    :return: True if password is secure else false
    """
    return (len(data) >= 10 and any(i.isdigit() for i in data) and
    any(i.isalpha() for i in data) and any(i.isupper() for i in data) and
    any(i.islower() for i in data))


if __name__ == '__main__':
    assert housepw('A1213pokl') == False, "1st example"
    assert housepw('bAse730onE4') == True, "2nd example"
    assert housepw('asasasasasasasaas') == False, "3rd example"
    assert housepw('QWERTYqwerty') == False, "4th example"
    assert housepw('123456123456') == False, "5th example"
    assert housepw('QwErTy911poqqqq') == True, "6th example"
    print("Tests complete!")
