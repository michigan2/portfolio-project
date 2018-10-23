from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')


# 1. Create blog model (per above)

# 2. Add the Blog app to the settings

# 3. Create a migration

# 4. Migrate

# 5. Add to the admin