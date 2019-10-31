# at_backup
 A simple python application to backup Airtable data to CSV files.
 
 Backing up Airtable data is no fun, especially if your base has multiple tables. This app allows for a simple, 
 one-button backup of all your tables within a specific base. Just run it whenever you need a backup and you're done. 
 No need to mess with the web GUI at all.
 
 It *does*, however, require some setup. You'll have to create a specially named text file for each table you want to 
 back up. Each text file must contain each field name in the given table, separated by line breaks (see sample files). 
 Also, Airtable Python Wrapper assumes you've stored your Airtable API Key as 'AIRTABLE_API_KEY' in your environment 
 variables. If not, you need to do that or set it manually elsewhere. See the 
 [docs](https://airtable-python-wrapper.readthedocs.io/en/master/authentication.html) for more info!
 
 Inside the at_backup file, you'll also need to set up some namedtuples for each table, as well as the path to your 
 backup folder.
 
 I made this for work, as we need daily backups of our Airtable base, and this saves me a lot of clicks.

 Manually creating and reading a text file to define fields may not be the most elegant solution, but so far 
 Airtable's API doesn't let you access metadata like field names. Getting "all" records doesn't return any fields that 
 are empty, which means the JSON response can be in just about any order, regardless of how fields are organized in 
 your table. That's super messy in the event you ever need to use your CSV to recreate your Airtable base. The downside, 
 of course, is that you'll have to update these text files any time you add new fields to your table.
 
 I'm considering having the namedtuple values being read out of a CSV rather than defining them directly in the
 at_backup file, but that might be overkill.
 
 Finally, huge, HUGE shoutout to [Airtable Python Wrapper](https://github.com/gtalarico/airtable-python-wrapper), 
 without which this wouldn't have been made. Definitely check it out and give it a star if you're even a little curious 
 about using the AT API with Python.



