
import os
from datetime import datetime
import time
from django.test import TestCase

# Create your tests here.
date = "9950-1-12"
b=datetime.strptime(date, "%Y-%m-%d").date()
print(b)
c= b.strftime("%Y")
print(c)