import pymongo
import pprint
from scrapy.utils.project import get_project_settings


class MongoQueries:
    collectionName = "flipkart"

    def __init__(self):
        settings = get_project_settings()
        self.client = pymongo.MongoClient(settings.get('MONGODB_URI'))
        self.db = self.client[settings.get('MONGODB_DB')]
        self.collection = self.db[self.collectionName]

    def productCount(self):
        # How many products did you scrape?
        count = self.collection.count_documents({})
        return count

    def productWithDiscountCount(self):
        # How many products have a discount on them?
        count = self.collection.count_documents({"$expr": {"$gt": ['$original_price', '$sale_price']}})
        return count

    def topWearsWithoutDiscountCount(self):
        # How many Topwear products don't have any discount on them?
        count = self.collection.count_documents({'product_category': 'topwear',
                                                 "$expr": {"$gte": ['$sale_price', '$original_price']}
                                                 })
        return count

    def uniqueBrandsCount(self):
        # How many unique brands are present in the collection?
        count = len(self.collection.distinct('brand'))
        return count

    def discountProductCountPerBrand(self):
        # What is the count of discounted products for each brand?
        return list(self.collection.aggregate([
            {
                "$group": {
                    "_id": "$brand",
                    "count": {"$sum": 1}
                },
            },
            {
                "$match": {"$expr": {'$gt': ['$original_price', '$sale_price']}},
            },
        ]))

    def nameContainShirtCount(self):
        # How many products have shirt in their name?
        count = self.collection.count_documents({'name': {'$regex': '.*shirt.*'}})
        return count

    def offerPriceGreaterThanX(self, X):
        # How many products have offer price greater than 300?
        count = self.collection.count_documents({'sale_price': {'$gt': X}})
        return count

    def discountGreaterThanX(self, X):
        # How many products have discount % greater than 30 %?
        count = self.collection.count_documents(
            {
                "$expr": {
                    "$gt": [
                        {"$multiply": [
                            {"$divide": [{"$subtract": ["$original_price", "$sale_price"]}, "$original_price"]}, 100]},
                        X]}
            }
        )
        return count

    def categoryWithDiscountX(self, category, discount):
        # How many  footwear products have a 50% discount?
        count = self.collection.count_documents(
            {'product_category': category,
             "$expr": {
                 "$gt": [
                     {"$multiply": [
                         {"$divide": [{"$subtract": ["$original_price", "$sale_price"]}, "$original_price"]}, 100]},
                     discount]}
             }
        )
        return count

    def topSellerBrand(self):
        # Which brand in  Topwear section is selling the most number of products?
        topBrand = list(self.collection.aggregate([
            {"$match": {'product_category': 'topwear'}},
            {
                "$group": {
                    "_id": "$brand",
                    "count": {"$sum": 1}
                },
            },
            {'$sort': {'count': -1}},
            {'$limit': 1}
        ]))
        return topBrand[0]['_id']

    def close(self):
        self.client.close()


query = MongoQueries()

with open("QueryResults.txt","w") as file:
    # How many products did you scrape?
    file.write("Total Scrape: "+str(query.productCount())+"\n")

    # How many products have a discount on them?
    file.write("Total Discounted Item: "+str(query.productWithDiscountCount())+"\n")

    # How many Topwear products don't have any discount on them?
    file.write("Topwear Without Discount: "+str(query.topWearsWithoutDiscountCount())+"\n")

    # How many unique brands are present in the collection?
    file.write("Number of Unique Brands: "+str(query.uniqueBrandsCount())+"\n")

    # What is the count of discounted products for each brand?
    file.write("Discounted Products for Each Brand: "+str(query.discountProductCountPerBrand())+"\n")

    # How many products have shirt in their name?
    file.write("Products have 'Shirt' in name: "+str(query.nameContainShirtCount())+"\n")

    # How many products have offer price greater than 300?
    file.write("Num Of products with offer price > 300: "+str(query.offerPriceGreaterThanX(300))+"\n")

    # How many products have discount % greater than 30 %?
    file.write("Num Of products with discount 30: "+str(query.discountGreaterThanX(30))+"\n")

    # How many  footwear products have a 50% discount?
    file.write("Footwear with more than 50% discount: "+str(query.categoryWithDiscountX('footwear', 50))+"\n")

    # Which brand in  Topwear section is selling the most number of products?
    file.write("TopSelleing Top Wear: "+str(query.topSellerBrand())+"\n")

# Close the Connection
query.close()
