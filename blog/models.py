from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Registration(models.Model):
    person = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    event = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)


    def __str__(self):
        return f"{self.person} - {self.event}"
class Record(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')])
    
    class Meta:
        unique_together = ('email', 'status')  # Example duplication check
def is_duplicate(row):
    return Record.objects.filter(email=row['email']).exists()
class Record(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(
        max_length=10,
        choices=[('draft', 'Draft'), ('published', 'Published')],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('email', 'status')  # Prevent duplicate emails per status
class Instructor(models.Model):
    instructor_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentRecord(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('email', 'course', 'status')  # Prevent duplicate entries per course/status