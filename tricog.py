import marimo

__generated_with = "0.14.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import geopandas as gp
    import pandas as pd
    import csv
    import matplotlib.pyplot as plt
    import asyncio
    import time

    from constants import (
        PARCELS_PATH,
        ASSESSMENTS_PATH,
        TRICOG_PATH,
        LIENS_PATH,
        ALL_PARCELS_IMG_PATH,
        CLIPPED_PARCELS_IMG_PATH,
        OAKLAND_PARCELS_IMG_PATH,
        TRICOG_OVER_PARCELS_IMG_PATH,
        response_dict,
        opening_greeting,
    )

    return (
        ALL_PARCELS_IMG_PATH,
        ASSESSMENTS_PATH,
        CLIPPED_PARCELS_IMG_PATH,
        LIENS_PATH,
        OAKLAND_PARCELS_IMG_PATH,
        PARCELS_PATH,
        TRICOG_OVER_PARCELS_IMG_PATH,
        TRICOG_PATH,
        gp,
        mo,
        pd,
        time,
    )


@app.cell
def _(mo):
    # prologue buttons
    begin_button = mo.ui.run_button(label="Ready to Begin?")
    moving_on = mo.ui.run_button(label="Moving on...")
    read_files_button = mo.ui.run_button(label="Read In Files")

    # user text entry boxes
    join_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_text_box_one = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_text_box_two = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_text_box_three = mo.ui.text_area(full_width=True).form(clear_on_submit=True)
    residential_text_box_one = mo.ui.text(full_width=True).form(clear_on_submit=True)
    residential_text_box_two = mo.ui.text(full_width=True).form(clear_on_submit=True)
    residential_text_box_three = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_one = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_two = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_two_a = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_three = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_four = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_five = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_box_six = mo.ui.text(full_width=True).form(clear_on_submit=True)

    parcels_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    combining_data_text_box_one = mo.ui.text(full_width=True).form(clear_on_submit=True)
    combining_data_text_box_two = mo.ui.text(full_width=True).form(clear_on_submit=True)


    # instantiating seperate buttons to use at different stages while avoiding conflicts
    tricog_button = mo.ui.run_button(label="Find Parcels Within TriCOG")
    tricog_button_2 = mo.ui.run_button(label="Find Parcels Within TriCOG")
    tricog_button_3 = mo.ui.run_button(label="Find Parcels Within TriCOG")

    residential_button = mo.ui.run_button(label="Find Residential Parcels")

    abandoned_button = mo.ui.run_button(label="Find Abandoned Parcels")

    return (parcels_text_box,)


@app.cell
def _(mo):
    # global state

    # tracks state of which steps the user took
    get_launch_tasks, set_launch_tasks = mo.state(False)

    get_iteration_move_along, set_iteration_move_along = mo.state(False)

    get_parcels_display, set_parcels_display = mo.state(False)
    get_combined_data_step_one, set_combined_data_step_one = mo.state(False)
    get_combined_data_step_two, set_combined_data_step_two = mo.state(False)
    return


@app.function
def strip_string(unstripped: str):
    return unstripped.replace('"','').replace(' ','').replace("'","").replace("\n","").replace('`','').replace('&nbsp;','').lower()


@app.cell
def _(mo):
    mo.md(text="#TriCOG Land Bank Scenario").center()
    return


@app.cell
def _(mo):
    mo.md(r"""Congratulations on your new role with TriCOG Land Bank! You have been hired to assist their GIS and Data Analyst. Your task is to help the analyst identify homes that the Land Bank can purchase and make available as affordable housing. Please click the buttons below for more information, or proceed to the **`Reading Files`** section to begin.""")
    return


@app.cell
def _(mo):
    # File reading prep

    # expected values
    assessments_file_expected_code = 'assessments_df = pd.read_csv(ASSESSMENTS_PATH)'
    liens_file_expected_code = 'liens_df = pd.read_csv(LIENS_PATH)'
    parcels_file_expected_code = 'parcels_df = gp.read_file(PARCELS_PATH)'
    tricog_file_expected_code = 'tricog_df = gp.read_file(TRICOG_PATH)'


    # ui elements
    assessments_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    liens_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_geojson_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_explore_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    intro_objective_button = mo.ui.run_button(label = "Objective")
    intro_vocab_button = mo.ui.run_button(label = "Key Terms")
    intro_files_button = mo.ui.run_button(label = "Provided Files")
    intro_concepts_button = mo.ui.run_button(label = "Educational Concepts")

    return (
        assessments_file_expected_code,
        assessments_text_box,
        intro_concepts_button,
        intro_files_button,
        intro_objective_button,
        intro_vocab_button,
        liens_file_expected_code,
        liens_text_box,
        parcels_file_expected_code,
        tricog_explore_text_box,
        tricog_file_expected_code,
        tricog_text_geojson_box,
    )


@app.cell
def _(
    intro_concepts_button,
    intro_files_button,
    intro_objective_button,
    intro_vocab_button,
    mo,
):
    mo.hstack([intro_objective_button, intro_vocab_button, intro_files_button, intro_concepts_button], justify='space-around')
    return


@app.cell
def _(
    intro_concepts_button,
    intro_files_button,
    intro_objective_button,
    intro_vocab_button,
    mo,
):
    if intro_objective_button.value:
        mo.output.replace(
            mo.md(f"""<br>You will be given four data files. Using them, you will generate an output file that lists parcels that the TriCOG Land Bank should consider buying. The list can be any length, but regardless of size, each parcel must meet three standards: <br><br>1. They must all be within TriCOG's boundaries<br><br>2. They must be residential properties with single-family homes<br><br>3. They must be abandoned.<br><br>""")
        )
    elif intro_vocab_button.value:
        mo.output.replace(
            mo.md(f"""<br>"**Land Bank**": A land bank is a special organization created by state and local laws to generate affordable housing in a community. Land Banks typically get special permission to purchase abandonded properties and sell them to individuals in the community for below market rates.

    "**Parcel**": Parcels are the smallest distinct units of land in a municipality. For these purposes, it may help to think of a parcel as what a homeowner would call their "property" -- you don't usually think about just their house, but also their yard, their driveway, or whatever else is inside their "property". That said, all sorts of land can be a parcel: city parks are parcels, the buildings at school sit on parcels, warehouses and hospitals are on parcels too.

    "**Polygon**": Parcels are the smallest distinct units of land in a municipality. For these purposes, it may help to think of a parcel as what a homeowner would call their "property" -- you don't usually think about just their house, but also their yard, their driveway, or whatever else is inside their "property". That said, all sorts of land can be a parcel: city parks are parcels, the buildings at school sit on parcels, warehouses and hospitals are on parcels too.

    "**Multipolygon**": Multipolygons are multiple polygons that, together, represent a singular entity. The US map would be represented as a multipolygon (with its 48 connected states, Alaska, Hawaii, and other territories).

    "**Tax Delinquency**": If you have not paid your taxes on time, you are said to be tax delinquent. If you eventually do pay your taxes, you can exit tax delinquency (in other words, 'tax delinquency' is not a permanent state or label).

    "**Liens**": A penalty assigned to someone who is tax delinquent. Liens are debts that are attached to properties or other large-value possessions. If you have a lien on your house and you sell it, the lien has to be paid off before you receive money from the sale.""")
        )
    elif intro_concepts_button.value: 
        mo.output.replace(
            mo.md(f"""<br>After completing this project, you will have:
        
            1. been introduced to geospatial file types, and ways to open the files
        
            2. been introduced to geopandas and compare that library's functionality to pandas
        
            3. been introduced to GIS processing techniques such as 'clip'
        
            4. considered the human context behind data""")
        )
    elif intro_files_button.value:
        mo.output.replace(
            mo.md(f"""<br>You will be given four files to complete the project: 
        
            **`assessments.csv`** contains descriptive data about every parcel in the county. This can tell us which parcels have houses or businesses or parks (among other details) without having to drive and look at them. 
        
            **`liens.csv`** lists every parcel in Allegheny County that currently has liens against it
        
            **`tricog.geojson`** contains the shape of the TriCOG land bank's operating boundaries. By law, TriCOG's business efforts have to stay within these boundaries
        
            **`parcels.geojson`** contains data on the shape and size of every parcel in the county.
            """)
        )

    return


@app.cell
def _(
    ASSESSMENTS_PATH,
    assessments_file_expected_code,
    assessments_text_box,
    mo,
    pd,
):
    # Instructions on how to read assessments file
    assessments_code_entry = None
    assessments_df = None
    mo.output.replace(
        mo.vstack([
            mo.md(f"""#Reading In Files""").center(),
            mo.md(f"""To begin your work, you'll need to read in four files:<br>
            1. **assessments.csv**<br>
            2. **liens.csv**<br>
            3. **tricog.geojson**<br>
            4. **parcels.geojson**<br>"""),
            mo.md(f"""Reading in `csv` files is a fairly straightforward process, thanks to the `pandas` library. You can read in the files using pandas' `read_csv()` function.<br>
            In the function's simplest form, all you need is the location of the file. Try and run it now: type the following line of code into the text box below and hit 'submit'. (In this code, `ASSESSMENTS_PATH` is a variable that represents the location of `assessments.csv` on your computer.) <br>
            `{assessments_file_expected_code}`"""),
            assessments_text_box,
        ])
    )
    # capture input
    assessments_code_entry = assessments_text_box.value


    # check input
    if assessments_code_entry:
        if strip_string(assessments_file_expected_code) == strip_string(assessments_code_entry):
            with mo.status.spinner(
                title="Reading in 'assessments_df.csv'",
                subtitle="Please be patient, this may take a minute"
            ) as _spinner:
                    assessments_df = pd.read_csv(ASSESSMENTS_PATH, low_memory=False)
                    mo.output.replace_at_index("Correct!", 1)
        else:
            mo.output.append('Not quite...  Try again.')

    return (assessments_df,)


@app.cell
def _(assessments_df, mo):
    # wait for assessments dataframe to be created (i.e. correct input from user)
    mo.stop(assessments_df is None)

    #
    mo.output.replace(mo.vstack(
        [
            mo.md(f"""##assessments.csv"""),
            assessments_df,
            mo.md(f"""<br>The dataframe above is the `assessments.csv` file that was just read in. Notice that it has 86 columns and over 584,000 rows. This is a large file! Also notice the column on the far left is a column named `PARID`. This is the parcel identification number. That means that every row contains data about a different parcel. Finally, it's important to note that this file does not have any geospatial data in it; the contents are entirely descriptive.<br>""")
        ]
    ))
    return


@app.cell
def _(
    LIENS_PATH,
    assessments_df,
    liens_file_expected_code,
    liens_text_box,
    mo,
    pd,
):
    # Read in liens.csv file
    mo.stop(assessments_df is None)

    mo.output.replace(mo.vstack(
        [
            mo.md(f"""Let's read in the other csv file, `liens.csv`. The process is very much the same; just enter the code into the text box and hit submit.<br>`{liens_file_expected_code}`"""),
            liens_text_box,
        ]
    ))

    liens_code_entry = liens_text_box.value

    liens_df = None
    if liens_code_entry:
        if strip_string(liens_file_expected_code) == strip_string(liens_code_entry):
            with mo.status.spinner(
                title="Reading in 'liens.csv'",
                subtitle="This should be a bit quicker, thankfully"
            ) as _spinner:
                liens_df = pd.read_csv(LIENS_PATH)
                mo.output.replace_at_index("Correct!", 1)
        else:
            mo.output.append('Not quite...  Try again.')
    return (liens_df,)


@app.cell
def _(liens_df, mo):
    # wait for correct user input (i.e. the datafram get's instantiated)
    mo.stop(liens_df is None)

    mo.output.replace(    
        mo.vstack(
            [
                mo.md(f"""##liens.csv"""),
                liens_df,
                mo.md(f"""<br>`liens.csv` is a dataset that contains information about properties that have liens against them. You'll notice that this file also has a new parcel ID for each row, only in this file the column is labeled 'pin' (instead of 'PARID'). The three columns of note are the parcel ID, the number of liens a property has, and the total amount of money owed.""")
            ]
        )
    )
    return


@app.cell
def _(
    TRICOG_PATH,
    gp,
    liens_df,
    mo,
    tricog_file_expected_code,
    tricog_text_geojson_box,
):
    mo.stop(liens_df is None)

    tricog_code_entry = tricog_text_geojson_box.value
    tricog_df = None

    mo.output.replace(
        mo.vstack([
            mo.md(
                f"""The next file is not a .csv file: it's a .geojson file. Unfortunately, pandas does not have a `read_geojson()` function. This is where `geopandas` comes in! `Geopandas` is a python library that adds geospatial support to pandas objects. `Geopandas` has a similarly easy function for reading in files: `read_file()`. Let's try and use it! Type the following code into the text box and hit submit.<br><br>`{tricog_file_expected_code}`"""
            ),
            tricog_text_geojson_box
        ])
    )


    if tricog_code_entry: 
        if strip_string(tricog_file_expected_code) == strip_string(tricog_code_entry):
            with mo.status.spinner(
                title="Reading in 'tricog_df.geojson'",
                subtitle="Please be patient, this may take a minute"
            ) as _spinner:
                tricog_df = gp.read_file(TRICOG_PATH)
                mo.output.replace_at_index("Correct!", 1)
        else:
            mo.output.append('Not quite... Try again.')
    return (tricog_df,)


@app.cell
def _(mo, pd, tricog_df, tricog_explore_text_box):
    def handle_tricog(tricog):
        """convert ot plain ol' dataframe for display purposes """
        if tricog is not None:
            return pd.DataFrame(tricog.astype({'geometry':'str'}))
        else: 
            return None

    # wait for correct user input (i.e. the dataframe get's instantiated)
    mo.stop(tricog_df is None)

    exploration = None

    mo.output.replace(
        mo.vstack([
            mo.md(f"""##tricog.geojson"""),
            handle_tricog(tricog_df),
            mo.md(f"""Unlike the other files we've looked at so far, `tricog.geojson` isn't organized at the parcel level. Instead, each row of this file represents a different municipality that is a member of the TriCOG land bank. Also unlike the other files, `tricog.geojson` has a column at the far right called 'geometry' that contains the shape of each municipality.<br><br>
        Because this shape data is contained in the file, geopandas lets us do neat things like visualizing the content. Watch what happens when you enter the following line of code into the textbox.<br><br>
        `tricog_df.explore()`"""),
            tricog_explore_text_box
            ]
        )
    )
    explore_code_entry = tricog_explore_text_box.value

    if explore_code_entry:
        if explore_code_entry == 'tricog_df.explore()':
            exploration = tricog_df.explore(height='90%')
            mo.output.replace_at_index("Correct!", 1)
        else:
            mo.output.append(mo.md('Try again.'))

    return exploration, handle_tricog


@app.cell
def _(exploration, mo):
    # wait for correct input
    mo.stop(exploration is None)

    mo.output.replace(
        mo.vstack(
            [
                mo.md(f"""##tricog.explore()"""), 
                exploration, 
                mo.md(f"""Here, we see the various municipalities in which TriCOG operates. If you hover your mouse over any of the shaded areas, a pop-up will display the rest of the data that we saw in the dataframe.""",)
            ]
        )
    )
    return


@app.cell
def _(
    PARCELS_PATH,
    exploration,
    gp,
    mo,
    parcels_file_expected_code,
    parcels_text_box,
):
    mo.stop(exploration is None)

    mo.output.replace(
        mo.vstack([
        mo.md(f"""Finally, let's read in our last file: parcels.geojson. Since this file is also a GeoJSON file, we'll once again use geopandas' `read_file()` function. Type out the following text and hit submit: <br><br>
        `{parcels_file_expected_code}`"""), 
                parcels_text_box
        ])
    )

    parcel_code_entry = parcels_text_box.value
    parcels_df = None
    if parcel_code_entry: 
        if strip_string(parcels_file_expected_code) == strip_string(parcel_code_entry):
            with mo.status.spinner(
                title="Reading in 'parcels.geojson'",
                subtitle="Please be patient, this may take a minute"
            ) as _spinner:
                parcels_df = gp.read_file(PARCELS_PATH)
                mo.output.replace_at_index('Great!',1)
        else:
            mo.output.append("Try again.")
    return (parcels_df,)


@app.cell
def _(
    ALL_PARCELS_IMG_PATH,
    OAKLAND_PARCELS_IMG_PATH,
    finished_with_files_button,
    mo,
    parcels_df,
    pd,
):

    mo.stop(parcels_df is None)

    view_analyses = False

    mo.output.replace(
        mo.vstack(
            [
                mo.md(f"""##parcels.geojson"""),
                pd.DataFrame(parcels_df),
                mo.md(f"""Here we see the parcels.geojson dataframe. Unfortunately, the file is too large to use the explore function: doing so would likely make your browser crash. That said, if you load  the file into GIS software, it looks like this: <br><br>"""),
                mo.image(ALL_PARCELS_IMG_PATH),
                mo.md(f"""Because there are so many parcels, it's difficult to make them all out at this distance. Here is a zoomed in picture of the parcels in Oakland, with the parcel that holds the Cathedral of Learning highlighted on the right side of the image."""),
                mo.image(OAKLAND_PARCELS_IMG_PATH),
                mo.md(f"""Scrolling up to look at the dataframe, we can see that it is organized at the level of the parcel (with the column 'PIN' providing the parcels' ID numbers. If you scroll to the right, you can see that this file also has a geometry column.<br><br>

                You can feel free to investigate these datasets more, but if you're ready to get started on your tasks, click the button below<br><br>"""),
                finished_with_files_button.center(),
            ]
        )
    )
    if finished_with_files_button.value:
        view_analyses = True
    return (view_analyses,)


@app.cell
def _(mo):
    get_tricog_text_path_cell_one, set_tricog_text_path_cell_one = mo.state(False)
    get_tricog_geo_path_cell_one, set_tricog_geo_path_cell_one = mo.state(False)

    return (
        get_tricog_geo_path_cell_one,
        get_tricog_text_path_cell_one,
        set_tricog_geo_path_cell_one,
        set_tricog_text_path_cell_one,
    )


@app.cell
def _(
    assessments_df,
    mo,
    set_tricog_geo_path_cell_one,
    set_tricog_text_path_cell_one,
):
    # Analysis prep
    finished_with_files_button = mo.ui.run_button(label="Start Analysis")
    # text_analysis_button = mo.ui.run_button(label="Use Text Analysis")
    # geospatial_button = mo.ui.run_button(label="Use Geospatial Analysis")

    def handle_tricog_path_selection(value):   
        if (value == "TEXT"):
            set_tricog_text_path_cell_one(True)
            set_tricog_geo_path_cell_one(False)
            return "TEXT"
        if (value == "GEO"):
            set_tricog_text_path_cell_one(False)
            set_tricog_geo_path_cell_one(True)
            return "GEO"


    text_analysis_btn = mo.ui.button(label="Use Text Analysis", value="TEXT", on_click=handle_tricog_path_selection)

    geo_analysis_btn = mo.ui.button(label="Use Geospatial Analysis", value="GEO", on_click=handle_tricog_path_selection)

    #text input correct answers
    tricog_municipality_name_expected_code = "tclb_municipalities = list(tricog.NAME)"
    countywide_municipality_name_list = 'munidesc = list(set(assessments.MUNIDESC))'
    countywide_municipality_name_list_sorted = 'munidesc.sort()'
    countywide_municipality_name_list_sorted_printed = 'print(munidesc[:20])'
    clip_function_code = 'clipped_parcels = gp.clip(parcels, tricog)'
    clip_function_parcel_length_code = "f'length of parcels: {len(parcels)}'"
    clip_function_clip_output_length_code = "f'length of clipped_parcels: {len(clipped_parcels)}'"


    #text entry boxes
    tricog_municipality_name_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_path_box_countywide_muni_name_list = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_path_box_countywide_muni_name_list_sorted = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_text_path_box_countywide_muni_name_list_sorted_printed = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_geo_path_text_box_clip_function = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_geo_path_clip_function_parcel_length = mo.ui.text(full_width=True).form(clear_on_submit=True)
    tricog_geo_path_clip_function_clip_output_length = mo.ui.text(full_width=True).form(clear_on_submit=True)


    #other
    if assessments_df is not None:
        munis = list(set(assessments_df.MUNIDESC))
        munis.sort()
        list_of_sorted_munis = munis[:20]

    return (
        clip_function_clip_output_length_code,
        clip_function_code,
        clip_function_parcel_length_code,
        countywide_municipality_name_list,
        countywide_municipality_name_list_sorted,
        countywide_municipality_name_list_sorted_printed,
        finished_with_files_button,
        geo_analysis_btn,
        munis,
        text_analysis_btn,
        tricog_geo_path_clip_function_clip_output_length,
        tricog_geo_path_clip_function_parcel_length,
        tricog_geo_path_text_box_clip_function,
        tricog_municipality_name_expected_code,
        tricog_municipality_name_text_box,
        tricog_text_path_box_countywide_muni_name_list,
        tricog_text_path_box_countywide_muni_name_list_sorted,
        tricog_text_path_box_countywide_muni_name_list_sorted_printed,
    )


@app.cell
def _(geo_analysis_btn, mo, text_analysis_btn, view_analyses):
    mo.stop(not view_analyses)

    tricog_intro_output = mo.vstack(
        [
            mo.md(f"""###Finding Parcels Within TriCOG's Boundaries"""), 
            mo.md("""
    One of the three steps we need to take is to isolate parcels that are within TriCOG's operating boundaries. This step is important because state law only allows TriCOG to operate within a certain boundary, so it is crucial that the properties included on your final list be within those boundaries. 

    In order to achieve this goal, we'll need to know what the TriCOG boundaries are, and what parcels are inside them. `tricog_boundaries.shp`, which we loaded in the last step, has the data we'll need for TriCOG's boundaries. 

    There are two files we've loaded that have county-wide parcel data: <br> 1. **parcels.geojson** includes geospatial data, and<br> 2. **assessments.csv** provides text data about the parcels. <br>If we want to try and parse text to get the answer, we can use `assessments.csv`. If we want to perform a geospatial analysis, we can use `parcels.geojson`.  

    So: should we start with a text analysis, or should we use a geospatial analysis?
    """), 
            mo.hstack([text_analysis_btn,geo_analysis_btn],
            justify='space-around')
        ]
    )

    mo.output.replace(tricog_intro_output)
    return


@app.cell(hide_code=True)
def tricog_path_cell_1(
    TRICOG_OVER_PARCELS_IMG_PATH,
    clip_function_code,
    get_tricog_geo_path_cell_one,
    get_tricog_text_path_cell_one,
    gp,
    handle_tricog,
    mo,
    parcels_df,
    tricog_df,
    tricog_geo_path_text_box_clip_function,
    tricog_municipality_name_expected_code,
    tricog_municipality_name_text_box,
):
    #tricog path, text choice, cell 1
    tricog_text_path_cell_one = get_tricog_text_path_cell_one()
    tricog_geo_path_cell_one = get_tricog_geo_path_cell_one()

    mo.stop(not tricog_text_path_cell_one and not tricog_geo_path_cell_one)
    tricog_text_path_cell_two = False
    tricog_geo_path_cell_two = False 

    # text analysis path
    if tricog_text_path_cell_one: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""##Text Analysis"""),
                    mo.md(f"""Let's take a look at the TriCOG boundaries again: """),
                    handle_tricog(tricog_df),
                    mo.md(f"""As you can see in the above, there is a column named "NAME" that contains the names of the municipalities included in their operating boundaries.

                    We can isolate these names as a list and then compare them to the municipality names found in the assessments file that was introduced above.

                    Type the following code into the text entry box as it appears and hit 'Submit'<br>
                    `{tricog_municipality_name_expected_code}`"""),
                    tricog_municipality_name_text_box,                
                ]
            )
        )
        tricog_muni_user_text_entry = tricog_municipality_name_text_box.value
        if tricog_muni_user_text_entry: 
            if tricog_muni_user_text_entry == tricog_municipality_name_expected_code:
                mo.output.replace_at_index("Correct!", 1)
                tricog_text_path_cell_two = True
            else: 
                mo.output.append("Try again")

    # geo analysis path
    elif tricog_geo_path_cell_one: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""###Geospatial Analysis"""),
                    mo.md(f"""An alternate method to find the parcels we're looking for is to use the geopandas `clip` function.   `Clip` is a common feature across GIS programs that "clips" a GIS file within a boundary provided by a second file. You can think of the two files like a cookie cutter and cookie dough; the `clip` function returns only the features (dough) that fell within the second file's boundaries (cookie cutter)."""),
                    mo.md(f"""The image below shows the TriCOG's operating boundaries laid over all of the parcels within Allegheny County. Using `clip` will return a geopandas dataframe that only contains the parcels within that border."""), 
                    mo.image(TRICOG_OVER_PARCELS_IMG_PATH, width=1265 * .5, height=838 * .5).center(),
                    mo.md(f"""Let's try to use `clip` and see what happens.<br><br>
                    Enter the following code snippet in the box below to run 'clip': """),
                    mo.md(text=f"""`{clip_function_code}`"""),
                    tricog_geo_path_text_box_clip_function
                ]
            )
        )

        if tricog_geo_path_text_box_clip_function.value: 
            if tricog_geo_path_text_box_clip_function.value == clip_function_code: 
                mo.output.replace_at_index("Correct!", 1)
                with mo.status.spinner(
                    title="Performing your requested clip",
                    subtitle="Please be patient, this may take a minute"
            ) as _spinner:
                    clipped_parcels = gp.clip(parcels_df, tricog_df)
                    mo.output.replace_at_index("Correct!", 1)
                    tricog_geo_path_cell_two = True
                    tricog_text_path_cell_two = False
            else: 
                mo.output.append("Try again!")
    else: 
        mo.output.clear()
    return clipped_parcels, tricog_geo_path_cell_two, tricog_text_path_cell_two


@app.cell(hide_code=True)
def tricog_path_cell_2(
    CLIPPED_PARCELS_IMG_PATH,
    assessments_df,
    clip_function_parcel_length_code,
    countywide_municipality_name_list,
    mo,
    tricog_geo_path_cell_two,
    tricog_geo_path_clip_function_parcel_length,
    tricog_text_path_box_countywide_muni_name_list,
    tricog_text_path_cell_two,
):
    mo.stop(not tricog_text_path_cell_two and not tricog_geo_path_cell_two)
    tricog_text_question_box_two_bool = False
    tricog_geo_question_box_two_bool = False

    if tricog_text_path_cell_two:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""Looking back at the assessments file, we can see a column named "MUNIDESC". That means Municipal Description -- the text name of the municipality that that row's parcel is in."""),
                    assessments_df,
                    mo.md(f"""The size of the spreadsheet makes it hard to get a sense of what the values in that column are. Let's take a look at a de-duplicated list of values from that column. But using three lines of code, we can get a nice, short sample of unique names in the MUNIDESC field. 
                    <br><br>To start, enter the code below and hit 'Submit' to take the first step, which isolates the MUNICDESC column, removes all duplicates, and converts it to a list that we can reorder and subsample. """),
                    mo.md(text=f"""`{countywide_municipality_name_list}`"""),
                    tricog_text_path_box_countywide_muni_name_list,
                ]
            )
        )

        if tricog_text_path_box_countywide_muni_name_list.value: 
            if tricog_text_path_box_countywide_muni_name_list.value == countywide_municipality_name_list: 
                mo.output.replace_at_index('Correct!',1)
                tricog_text_question_box_two_bool = True
            else:
                mo.output.append('Try again!')                
    elif tricog_geo_path_cell_two:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""That did it! Nice work! Unfortunately, the output variable, `clipped_parcels`, is still too large to visualize with the `explore()` function. So how do we know it worked? <br>

                        If you have GIS software, you can output the `clipped_parcels` variable using `geopandas`' `to_file()` command. The argument you would use in the function is the name you want the outputted file to have. Running the command: <br>

            `clipped_parcels.to_file("clipped_parcels_output.geojson")`

            would create a file in your current working directory called `clipped_parcels_output.geojson`. 

            The specifics of doing so are outside the scope of this lesson, but if you were to do so, the output would look like this:"""), 
                    mo.image(CLIPPED_PARCELS_IMG_PATH, width=1248 * .5, height=839 * .5),
                    mo.md(f"""<br>As a rough secondary test, you can check the length of the `clipped_parcels` variable and compare it to the length of the `parcels` variable. If the clip reduced the number of parcels, `clipped_parcels` should have a notably shorter length.<br><br> 
                    The next two code snippets are called f-strings. F-strings allow you to write variable names and have the printout show the variable's value. They always begin with the letter f and are enclosed between a set of apostrophes or quotes. 
                    <br><br>Type the two snippets of code below one at a time to find out the lenght of the parcels file, and the length of our new clipped variable.<br><br>
                    `{clip_function_parcel_length_code}`"""),
                    tricog_geo_path_clip_function_parcel_length,
                ]
            )
        )
        if tricog_geo_path_clip_function_parcel_length.value:
            if tricog_geo_path_clip_function_parcel_length.value == clip_function_parcel_length_code:
                mo.output.replace_at_index("Correct!", 1)
                tricog_geo_question_box_two_bool = True
            else: 
                mo.output.append("Not quite right...try again?")

    else: 
        mo.output.clear()
    return tricog_geo_question_box_two_bool, tricog_text_question_box_two_bool


@app.cell
def tricog_path_cell_2a(
    clip_function_clip_output_length_code,
    clipped_parcels,
    countywide_municipality_name_list_sorted,
    mo,
    parcels_df,
    tricog_geo_path_clip_function_clip_output_length,
    tricog_geo_question_box_two_bool,
    tricog_text_path_box_countywide_muni_name_list_sorted,
    tricog_text_question_box_two_bool,
):
    mo.stop(not tricog_text_question_box_two_bool and not tricog_geo_question_box_two_bool)
    tricog_text_question_box_three_bool = False 
    begin_residential_path = False 

    if tricog_text_question_box_two_bool:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""<br>This piece of code will sort the municipality names, to make sure we're all looking at the same list.<br>Type the code into the box and submit it."""),
                    mo.md(text=f"""`{countywide_municipality_name_list_sorted}`"""), 
                    tricog_text_path_box_countywide_muni_name_list_sorted,
                ],
            )
        )
        if tricog_text_path_box_countywide_muni_name_list_sorted.value: 
            if tricog_text_path_box_countywide_muni_name_list_sorted.value == countywide_municipality_name_list_sorted: 
                mo.output.replace_at_index('Correct!',1)
                tricog_text_question_box_three_bool = True
            else:
                mo.output.append('Try again!')
    elif tricog_geo_question_box_two_bool:
        mo.output.replace(
            mo.vstack( 
                [
                    mo.md(f"""`{clip_function_clip_output_length_code}`"""),
                    tricog_geo_path_clip_function_clip_output_length,
                ]
            )
        )
        if tricog_geo_path_clip_function_clip_output_length.value:
            if tricog_geo_path_clip_function_clip_output_length.value == clip_function_clip_output_length_code:
                output_to_append = mo.md(f"""Correct!<br><br>length of parcels: `{len(parcels_df)}`<br>
                          length of clipped_parcels: `{len(clipped_parcels)}`""")
                mo.output.replace_at_index(output_to_append, 1)
                begin_residential_path = True
            else: 
                mo.output.append("Try again!")

    else:
        mo.output.clear()
        parcel_length_code = "f''"
        clip_length_code = "f'length of clipped_parcels: {len(clipped_parcels)}'"
    return begin_residential_path, tricog_text_question_box_three_bool


@app.cell
def tricog_path_cell_2b(
    countywide_municipality_name_list_sorted_printed,
    mo,
    tricog_text_path_box_countywide_muni_name_list_sorted_printed,
    tricog_text_question_box_three_bool,
    tricog_text_question_box_two_bool,
):
    mo.stop(not tricog_text_question_box_three_bool)
    tricog_text_path_cell_three = False

    if tricog_text_question_box_two_bool:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""<br>The complete list of unique municipalities in Allegheny County is around 150 items long. We're just trying to get a sense of what the code includes, so let's only look at some of them. The following text will only provide the first 20 names in the list.<br><br> Once again, type out the code and hit 'Submit'"""),
                    mo.md(text=f"""`{countywide_municipality_name_list_sorted_printed}`"""), 
                    tricog_text_path_box_countywide_muni_name_list_sorted_printed,
                ],
            )
        )
        if tricog_text_path_box_countywide_muni_name_list_sorted_printed.value: 
            if tricog_text_path_box_countywide_muni_name_list_sorted_printed.value == countywide_municipality_name_list_sorted_printed: 
                mo.output.replace_at_index('Correct!',1)
                tricog_text_path_cell_three = True
            else:
                mo.output.append('Try again!')
    else:
        mo.output.clear()
    return (tricog_text_path_cell_three,)


@app.cell
def _(geo_analysis_btn, mo, munis, tricog_text_path_cell_three):
    mo.stop(not tricog_text_path_cell_three)

    if tricog_text_path_cell_three: 
        mo.output.replace(
            mo.vstack(
                [
                    munis[:20],
                    mo.md(f"""Looking at the first twenty municipalities in order, things look a little unusual. The labels seem to contain municipal names, but they also contain ward numbers. The municipal names are also in all caps (and the municipal names from `tricog` were not).  

        These are things we _could_ attempt to standardize between the two dataframes, but this many discrepancies in the first 20 results could suggest that there are additional discrepancies in the rest of the list. 

        Trying a geospatial analysis might be quicker and more straightforward. Click the button below to try that!"""),
                    geo_analysis_btn
                ]
            )
        )
    # elif geo_flag:
    #     pass
    else: 
        mo.output.clear()


    return


@app.cell
def residential_prep(mo):
    #residential path prep

    #code_snippets
    filter_on_classdesc = "assessments_df[assessments_df['CLASSDESC']=='RESIDENTIAL']"
    residential_classdesc_and_usedesc_code_snippet = "residential_parcels = assessments_df[(assessments_df['CLASSDESC']=='RESIDENTIAL') & (assessments_df['USEDESC']=='SINGLE FAMILY')]"

    #buttons
    residential_start_button = mo.ui.run_button(label="Push to Start")

    #text_boxes
    residential_text_box_parcel_class_descriptions = mo.ui.text(full_width=True).form(clear_on_submit=True)
    residential_text_box_only_classdesc_value_residential = mo.ui.text(full_width=True).form(clear_on_submit=True)
    residential_text_box_final_classdesc_usedesc_filter = mo.ui.text(full_width=True).form(clear_on_submit=True)

    #chat variable
    response_message = "I'm glad you asked! The assessments file is very large and confusing. You'll want to find parcels where the CLASSDESC value is 'Residential' and the USEDESC value is 'Single Family'."

    return (
        filter_on_classdesc,
        residential_classdesc_and_usedesc_code_snippet,
        residential_start_button,
        residential_text_box_final_classdesc_usedesc_filter,
        residential_text_box_only_classdesc_value_residential,
        residential_text_box_parcel_class_descriptions,
        response_message,
    )


@app.cell
def residential_path_cell_0(
    begin_residential_path,
    mo,
    residential_start_button,
):
    mo.stop(not begin_residential_path)
    residential_path_one = False
    if begin_residential_path: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""##Ready to begin looking for residential parcels?""").center(),
                    mo.md(f"""Click the button below...""").center(),
                    residential_start_button.center()
                ]
            )
        )
        residential_path_one = residential_start_button.value
    else: 
        mo.output.clear()
    return (residential_path_one,)


@app.cell
def residential_path_cell_1(
    assessments_df,
    mo,
    residential_path_one,
    residential_text_box_parcel_class_descriptions,
):
    mo.stop(not residential_path_one)
    residential_path_two = False

    if residential_path_one:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""###Finding Residential Parcels"""),
                    mo.md(f"""Another important factor in finding suitable parcels for consideration is to find residential parcels. Local governments categorize parcels into different categories: residential (e.g. homes), commercial (e.g. stores), industrial (e.g. steel furnaces), and more.<br><br>

        This seems like the sort of information that would be contained in the `assessments` file: remember, that file contains descriptive elements about the parcels in the county.<br><br> 

        But there are 85 columns in the dataframe, and most columns have numerous values across the 585,000 rows. How do we know which columns contain the information we're looking for? How do we know we've found all of the relevant rows and values?<br><br>

        Let's take a quick look at the `assessments` dataframe again."""),
                assessments_df,
                mo.md(f"""If you scroll to the right, you'll notice that the column CLASSDESC has several 'COMMERCIAL' values in the first few rows. Commercial was one of the classification types that was briefly mentioned during the introduction, so that column may hold the key. Let's isolate that column and look at the unique values.<br>

                Type the following code into the box below and press 'Submit' to view the unique set of values in the CLASSDESC column.<br>
                `set(assessments_df.CLASSDESC)`"""),
                residential_text_box_parcel_class_descriptions
                ]
            )
        )
        if residential_text_box_parcel_class_descriptions.value:
            if residential_text_box_parcel_class_descriptions.value == "set(assessments_df.CLASSDESC)":
                classdesc_values = set(assessments_df.CLASSDESC)
                mo.output.replace_at_index("Correct!", 1)
                residential_path_two = True
            else: 
                mo.output.append("Sorry, please try again!")

    return classdesc_values, residential_path_two


@app.cell
def residential_path_cell_2(
    assessments_df,
    classdesc_values,
    filter_on_classdesc,
    mo,
    residential_path_two,
    residential_text_box_only_classdesc_value_residential,
):
    mo.stop(not residential_path_two)
    residential_path_three = False

    if residential_path_two:
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""Here's the output that our previous line of code generated:<br> 
                    `{classdesc_values}`<br>
                    Look closely at that output: one of those values is 'RESIDENTIAL'!<br><br>
                    Let's see what happens when we filter the dataset so it only contains rows where the value in the CLASSDESC column is 'RESIDENTIAL'.<br><br>
                    Type the following code into the text box to filter the dataframe on "RESIDENTIAL"<br>
                    `{filter_on_classdesc}`"""),
                    residential_text_box_only_classdesc_value_residential,                
                ]
            )
        )
        if residential_text_box_only_classdesc_value_residential.value:
            if residential_text_box_only_classdesc_value_residential.value == filter_on_classdesc:
                mo.output.replace_at_index("Correct!", 1),
                assessments_df_classdesc = assessments_df[assessments_df['CLASSDESC']=='RESIDENTIAL']
                residential_path_three = True
            else: 
                mo.output.append("Try again!")
    else: 
        mo.output.clear()
    return assessments_df_classdesc, residential_path_three


@app.cell
def residential_path_3(assessments_df_classdesc, mo, residential_path_three):
    mo.stop(not residential_path_three)
    residential_path_four = False

    if residential_path_three:
        mo.output.replace(
            mo.vstack(
                [
                    assessments_df_classdesc,
                    mo.md(f"""If we scroll over to the CLASSDESC column, it appears to be entirely populated by the value 'RESIDENTIAL'. But is this what we're looking for? The guidelines above said we were looking for single-family homes; are all of these residential properties single-family?<br><br>
                    With this much uncertainty, it might be best to ask a `clarifying question`.<br><br>

                    We've set up a connection for you to your supervisor at TriCOG using their internal chat client. Ask your supervisor `which filters should be used to find suitable residential properties`? (You can also type "/" to have the question filled in as a prompt.)""")
                ]
            )
        )
    return


@app.cell
def _(mo):
    get_residential_post_chat_move_on, set_residential_post_chat_move_on = mo.state(False)
    return get_residential_post_chat_move_on, set_residential_post_chat_move_on


@app.cell
def residential_path_chat(
    mo,
    residential_path_three,
    response_message,
    set_residential_post_chat_move_on,
):
    mo.stop(not residential_path_three)
    prompts = ["Which filters should be used to find residential properties?"]
    responses = []

    def residential_parcel_chat_session(messages):
        if len(responses)==0 and (messages[-1].content.lower()=='hi' or 'hello' in messages[-1].content.lower()):
            responses.append("Hi! What's up?")
            return responses[-1]
        for appreciation in ['thanks', 'thank you']:
            if appreciation in messages[-1].content.lower():
                responses.append("You're welcome!")
                return responses[-1]
        if response_message in responses:
            set_residential_post_chat_move_on(True)
            responses.append("I'm sorry, I'm a bit busy. Did that answer your question? Look for CLASSDESC=='RESIDENTIAL' and USEDESC=='SINGLE FAMILY'")
            return responses[-1]
        if response_message not in responses: 
            responses.append(response_message)
            set_residential_post_chat_move_on(True)
        return response_message

    chat = mo.ui.chat(residential_parcel_chat_session, prompts=prompts)
    chat
    return


@app.cell
def residential_path_four(
    assessments_df,
    get_residential_post_chat_move_on,
    mo,
    residential_classdesc_and_usedesc_code_snippet,
    residential_text_box_final_classdesc_usedesc_filter,
):
    residential_post_chat_move_on = get_residential_post_chat_move_on()

    mo.stop(not residential_post_chat_move_on)
    residential_path_five = False 

    if residential_post_chat_move_on: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""Great! Now that you know which values to use, let's go find the parcels. We can combine both of these conditions into one statement to be more straightforward.<br><br>

                    Type the following code into the text box.<br>
                    `{residential_classdesc_and_usedesc_code_snippet}`"""),
                    residential_text_box_final_classdesc_usedesc_filter
                ]
            )
        )
        if residential_text_box_final_classdesc_usedesc_filter.value:
            if residential_text_box_final_classdesc_usedesc_filter.value == residential_classdesc_and_usedesc_code_snippet:
                residential_parcels = assessments_df[(assessments_df['CLASSDESC']=='RESIDENTIAL') & (assessments_df['USEDESC']=='SINGLE FAMILY')]
                mo.output.replace_at_index("Correct!", 1)
                residential_path_five = True
            else:
                mo.output.append("Sorry, please try again")
    else:
        mo.output.clear()
    return residential_parcels, residential_path_five


@app.cell(hide_code=True)
def residential_path_5(
    abandoned_begin_button,
    mo,
    residential_parcels,
    residential_path_five,
):
    mo.stop(not residential_path_five)
    abandoned_path_zero = False 
    if residential_path_five:
        mo.output.replace(
            mo.vstack(
                [
                    residential_parcels,
                    mo.md(f"""That looks correct! I think we've got it. But if you wanted to perform a check on your own, the way to do that would be to reuse the `set()` function we've used before to generate a list of unique values amongst given data. <br><br>
                    In this instance, the code would look like this: `set(residential_parcels.USEDESC)`<br><br>
                    Running that would give you the following output: <br>
                    `set(residential_parcels.USEDESC): {set(residential_parcels.USEDESC)}`<br><br>"""),

                    mo.md(f"""##Ready to move on and look into finding abandoned properties? Click the button below!""").center(),
                    abandoned_begin_button.center()
                ]
            )
        )
        abandoned_path_zero = abandoned_begin_button.value
    else:
        mo.output.clear()
    return (abandoned_path_zero,)


@app.cell
def _(mo):
    get_abandoned_iteration_path_1, set_abandoned_iteration_path_1 = mo.state(False)
    get_abandoned_join_path_1, set_abandoned_join_path_1 = mo.state(False)
    return (
        get_abandoned_iteration_path_1,
        get_abandoned_join_path_1,
        set_abandoned_iteration_path_1,
        set_abandoned_join_path_1,
    )


@app.cell
def abandoned_path_prep(
    mo,
    set_abandoned_iteration_path_1,
    set_abandoned_join_path_1,
):
    #abandoned section prep

    #buttons
    abandoned_begin_button = mo.ui.run_button(label="Begin")

    #code snippets
    parcels_with_liens = "parcels_df_with_liens = parcels_df[parcels_df['PIN'].isin(list(liens_df.pin))]"
    abandoned_pd_merge_code_snippet = "pd.merge(left=parcels_df, right=liens_df, left_on='PIN', right_on='pin', how='inner')"
    abandoned_iteration_generate_empty_lien_column_code_snippet = "parcels_df_with_liens = parcels_df_with_liens.assign(lien_amount='')"
    abandoned_iteration_iteration_code_block_no_spaces = "for idx, row in parcels_df_with_liens.iterrows(): amount = liens_df[liens_df['pin']==row.PIN].total_amount.values[0] parcels_df_with_liens.at[idx, 'lien_amount']= amount"
    abandoned_iteration_iteration_code_block_with_spaces = "for idx, row in parcels_df_with_liens.iterrows():`<br>            &nbsp;&nbsp;&nbsp;&nbsp;`amount = liens_df[liens_df['pin']==row.PIN].total_amount.values[0]`<br>            &nbsp;&nbsp;&nbsp;&nbsp;`parcels_df_with_liens.at[idx, 'lien_amount']= amount"

    #text boxes
    abandoned_iteration_text_box_parcels_with_liens = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_join_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_iteration_text_box_adding_lien_column = mo.ui.text(full_width=True).form(clear_on_submit=True)
    abandoned_iteration_text_box_code_block = mo.ui.text_area(full_width=True).form(clear_on_submit=True)

    #other
    miscellany = {'iteration_move_along': False}


    def handle_abandoned_path_selection(value):   
        if (value == "JOIN"):
            set_abandoned_join_path_1(True)
            set_abandoned_iteration_path_1(False)
            return "JOIN"
        if (value == "ITERATION"):
            set_abandoned_iteration_path_1(True)
            set_abandoned_join_path_1(False)
            return "ITERATION"

    abandoned_iteration_button = mo.ui.button(
        label="Iteration", 
        value="ITERATION", 
        on_click=handle_abandoned_path_selection
    )
    abandoned_join_button = mo.ui.button(
        label="Join", 
        value="JOIN", 
        on_click=handle_abandoned_path_selection
    )
    return (
        abandoned_begin_button,
        abandoned_iteration_button,
        abandoned_iteration_generate_empty_lien_column_code_snippet,
        abandoned_iteration_iteration_code_block_no_spaces,
        abandoned_iteration_text_box_adding_lien_column,
        abandoned_iteration_text_box_code_block,
        abandoned_iteration_text_box_parcels_with_liens,
        abandoned_join_button,
        abandoned_join_text_box,
        abandoned_pd_merge_code_snippet,
        parcels_with_liens,
    )


@app.cell(hide_code=True)
def abandoned_path_0(
    abandoned_iteration_button,
    abandoned_join_button,
    abandoned_path_zero,
    get_abandoned_iteration_path_1,
    get_abandoned_join_path_1,
    liens_df,
    mo,
):
    mo.stop(not abandoned_path_zero)
    abandoned_iteration_path_1 = get_abandoned_iteration_path_1()
    abandoned_join_path_1 = get_abandoned_join_path_1()

    if abandoned_path_zero: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""##Finding Abandoned Properties"""),
                    mo.md(f"""In this section, we're trying to find homes that have been abandoned. This can be difficult to do using data because there is no registry of abandoned homes in the county. We'll have to use a different dataset as a proxy for abandoned homes. 

        This is where tax delinquent property data comes in. Remember that tax delinquency is when an individual stops paying taxes. If a person has stopped paying taxes on their house, it's possible that they're having money problems. But it's also possible that it is a sign they have decided to abandon the property.

        This step again highlights one of the challenges of working with geospatial data: some datasets contain geospatial data, while other datasets will only contain text-based data about the same locations. 

        This is another one of those instances. In order to find homes that may be abandoned, we'll have to combine geospatial data and text-based data.<br><br>

        Let's take another look at the tax liens summary file."""),
                    liens_df,
                    mo.md(f"""The dataset is fairly easy to interpret, thanks to the small number of columns. The dataset contains an ID row, the parcel ID Number ('pin'), the number of liens against the property ('number'), and the total amount owed in taxes ('total_amount'). 

                In order to make use of this data, we'll have to connect the `pin` column to the `pin` column in our other files. There are a few ways we could do this. We could do this by **iterating** over the datasets and combining them when the field matches, or we could perform a **join.** 

                Which would you like to try?"""),
                    mo.hstack([abandoned_iteration_button, abandoned_join_button],justify='space-around')
                ]
            )
        )
    else: 
        mo.output.clear()

    return abandoned_iteration_path_1, abandoned_join_path_1


@app.cell(hide_code=True)
def abandoned_path_1(
    abandoned_iteration_path_1,
    abandoned_iteration_text_box_parcels_with_liens,
    abandoned_join_path_1,
    abandoned_join_text_box,
    abandoned_pd_merge_code_snippet,
    liens_df,
    mo,
    parcels_df,
    parcels_with_liens,
    pd,
):
    mo.stop(not abandoned_iteration_path_1 and not abandoned_join_path_1)
    abandoned_iteration_path_2 = False
    abandoned_join_path_2 = False

    if abandoned_iteration_path_1: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""###Iteration"""),
                    mo.md(f"""One way to approach this task is to iterate over the data.<br><br> 

                First, we can isolate the rows from our parcels file that have liens against them. We can do this by selecting the rows where the parcel ID number is in both files. `pandas` has a line of code that can do that quickly for us.<br><br>
                Type the following code into the box and press 'Submit'<br>`{parcels_with_liens}`"""), 
                    abandoned_iteration_text_box_parcels_with_liens,
                ]
            )
        )
        if abandoned_iteration_text_box_parcels_with_liens.value:
            if abandoned_iteration_text_box_parcels_with_liens.value == parcels_with_liens: 
                mo.output.replace_at_index("Correct!", 1)
                parcels_df_with_liens_iteration = parcels_df[parcels_df['PIN'].isin(list(liens_df.pin))]
                abandoned_iteration_path_2 = True 
            else:
                mo.output.append("Please try again")
    elif abandoned_join_path_1: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""###Joins"""),
                    mo.md(f"""A fast way to complete this task is to use a join. A join is a command that combines ("joins") two datasets. The output from a join is a new dataset that has all of the columns from both input datasets (unless you specify you only want some of the columns). 

        The two datasets are "joined" on a column that will have the same values in both datasets. In the files we've been given, the parcel ID numbers appear across multiple datasets. We can use those columns to join the various datasets together and see all of the information about these parcels in one place. 

        Types of joins include left, inner, and right joins. 

        One way to think about the types of joins is to think about folding socks. Any time you wash socks, you need to pair them up and put them away. But it's easy for socks to get lost in the process, so you might have some left and right socks that no longer have a mate. If you were to perform an inner join on your socks, you would only keep socks that still form a pair. A left join on the socks would mean you keep all of the matches as well as any left sock that's lost its match. A right join would mean you keep all of the matched socks, as well as all of the right socks that have lost their mate. 

        With data, an inner join returns a dataframe that only contains rows where there was a match on your specified column. Left joins would return all rows from the "left" dataframe; matched rows will have the data from the "right" dataframe, and the other rows will have null values in those columns. Right joins return the opposite: all rows from the "right" dataframe are returned, and matched rows will contain the data from the "left" dataframe. 

        For this join, we'll use the pandas command `pd.merge()`. The dataframes will be parcels and summary_of_liens. We'll use an inner join because we only need location data returned for parcels if they have a lien against them.<br><br>

        Type in the following code and press submit to perform the join.<br>
        `{abandoned_pd_merge_code_snippet}`"""),
                    abandoned_join_text_box,
                ]
            )
        )
        if abandoned_join_text_box.value:
            if abandoned_pd_merge_code_snippet == abandoned_join_text_box.value:
                parcels_df_with_joined_liens = pd.DataFrame(pd.merge(left=parcels_df, right=liens_df, left_on='PIN', right_on='pin', how='inner'))
                mo.output.replace_at_index("Correct!", 1)
                abandoned_join_path_2 = True
            else: 
                mo.output.append("Please try again!")
    else:
        mo.output.clear()
    return (
        abandoned_iteration_path_2,
        abandoned_join_path_2,
        parcels_df_with_joined_liens,
        parcels_df_with_liens_iteration,
    )


@app.cell(hide_code=True)
def _(
    abandoned_iteration_generate_empty_lien_column_code_snippet,
    abandoned_iteration_path_2,
    abandoned_iteration_text_box_adding_lien_column,
    abandoned_join_path_2,
    mo,
    parcels_df_with_joined_liens,
    parcels_df_with_liens_iteration,
):
    mo.stop(not abandoned_iteration_path_2 and not abandoned_join_path_2)
    abandoned_iteration_path_3 = False
    combining_files_path_0 = False

    if abandoned_iteration_path_2: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""Now we have a dataframe filled with parcels that have liens against them. The only problem is, we don't have any of the data from the liens dataframe. Let's iterate over the two dataframes.

                First, we'll add a column to our parcels slice dataframe to hold the lien amount.<br><br>
                Type the following code into the box below and press 'Submit': <br>
                `{abandoned_iteration_generate_empty_lien_column_code_snippet}`
                """),
                    abandoned_iteration_text_box_adding_lien_column
                ]
            )
        )
        if abandoned_iteration_text_box_adding_lien_column.value:
            if abandoned_iteration_text_box_adding_lien_column.value == abandoned_iteration_generate_empty_lien_column_code_snippet: 
                parcels_df_with_liens_iteration_2 = parcels_df_with_liens_iteration.assign(lien_amount='')
                mo.output.replace_at_index("Correct!", 1)
                abandoned_iteration_path_3 = True

    elif abandoned_join_path_2:
        mo.output.replace(
            mo.vstack(
                [
                    parcels_df_with_joined_liens,
                    mo.md(f"""You can see above that your statement returned a smaller dataframe that has all of the columns from both the parcels dataframe and the liens dataframe. Well done!""")
                ]
            )
        )
        combining_files_path_0 = True
    else:
        mo.output.clear()
    return (
        abandoned_iteration_path_3,
        combining_files_path_0,
        parcels_df_with_liens_iteration_2,
    )


@app.cell(hide_code=True)
def _(
    abandoned_iteration_iteration_code_block_no_spaces,
    abandoned_iteration_path_3,
    abandoned_iteration_text_box_code_block,
    abandoned_join_button,
    liens_df,
    mo,
    parcels_df_with_liens_iteration_2,
    pd,
    time,
):
    mo.stop(not abandoned_iteration_path_3)

    abandoned_iteration_path_4 = False
    def fake_iteration(): 
        mo.output.append("Iteration has begun...")
        seconds_counter = 0
        next_out = 10
        start_time = time.time()
        for _idx, _row in parcels_df_with_liens_iteration_2.iterrows():
            amount = liens_df[liens_df['pin']==_row.PIN].total_amount.values[0]
            parcels_df_with_liens_iteration_2.at[_idx, 'lien_amount']= amount
            seconds_counter = time.time() - start_time
            if seconds_counter > next_out: 
                mo.output.append(f'{seconds_counter:.0f} seconds have passed...')
                next_out += 10
            if seconds_counter > 40: 
                break

    if abandoned_iteration_path_3: 
        mo.output.replace(
            mo.vstack(
                [
                    pd.DataFrame(parcels_df_with_liens_iteration_2),
                    mo.md(f"""Here is the output from the code you just entered. If you scroll to the last column of the dataframe, you can see that the 'lien_amount' column has been added. Now we can begin the work of iterating through the dataframe and adding the lien amounts to the dataframe.<br><br>
                    Type the following rows of text into the text entry box below and press 'Submit' and watch the output while it processes.<br><br>
                `for idx, row in parcels_df_with_liens.iterrows():`<br>
                &nbsp;&nbsp;&nbsp;&nbsp;`amount = liens_df[liens_df['pin']==row.PIN].total_amount.values[0]`<br>
                &nbsp;&nbsp;&nbsp;&nbsp;`parcels_df_with_liens.at[idx, 'lien_amount']= amount`"""),
                abandoned_iteration_text_box_code_block
                ]
            )
        )
        if abandoned_iteration_text_box_code_block.value:
            if strip_string(abandoned_iteration_text_box_code_block.value) == strip_string(abandoned_iteration_iteration_code_block_no_spaces): 
                mo.output.replace_at_index("Correct!", 1)
                fake_iteration()
                mo.output.append(
                    mo.vstack(
                        [
                            mo.md(f"""Sorry, but I stopped that function -- it was taking too long! Surely there's a faster way. Let's try using a join to see how long that takes.

                Click the button below to look at joins."""),
                            abandoned_join_button
                        ]
                    )
                )
            else: 
                mo.output.append("Try again!")
    return


@app.cell
def _(mo):
    #combining files prep

    #code snippets
    combining_path_clipped_and_single_family_join = "clipped_and_residential = pd.merge(left=clipped_parcels,                                          right=residential_parcels[['PARID', 'CLASSDESC', 'USEDESC']], left_on='PIN', right_on='PARID')"
    combining_path_final = "final_output = pd.merge(left=clipped_and_residential, right=parcels_df_with_joined_liens[['PIN', 'total_amount']], left_on='PIN', right_on='PIN')"

    #text boxes
    combining_path_text_box_clipped_and_residential = mo.ui.text(full_width=True).form(clear_on_submit=True)
    combining_final_text_box = mo.ui.text(full_width=True).form(clear_on_submit=True)
    return (
        combining_final_text_box,
        combining_path_clipped_and_single_family_join,
        combining_path_final,
        combining_path_text_box_clipped_and_residential,
    )


@app.cell(hide_code=True)
def _(
    clipped_parcels,
    combining_files_path_0,
    combining_path_clipped_and_single_family_join,
    combining_path_text_box_clipped_and_residential,
    mo,
    pd,
    residential_parcels,
):
    mo.stop(not combining_files_path_0)
    combining_files_path_1 = False

    if combining_files_path_0: 
        mo.output.replace(
            mo.vstack(
                [
                    mo.md(f"""##Combining the Data"""),
                    mo.md(f"""We now have three datasets, and each dataset meets one of the criteria set forth by TriCOG land bank. To get our final result, we need to combine them so our final dataframe only has parcels that meet all three criteria. 

        We can manage this using the joins that we learned about while looking for abandoned properties.

        First, let's perform an inner join to find the parcels within TriCOG's boundaries (`clipped_parcels`) and the residential, single-family home parcels in the county (`residential_assessments`).<br><br>
        Type the following code into the box below and hit 'submit'.<br>
        `{combining_path_clipped_and_single_family_join}`"""),
                    combining_path_text_box_clipped_and_residential
                ]
            )
        )
        if combining_path_text_box_clipped_and_residential.value:
            if strip_string(combining_path_text_box_clipped_and_residential.value) == strip_string(combining_path_clipped_and_single_family_join): 
                clipped_and_residential = pd.merge(left=clipped_parcels,                                          right=residential_parcels[['PARID', 'CLASSDESC', 'USEDESC']], left_on='PIN', right_on='PARID')
                mo.output.replace_at_index("Correct!", 1)
                combining_files_path_1 = True
            else:
                mo.output.append("Try again!")
    else:
        mo.output.clear()

    return clipped_and_residential, combining_files_path_1


@app.cell
def _(
    clipped_and_residential,
    combining_files_path_1,
    combining_final_text_box,
    combining_path_final,
    mo,
    parcels_df_with_joined_liens,
    pd,
):
    mo.stop(not combining_files_path_1)
    reflections = False

    if combining_files_path_1:
        mo.output.replace(
            mo.vstack(
                [
                    pd.DataFrame(clipped_and_residential),
                    mo.md(f"""Great! Now we can join the `clipped_and_residential` dataframe with the `parcels_df_joined_liens` dataframe to give us our final list.<br><br>

                    Type this last bit of code into the box below and you should be set!<br>
                    `{combining_path_final}`"""),
                    combining_final_text_box
                ]
            )
        )
        if combining_final_text_box.value: 
            if combining_final_text_box.value == combining_path_final: 
                final_output = pd.merge(left=clipped_and_residential, right=parcels_df_with_joined_liens[['PIN', 'total_amount']], left_on='PIN', right_on='PIN')
                mo.output.replace_at_index("Correct!", 1)
                reflections = True
            else: 
                mo.output.append("Almost there! Try again!")
    return final_output, reflections


@app.cell
def _(final_output, mo):
    #reflections prep

    lien_slider = mo.ui.slider.from_series(final_output['total_amount'], stop=10000, label="Lien Cutoff Amount")
    return (lien_slider,)


@app.cell
def _(final_output, lien_slider, mo, pd, reflections):
    mo.stop(not reflections)

    if reflections:
        mo.output.replace(
            mo.vstack(
                [

                    pd.DataFrame(final_output.astype({'geometry':'str'})),
                    mo.md(f"""##Reflections"""),
                    mo.md(f"""After much work, we have arrived at this dataframe.<br><br> 
                    One of the difficult questions of working with large data is knowing whether or not an end product is correct. Take this dataframe, for example: is this output what we were looking for? Does it contain only properties that meet the stated requirements?<br><br>
                    Perhaps counterintuitively, these are two distinct questions. The values within the output dataframe do meet the requirements -- they are all parcels within TriCOG's operating boundaries that are single-family homes with liens against them. This may not be what we were looking for, though. <br><br>
                    Remember that we are trying to identify abandoned properties, and we are using tax liens as a proxy. However, liens can be assessed against a property for a number of reasons (not just abandonment). Take a look at the range of lien values: the lowest lien amount in the datafram is `${list(final_output.total_amount.sort_values())[0]}.` This hardly feels like the result of abandonment; it could just be clerical or human error instead.

                    Take a look at the slider below. The slider adjusts the amount we consider as the lower-bound lien amount for considering that a house is possibly "abandoned". As we move the slider, we can see how this impacts the total number of houses that would be included in our output dataframe. Try it for yourself; move the slider to various amounts and look at how many houses remain at that level. """),
                    lien_slider.center(),
                    mo.md(f"""Lowest Allowable Amount: ${lien_slider.value:.02f}<br>
                    Number of Properties above Lien Threshhold: {len(final_output[final_output["total_amount"] > lien_slider.value])}""").center(),
                    mo.md(f"""<br><br>Note that as we adjust the slider to around $1000, we've already eliminated roughly 3,000 houses from consideration. And while you would eventually realize the houses were not abandoned if you actually attempted to purchase them, the act of doing so could create stress for individuals and make them feel as if their housing is insecure. The role of your organizaiton is to find homes for people and build community; making people feel uncertain about their current housing goes against the broader work you're trying to do. <br><br>
                    It would be impossible to come up with a dataframe that reflects the real world housing situation 100% accurately, so an important task of yours is to consider what distortions and tradeoffs are being made to represent the real world as data, and how to balance those tradeoffs while creating the least amount of harm.""")
                ]
            )
        )
    return


if __name__ == "__main__":
    app.run()
