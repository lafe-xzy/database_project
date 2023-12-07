from django.db import models

# Create your models here.
'''
校区表: Campus{campus_id(char, PK), campus_name(char), location(char)}
食堂表: Cafeteria{cafeteria_id(char, PK), cafeteria_name(char), campus_id(char, FK)}
供应时间: ServedTime{served_time_id(char, PK), served_time_period(char), cafeteria_id(char, FK)}
菜品: Dish{dish_id(char, PK), dish_name(char), dish_price(int), cafeteria_id(char, FK), served_time_id(char, FK)} 
评价: Comments{comments_id(char, PK), user_name(varchar), dish_id(char, FK), score(int), content(varchar)}
'''
class Campus(models.Model):
    campus_id = models.CharField(max_length=10, primary_key=True)
    campus_name = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    
class Cafeteria(models.Model):
    cafeteria_id = models.CharField(max_length=10, primary_key=True)
    cafeteria_name = models.CharField(max_length=100)
    campus_id = models.ForeignKey(Campus, on_delete=models.CASCADE)

class ServedTime(models.Model):
    served_time_id = models.CharField(max_length=10, primary_key=True)
    served_time_period = models.CharField(max_length=100)
    # cafeteria_id = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    
class Dish(models.Model):
    dish_id = models.CharField(max_length=10, primary_key=True)
    dish_name = models.CharField(max_length=100)
    dish_price = models.FloatField()
    cafeteria_id = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    served_time_id = models.ForeignKey(ServedTime, on_delete=models.CASCADE)
    
class Comments(models.Model):
    comments_id = models.CharField(max_length=10, primary_key=True)
    # username_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    score = models.FloatField()
    content = models.CharField(max_length=200)
    