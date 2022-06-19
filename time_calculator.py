def add_time(start, duration,day=False):

## debe sumar duration,debe cambiar de AM to PM y viceversa
## si paso argumento de dia, debe darte si corresponde a duration
### el siguente dia y AM PM
 elementos=start.split(" ") ### 
 hour=elementos[0]## string 
 typ=elementos[1]
 horab=hour.split(":") ### 
 hora=horab[0]
 min=horab[1]
  
  
 hora2=duration.split(":") ###

 hora3=hora2[0]
 min2=hora2[1]
 dias=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

 horas_str=['12','1','2','3','4','5','6','7','8','9','10','11']

 try:
    day=day.lower()
    ind=dias.index(day)
 except:
    day=False

 if day != False:
    day=day.lower()
    hora=int(hora)
    min=int(min)

    hora3=int(hora3)
    min2=int(min2)
    
    horasuma=hora+hora3
    # print("suma de horas ",horasuma)
    horasuma2=((min+min2)//60)
    # print(" suma de horas en minuto ",horasuma2)
    minutore=(min+min2) %60

    diasv= round((hora+hora3+horasuma2)/24) % 7
    diasv=(ind+diasv) % 7

    day2=dias[diasv]
    day2=day2.capitalize()
    # diasn=((horasuma+horasuma2)//24)
    diasn=round((hora*1+hora3+horasuma2)/24)
    
    # print("suma de dias ",int(diasn))
    horast=(hora3+horasuma2)

    
    hpasa=(hora+horast) % 12
    hpasa2=hpasa
    hpasa=horas_str[hpasa]
    # hpasa2=horas_str[hpasa]
    # print("las horas a sumar am:",hora3+horasuma2,diasn,(horast % 12+hora),hora,hora3,hpasa2,typ)
    if (horast % 12+hora) >=12 and typ =='PM':
       # typ2='AM'
       if  hpasa2 != hora:
           typ2='AM'
       else:
         typ2=typ
       if diasn<1 :
          diasn=diasn+1
      #  hpasa2=hpasa %
    if  (horast % 12+hora) >=12 and typ =='AM':
       if  hpasa2 != hora:
           typ2='PM'
       else:
         typ2=typ
    if (horast % 12+hora) <12:
      typ2=typ    
      # hpasa2=hpasa % 12
    if minutore<10:
      minutore2='0'+str(minutore)
    else:
      minutore2=str(minutore)

    if diasn ==1:
      dnew="(next day)"

      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew+","+" "+day2+" "+dnew 
    if diasn>=2:
      dnew="("+str(diasn)+" days later)"
      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew+","+" "+day2+" "+dnew
    
    if diasn <1:
      # dnew="(next day)"

      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew+","+" "+day2 
    
 else:
    
    

    hora=int(hora)
    min=int(min)

    hora3=int(hora3)
    min2=int(min2)
    
    horasuma=hora+hora3
    
    horasuma2=((min+min2)//60)

    minutore=(min+min2) %60

    
    diasv= round((hora3+horasuma2)/24) % 7
    day2='None'
    diasn=round((hora*0+hora3+horasuma2)/24)
    horast=(hora3+horasuma2)
    # print("las horas a sumar de minutos son:",horasuma2)
    # print("las horas a sumar son:",horast)

    hpasa=(hora+horast) % 12
    hpasa2=hpasa
    hpasa=horas_str[hpasa]
    # print("las horas a sumar am:",hora3+horasuma2,diasn,(horast % 12+hora),hora,hora3,hpasa2,typ)
    # print("las horas:",(horast % 12+hora))
    if (horast % 12+hora) >=12 and typ =='PM':
       if  hpasa2 != hora:
           typ2='AM'
           diasn=diasn+1
       else:
         typ2=typ
       if diasn<=1:
          diasn=diasn
      #  hpasa2=hpasa % 12
    if (horast % 12+hora) >=12 and typ =='AM':
       if  hpasa2 != hora:
           typ2='PM'
       else:
           typ2=typ
    if (horast % 12+hora) <12:
       typ2=typ    
      # hpasa2=hpasa % 12
    if minutore<10:
       minutore2='0'+str(minutore)
    else:
      minutore2=str(minutore)

    if diasn ==1:
      dnew="(next day)"

      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew+" "+dnew 
    if diasn>=2:
      dnew="("+str(diasn)+" days later)"
      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew+" "+dnew
    
    if diasn <1:
      # dnew="(next day)"

      hnew=str(hpasa)+":"+minutore2+" "+typ2
      new_time=hnew  
    


  
 return new_time
# print(add_time("11:40 AM", "0:25")) 
# print(add_time("8:16 PM", "466:02"))
# print("6:18 AM (20 days later)")

# print( add_time("3:30 PM", "2:12", "Monday"))
# print("5:42 PM, Monday")
# print(add_time("9:15 PM", "5:30"))
# print("2:45 AM (next day)")

        #  actual = add_time("9:15 PM", "5:30")
        # expected = "2:45 AM (next day)"
    # actual = add_time("11:59 PM", "24:05")
    #     expected = "12:04 AM (2 days later)"
        # actual = add_time("8:16 PM", "466:02")
        # expected = "6:18 AM (20 days later)"
        # actual = add_time("2:59 AM", "24:00")
        # expected = "2:59 AM (next day)"
        # actual = add_time("3:30 PM", "2:12", "Monday")
        # expected = "5:42 PM, Monday"
        # actual = add_time("3:30 PM", "2:12", "Monday")
        # expected = "5:42 PM, Monday"
        # actual = add_time("8:16 PM", "466:02", "tuesday")
        # expected = "6:18 AM, Monday (20 days later)"
        # actual = add_time("2:59 AM", "24:00")
        # expected = "2:59 AM (next day)"
        # actual = add_time("11:55 AM", "3:12")
        # expected = "3:07 PM"
        #    actual = add_time("11:59 PM", "24:05")
        # expected = "12:04 AM (2 days later)"
        # actual = add_time("11:55 AM", "3:12")
        # expected = "3:07 PM"
        # actual = add_time("8:16 PM", "466:02")
        # expected = "6:18 AM (20 days later)"