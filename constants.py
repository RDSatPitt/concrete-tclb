import dotenv
import os

dotenv.load_dotenv()

PARCELS_PATH = os.environ.get("PARCELS_PATH")
ASSESSMENTS_PATH = os.environ.get("ASSESSMENTS_PATH")
TRICOG_PATH = os.environ.get("TRICOG_PATH")
LIENS_PATH = os.environ.get("LIENS_PATH")
TRICOG_OVER_PARCELS_IMG_PATH = os.environ.get("TRICOG_OVER_PARCELS_IMG_PATH")
ALL_PARCELS_IMG_PATH = os.environ.get("ALL_PARCELS_IMG_PATH")
OAKLAND_PARCELS_IMG_PATH = os.environ.get("OAKLAND_PARCELS_IMG_PATH")
CLIPPED_PARCELS_IMG_PATH = os.environ.get("CLIPPED_PARCELS_IMG_PATH")

opening_greeting = f"""Hello! Glad to have you on board, because I can really use your help. We're excited to move forward with our goal of buying abandoned houses and converting them to affordable houses. 

I'm going to give you a file that has every parcel in Allegheny County, and I want you to tell me which parcels we should consider buying. The list can be as long as you think is appropriate as long as the parcels meet three rules: 

1. The parcels are within our boundaries. 
2. The parcels have single-family houses on them. 
3. The parcels are tax delinquent. 

I know I'm throwing a lot at you, so feel free to ask for help. You can ask for information about those three rules, about key vocabulary terms, or about the important concepts you'll learn by helping me out. 

Simply type **guidelines**, **vocabulary**, **concepts** or **files** to learn more about those topics. You can always type **help** if you need a reminder of this information, and you can also type **done** if you're finished and ready to start working."""
vocab_response = f"""Here's a list of field-specific words I can help you with. 

"**Land Bank**"

"**Parcel**"

"**Polygon**"

"**Multipolygon**"

"**Tax Delinquency**"

"**Liens**"

If you type in any of those words, I can tell you what they mean. You can also type "**help**" and I'll repeat the different ways I can help. Or you can type "**Done**" if you're ready to start working!
"""

land_bank_response = f"""A land bank is a special organization created by state and local laws to generate affordable housing in a community. Land Banks typically get special permission to purchase abandonded properties and sell them to individuals in the community for below market rates."""
parcels_response = f"""Parcels are the smallest distinct units of land in a municipality. For these purposes, it may help to think of a parcel as what a homeowner would call their "property" -- you don't usually think about just their house, but also their yard, their driveway, or whatever else is inside their "property". That said, all sorts of land can be a parcel: city parks are parcels, the buildings at school sit on parcels, warehouses and hospitals are on parcels too."""
polygon_response = f"""In GIS terms, polygons are one of three vector features that can be represented on a map (along with points and lines). Polygons have at least three lines that form the border of a shape (much like polygons in the context of geometry). Typically, parcels in a town are polygons."""
multipolygon_response = f"""Multipolygons are multiple polygons that, together, represent a singular entity. The US map would be represented as a multipolygon (with its 48 connected states, Alaska, Hawaii, and other territories)."""
tax_delinquency_response = f"""If you have not paid your taxes on time, you are said to be tax delinquent. If you eventually do pay your taxes, you can exit tax delinquency (in other words, 'tax delinquency' is not a permanent state or label)."""
lien_response = f"""A penalty assigned to someone who is tax delinquent. Liens are debts that are attached to properties or other large-value possessions. If you have a lien on your house and you sell it, the lien has to be paid off before you receive money from the sale."""
concept_response = f"""After completing this project, you will have: \n\n1. been introduced to geospatial file types, and ways to open the files\n\n2. be introduced to geopandas and compare that library\n\n3. be introduced to GIS processing techniques such as 'clip'\n\n4. consider the human context behind data"""
rules_response = f"""When you create your final list of parcels, every parcel must meet these three rules:\n\n1. They must all be within TriCOG's boundaries\n\n2. They must be residential properties with single-family homes\n\n3. They must be abandoned.\n\nWhich would you like to know more about? Type **1**, **2**, or **3**."""
one_response = f"""**Boundaries**: The TriCOG Land Bank operates within legally-defined borders. Any houses or parcels we purchase have to be within those borders. One of the files I give you will be a map that shows exactly where those borders are."""
two_response = f"""**Residential Properties**: Properties are classified by how they're used: if they're for living, they're residential. If they're for businesses, they're commercial. There are several other different classifications, and parcels of all different types will be on the list I give you. You just need to make sure that any you select are residential."""
three_response = f"""**Abandoned Homes**: There's no document that lists abandoned homes in the county. But we can use tax liens as a proxy -- if someone has stopped paying their taxes, it may be because they've abandoned the house. I have a file with liens I can give you that'll tell you which houses have liens on them."""
files_response = f"""I'm giving you four files that you'll need to use to complete the project: **`liens.csv`**, **`assessments.csv`**, **`parcels.geojson`**, and **`tricog.geojson`**. You can type in the name of any of those files (with the extension) if you want more information."""
liens_csv_response = f"""**`liens.csv`** is a file that lists every parcel in Allegheny County that currently has liens against it."""
assessments_response = f"""**`assessments.csv`** is a file that has descriptive data about every parcel in the county. This can tell us which parcels have houses or businesses or parks (among other details) without having to drive and look at them."""
parcels_geojson_response = f"""**`parcels.geojson`** is a file that contains data on the shape and size of every parcel in the county."""
help_response = f"""I can provide more information about the **guidelines** for your task, the **concepts** you'll learn by doing it, the **vocabulary** specific to the field, the **files** needed to perform the task. If you're ready to begin, you can type **done**."""
tricog_response = f"""**`tricog.geojson`** contains the shape of the TriCOG land bank's operating boundaries. By law, our business efforts have to stay within these boundaries."""
done_response = f"""Great! The files you'll need should be loading shortly, along with some notes about how to use them. Good luck!"""

response_dict = {'vocab': vocab_response,
                 'land bank': land_bank_response,
                 'parcel': parcels_response,
                 'polygon': polygon_response,
                 'multi': multipolygon_response,
                 'tax delinquen': tax_delinquency_response,
                 'lien': lien_response,
                 'concepts': concept_response,
                 'guidelines': rules_response,
                 '1': one_response,
                 '2': two_response,
                 '3': three_response,
                 'help': help_response,
                 'files': files_response,
                 'done': done_response,
                 'liens_file': liens_csv_response,
                 'parcels_geojson': parcels_geojson_response,
                 'tricog': tricog_response,
                 'assessments': assessments_response,
                 }