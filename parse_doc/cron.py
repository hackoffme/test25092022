from parse_doc.parse import sync_db

def my_scheduled_job():
   sync_db.sync()
