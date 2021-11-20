from django.db import models

class Board(models.Model):
    description = models.TextField(null= True, blank= True)
    title = models.CharField(null= True, blank= True, max_length= 100 )
    privacy = models.BooleanField(default= False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class User(models.Model):
    first_name = models.CharField(max_length= 50 )
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    avatar = models.ImageField(upload_to= '', null= True, blank= True)
    followers = models.ManyToManyField(
        to='self',
        related_name='followees',
        symmetrical=False
    )
    friends = models.ManyToManyField('User', blank= True)



class Pin(models.Model):
    title = models.CharField(max_length= 100 )
    alt_txt = models.CharField(max_length= 500, null= True, blank= True )
    description = models.TextField(null=True, blank=True)
    destination_link = models.URLField(null=True, blank=True)
    type = models.CharField(max_length= 10, choices= [('image', 'video')], default= 'image' )
    url = models.ImageField(upload_to= '')
    boards = models.ManyToManyField(Board, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class freind_request(models.Model):
    from_user = models.ForeignKey('User', related_name= 'from_user', on_delete= models.CASCADE)
    to_user = models.ForeignKey('User', related_name= 'to_user', on_delete= models.CASCADE)

class Room(models.Model):
    subscribers = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length= 100)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField(null= True, blank= True)
    message_date = models.DateTimeField(auto_now_add= True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    notification_date = models.DateTimeField(auto_now_add=True)

class pin_tags(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    tag = models.CharField(max_length= 100 )