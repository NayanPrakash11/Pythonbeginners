"""Time and Date examples"""
import time

#weekday
print(time.strftime("%a"))

#month
print(time.strftime("%b"))

#hours and minutes
print(time.strftime("%H%M"))

#rectified time
print(time.strftime("%H:%M"))

#Month long
print(time.strftime("%B"))

""" messure time """

""" start time fo inlogin """
start_time=time.time()

"""inlog"""
name=input("Enter login name ")

""" end time fo inlog"""

end_time=time.time()-start_time

print("Welcome ", name, "\n")
print("User : ", name, "logged in at", time.strftime("%H:%M"))
print("Inlog took :", end_time)


