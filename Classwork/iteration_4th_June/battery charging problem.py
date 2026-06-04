#a mobile phone is charging.The bttery level starts at 20% and increases by 10% every charging cycle.
#by 10% every charging cycle.
# Wap that displays the battery percentage after each cycle and continues until the battery reaches 100%
charging_level=20
electricity_status=True 
while charging_level<=100:
    if electricity_status:
     print("Battery level: ",charging_level,"%")
     charging_level+=10
    else:
       break
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Battery is fully charged.")