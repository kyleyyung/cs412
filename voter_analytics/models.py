from django.db import models
import datetime

# Create your models here.

class Voter(models.Model):
    '''
    Store/represent the data from one runner at the Chicago Marathon 2023.
    BIB,First Name,Last Name,CTZ,City,State,Gender,Division,
    Place Overall,Place Gender,Place Division,Start TOD,Finish TOD,Finish,HALF1,HALF2
    '''
    # identification
    last_name = models.TextField()
    first_name = models.TextField()
    street_number = models.IntegerField()
    street_name = models.TextField()
    apartment_number = models.TextField()
    zipcode = models.IntegerField()
    dob = models.DateField()
    dor = models.DateField()
    party = models.TextField()
    precinct = models.IntegerField()
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.street_number}, {self.street_name}, {self.zipcode}), {self.party} {self.score}'
    
def load_data():
    '''Function to load data records from CSV file into Django model instances.'''
    # delete existing records to prevent duplicates:
    Voter.objects.all().delete()
    
    filename = '/Users/kyleyung/Desktop/newton_voters.csv'
    f = open(filename)
    f.readline() # discard headers
    # for row in range(5):
        # line = f.readline().strip()
    for line in f:
        try:
            fields = line.split(',')
            # create a new instance of Result object with this record from CSV
            result = Voter(last_name=fields[1],
                            first_name=fields[2],
                            street_number = fields[3],
                            street_name = fields[4],
                            apartment_number = fields[5],
                            zipcode = fields[6],
                            dob = datetime.datetime.strptime(fields[7], '%Y-%m-%d').date(),
                            dor = datetime.datetime.strptime(fields[8], '%Y-%m-%d').date(),
                            party = fields[9].strip(),
                            precinct = fields[10],
                            v20state = fields[11],
                            v21town = fields[12],
                            v21primary = fields[13],
                            v22general = fields[14],
                            v23town = fields[15],
                            score = fields[16].strip(),
                        )
            result.save() # commit to database
            print(f'Created result: {result}')
            
        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Voter.objects.all())} Results.')