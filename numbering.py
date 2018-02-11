def trans():
    def daftar3():
        print ('')
        print ('')
        print ('\t\tNumbering')
        print ('\n============================')
        print ('')
        print ('\nChoose : ')
        for panjang in ('1. English','2. Japanese','3. French','4. Back To First Menu','5. Exit'):
            print panjang
        print ('')

    def back_menu3():
        print ('Do you want to try again? [Y/N] :')
        back = raw_input().upper()
        if back == "Y":
            try:
                clear()
                daftar3()
                pilihan3()
            except:
                print "Please Input Number Only!!"
                back_menu3()
        elif back == "N":
            exit
        else:
            print "Pilih Y [to try again], Pilih N [exit]"
            print ('')
            back_menu3()


    def pilihan3():    
        p = input ("Input Your Choose : ")
        if p == 1:
			x = int(input(' Input Your Number for Translate : '))
			english = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
					11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 
					21: 'twenty-one', 22: 'twenty-two', 23: 'twenty-three', 24: 'twenty-four', 25: 'twenty-five', 26: 'twenty-six', 27: 'twenty-seven', 28: 'twenty-eight', 29: 'twenty-nine', 30: 'thirty', 
					31: 'thirty-one', 32: 'thirty-two', 33: 'thirty-three', 34: 'thirty-four', 35: 'thirty-five', 36: 'thirty-six', 37: 'thirty-seven', 38: 'thirty-eight', 39: 'thirty-nine', 40: 'forty', 
					41: 'forty-one', 42: 'forty-two', 43: 'forty-three', 44: 'forty-four', 45: 'forty-five', 46: 'forty-six', 47: 'forty-seven', 48: 'forty-eight', 49: 'forty-nine', 50: 'fifty', 
					51: 'fifty-one', 52: 'fifty-two', 53: 'fifty-three', 54: 'fifty-four', 55: 'fifty-five', 56: 'fifty-six', 57: 'fifty-seven', 58: 'fifty-eight', 59: 'fifty-nine', 60: 'sixty', 
					61: 'sixty-one', 62: 'sixty-two', 63: 'sixty-three', 64: 'sixty-four', 65: 'sixty-five', 66: 'sixty-six', 67: 'sixty-seven', 68: 'sixty-eight', 69: 'sixty-nine', 70: 'seventy', 
					71: 'seventy-one', 72: 'seventy-two', 73: 'seventy-three', 74: 'seventy-four', 75: 'seventy-five', 76: 'seventy-six', 77: 'seventy-seven', 78: 'seventy-eight', 79: 'seventy-nine', 80: 'eighty', 
					81: 'eighty-one', 82: 'eighty-two', 83: 'eighty-three', 84: 'eighty-four', 85: 'eighty-five', 86: 'eighty-six', 87: 'eighty-seven', 88: 'eighty-eight', 89: 'eighty-nine', 90: 'ninety', 
					91: 'ninety-one', 92: 'ninety-two', 93: 'ninety-three', 94: 'ninety-four', 95: 'ninety-five', 96: 'ninety-six', 97: 'ninety-seven', 98: 'ninety-eight', 99: 'ninety-nine', 100: 'one hundred'}
			x in english
			print ("")
			print (english.get(x))
			print ("\n=================================================")
			print ("")
			back_menu3()
        #<FARAH ULFA>
        elif p == 2:
			x = int(input(' Input Your Number for Translate : '))
			Japanese = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Shi/yon', 5: 'Go', 6: 'Roku', 7: 'Shichi', 8: 'Hachi', 9: 'Kyuu/ku', 10: 'juu', 
					11: 'juu ichi', 12: 'juu ni', 13: 'juu san ', 14: 'juu yon ', 15: 'juu go ', 16: 'juu roku ', 17: 'juu nana ', 18: 'juu hachi ', 19: 'juu kyuu ', 20: 'ni juu ', 
					21: 'ni juu ichi ', 22: 'ni juu ni ', 23: 'ni juu san', 24: 'ni juu yon ', 25: 'ni juu go', 26: 'ni juu roku', 27: 'ni juu nana ', 28: 'ni juu hachi ', 29: 'ni juu kyuu ', 30: 'san juu ', 
					31: 'san juu ichi ', 32: 'san juu ni ', 33: 'san juu san ', 34: 'san juu yon ', 35: 'san juu go ', 36: 'san juu roku ', 37: 'san juu nana ', 38: 'san juu hachi ', 39: 'san juu kyuu ', 40: 'yon juu ', 
					41: 'yon juu ichi ', 42: 'yon juu ni ', 43: 'yon juu san ', 44: 'yon juu yon ', 45: 'yon juu go ', 46: 'yon juu roku ', 47: 'yon juu nana', 48: 'yon juu hachi', 49: 'yon juu kyuu ', 50: 'go juu ', 
					51: 'Go juu ichi ', 52: 'Go ju ni ', 53: 'Go juu san ', 54: 'Go juu yon ', 55: 'Go juu go ', 56: 'Go juu roku ', 57: 'Go juu nana ', 58: 'Go juu hachi ', 59: 'Go juu kyuu ', 60: 'Roku juu ', 
					61: 'Roku juu ichi', 62: 'Roku juu ni', 63: 'Roku juu san', 64: 'Roku juu yon', 65: 'Roku juu go ', 66: 'Roku juu roku ', 67: 'Roku juu nana ', 68: 'Roku juu hachi ', 69: 'Roku juu kyuu ', 70: 'Nana juu ', 
					71: 'Nana juu ichi ', 72: 'Nana juu ni ', 73: 'Nana juu san ', 74: 'Nana juu yon ', 75: 'Nana juu go ', 76: 'Nana juu roku ', 77: 'Nana juu nana', 78: 'Nana juu hachi ', 79: 'Nana juu kyuu ', 
					80: 'Hachi juu ', 81: 'Hachi juu ichi ', 82: 'Hachi juu ni', 83: 'Hachi juu san', 84: 'Hachi juu yon', 85: 'Hachi juu go', 86: 'Hachi juu roku', 87: 'Hachi juu nana', 88: 'Hachi juu hachi', 89: 'Hachi juu kyuu', 
					90: 'Kyuu juu', 91: 'Kyuu juu ichi', 92: 'Kyuu juu ni', 93: 'Kyuu juu san',  94: 'Kyuu juu yon', 95: 'Kyuu juu go', 96: 'Kyuu juu roku', 97: 'Kyuu juu nana', 98: 'Kyuu juu hachi', 99: 'Kyuu juu kyuu', 100: 'Hyaku'}
			x in Japanese
			print ("")
			print (Japanese.get(x))
			print ("\n=================================================")
			print ("")
			back_menu3()

        elif p == 3:
			x = int(input(' Input Your Number for Translate : '))
			French = {1: 'un (ang)', 2: 'deux (deu)', 3: 'trois (trowa)', 4: 'quatre (qatr)', 5: 'cing (senq)', 6: 'six (siz)', 7: 'sept (set)', 8: 'huit (wit)', 9: 'neuf (nef)', 10: 'dix (diz)', 
			11: 'onze (ongz)', 12: 'douze (duz)', 13: 'treize (trez)', 14: 'quatorze (qatorz)', 15: 'qiunze (qengz)', 16: 'seize (sez)', 17: 'dix-sept (diz-set)', 18: 'dix-huit (diz-wit)', 19: 'dix-neuf (diz-nef)', 20: 'vingt (vang)', 
			21: 'ving et un (vang-e-yang)', 22: 'vingt deux (vang deu)', 23: 'vingt trois (vang trowa)', 24: 'vingt quatre (vang qatr)', 25: 'vingt cing (vang senq)', 26: 'vingt six (vang siz)', 27: 'vingt sept (vang set)', 28: 'vingt huit (vang wit)', 29: 'vingt neuf (vang nef)', 30: 'trente (trongt)', 
			31: 'trente et un (trengt-e-yang)', 32: 'trente deux', 33: 'trente trois', 34: 'trente quatre', 35: 'trente cing', 36: 'trente six', 37: 'trente sept', 38: 'trente huit', 39: 'trente neuf', 40: 'quarante (karongt)', 
			41: 'quarante et un (karongt-e-yang)', 42: 'quarante deux', 43: 'quarante trois', 44: 'quarante quatre', 45: 'quarante cing', 46: 'quarante six', 47: 'quarante sept', 48: 'quarante huit', 49: 'quarante neuf', 50: 'cinguante (sengqongt)', 
			51: 'cinguante et un (sengqongt-e-yang)', 52: 'cinguante deux', 53: 'cinguante trois', 54: 'cinguante quatre', 55: 'cinguante cing', 56: 'cinguante six', 57: 'cinguante sept', 58: 'cinguante huit', 59: 'cinguante neuf', 60: 'soixante (sowasongt)', 
			61: 'soixante et un (sowasongt-e-yang)', 62: 'soixante deux', 63: 'soixante trois', 64: 'soixante quatre', 65: 'soixante cing', 66: 'soixante six', 67: 'soixante sept', 68: 'soixante huit', 69: 'soixante neuf', 70: 'soixante-dix (sowazong-diz)', 
			71: 'soixante et onze', 72: 'soixante douze', 73: 'soixante treize', 74: 'soixante quatorze', 75: 'soixante quinze', 76: 'soixante seize', 77: 'soixante dix-sept', 78: 'soixante dix-huit', 79: 'soixante dix-neuf', 80: 'quatre-vingts (qatre-vang)', 
			81: 'quatre-ving et un (qatr-e-yang)', 82: 'quatre-vingt deux', 83: 'quatre-vingt trois', 84: 'quatre-vingt quatre', 85: 'quatre-vingt-cinq', 86: 'quatre-vingt six', 87: 'quatre-vingt sept', 88: 'quatre-vingt huit', 89: 'quatre-vingt neuf', 90: 'quatre-vingt dix', 
			91: 'quatre-vingt onze', 92: 'quatre-vingt douze', 93: 'quatre-vingt treize', 94: 'quatre-vingt quatorze', 95: 'quatre-vingt quinze', 96: 'quatre-vingt seize', 97: 'quatre-vingt dix-sept', 98: 'quatre-vingt dix huit', 99: 'quatre-vingt dix neuf', 100: 'cent (song)'}
			x in French
			print ("")
			print (French.get(x))
			print ("\n=================================================")
			print ("")
			back_menu3()
			
        elif p == 4:
            clear()
            back_utama()		

        elif p==5	:
            exit
        
        else:
            print "You input nothing found in choose !!"
            print ("")
            back_menu3()
        
    try:
        daftar3()
        pilihan3()
    except:
        print "Please Input Number Only!!"
        back_menu3()


def daftar_utama():
    print ("")        #<FARAH ULFA>
    print ("")
    print ("     Panel Dictionary")
    print ("\n============================")
    print ("")
    print ("\nChoose : ")
    for Menu_Utama in ["1. Numbering","2. Exit"]:
        print Menu_Utama
    print ("")
    
def back_utama():
    print ('Do you want to first menu? [Y/N] :')
    back2= raw_input().upper()
    if back2=="Y":   
        try:        #<FARAH ULFA>
            clear()
            daftar_utama()
            pilihan_utama()
        except:
            clear()
            print "Please Input Number Only!!"
            back_utama()
    elif back2=="N":
        exit
    else:
        print "Pilih Y [to try again], Pilih N [Exit]"
        back_utama()
        
def pilihan_utama():
    q=input ("Input Your Choose : ")
    if q==1:
        trans()
    elif q==2:
        exit
    else:        #<FARAH ULFA>
        clear()
        print "You input nothing found in choose !!"
        print ""
        back_utama()
            


try:
    daftar_utama()
    pilihan_utama()
except:
    print "Please Input Number Only!!"
    back_utama()
