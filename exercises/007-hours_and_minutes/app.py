#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  horas= secs // 3600
  minutos= (secs % 3600) // 60

  return horas, minutos

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))