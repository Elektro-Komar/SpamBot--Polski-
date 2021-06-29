import pyautogui, time
odp1 = input("Czy chcesz stworzyć plik .spam?(TAK/NIE): ")
if odp1 == "TAK":
    import createSpamFile
elif odp1 == "Tak":
    import createSpamFile
elif odp1 == "tak":
    import createSpamFile
if odp1 == "NIE":
    odp2 = input("Wprowadź nazwę stworzonego pliku z rozszerzeniem .spam:  ")
    filem = open(odp2, 'r')

    time.sleep(5)
    for word in filem:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


    pyautogui.typewrite("Zostales zaspamowany przez SpamBot w wersji 1.0 Szczegoly na stronie http://spambot.wex.pl")
    pyautogui.press("enter")
elif odp1 == "nie":
    odp2 = input("Wprowadź nazwę stworzonego pliku z rozszerzeniem .spam:  ")
    filem = open(odp2, 'r')

    time.sleep(5)
    for word in filem:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

    pyautogui.typewrite("Zostales zaspamowany przez SpamBot w wersji 1.0 Szczegoly na stronie http://spambot.wex.pl")
    pyautogui.press("enter")
elif odp1 == "Nie":
    odp2 = input("Wprowadź nazwę stworzonego pliku z rozszerzeniem .spam:  ")
    filem = open(odp2, 'r')

    time.sleep(5)
    for word in filem:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


    pyautogui.typewrite("Zostales zaspamowany przez SpamBot w wersji 1.0 Szczegoly na stronie http://spambot.wex.pl")
    pyautogui.press("enter")

