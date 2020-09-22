import excel
import mongoconsts as mg # Ignored in git for security reasons
import mongodb
import scraper

if __name__ == "__main__":
    database = mongodb.UniversityMongoDB(mg.MONGO_URI, mg.DATABASE_NAME, mg.COLLECTION_NAME)
    schools_already_in_database = database.get_school_names()
    all_results = scraper.run_from_file("schools.txt", schools_already_in_database)
    if len(all_results) > 0:
        database.insert_mutiple(all_results)
    excel.create_csv(database.find_by_query({}, {"_id": 0}))