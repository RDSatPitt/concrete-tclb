

import marimo

__generated_with = "0.13.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import geopandas

    all_parcels = geopandas.read_file("data/alleghenycounty_parcels202504.geojson")
    all_parcels = all_parcels.set_index('PIN')
    return all_parcels, geopandas


@app.cell
def _():
    import pandas as pd
    tax_delinquency = pd.read_csv("https://data.wprdc.org/datastore/dump/ed0d1550-c300-4114-865c-82dc7c23235b")
    tax_delinquency = tax_delinquency.set_index("pin")
    tax_delinquency
    return (tax_delinquency,)


@app.cell
def _(all_parcels, tax_delinquency):
    delinquent = all_parcels.join(tax_delinquency, how='inner')
    delinquent = delinquent[delinquent['prior_years'] > 2]
    delinquent
    return (delinquent,)


@app.cell
def _(geopandas):
    mva = geopandas.read_file("data/pitts_allegheny_mva2021.zip")
    mva = mva[mva["MVA21"] != "NC"]
    return (mva,)


@app.cell
def _(mva):
    mva.explore(
        column="MVA21",
        cmap="Blues",
        style_kwds={"fillOpacity": 0.8},
        tooltip="MVA21"
    )
    return


@app.cell
def _(mva):
    target_mvas = mva[mva['MVA21'].isin(['D', 'E', 'F'])]
    target_mvas.explore()
    return (target_mvas,)


@app.cell
def _():
    DELINQUENCY_LIMIT = 1000 # dollars
    TIME_LIMIT = 10 # years
    return DELINQUENCY_LIMIT, TIME_LIMIT


@app.cell
def _(DELINQUENCY_LIMIT, TIME_LIMIT, delinquent, target_mvas):
    target_delinquent = delinquent.sjoin(target_mvas, how="inner")
    target_delinquent = target_delinquent[target_delinquent["current_delq_tax"] > DELINQUENCY_LIMIT]
    target_delinquent = target_delinquent[target_delinquent["prior_years"] > TIME_LIMIT]
    return (target_delinquent,)


@app.cell
def _(target_delinquent):
    len(target_delinquent)
    return


@app.cell
def _(target_delinquent):
    target_delinquent.explore(
        tiles="cartodb positron", 
        column="current_delq_tax",
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Fix color ramp.""")
    return


@app.cell
def _(target_delinquent):
    target_delinquent.explore(
        tiles="cartodb positron", 
        column="current_delq_tax",
        scheme="JenksCaspallForced",
        tooltip=['PIN', 'current_delq_tax', 'prior_years']
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Lets look at a histogram of values to get a better idea of what scheme to use.""")
    return


@app.cell
def _(target_delinquent):
    target_delinquent['current_delq_tax'].plot.hist(bins=20)
    return


@app.cell
def _(target_delinquent):
    target_delinquent['prior_years'].plot.hist(bins=5)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
