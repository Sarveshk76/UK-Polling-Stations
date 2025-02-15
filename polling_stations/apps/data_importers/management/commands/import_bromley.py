from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "BRY"
    addresses_name = (
        "2022-05-05/2022-03-18T16:48:00.459690/Democracy_Club__05May2022 BROMLEY.tsv"
    )
    stations_name = (
        "2022-05-05/2022-03-18T16:48:00.459690/Democracy_Club__05May2022 BROMLEY.tsv"
    )
    elections = ["2022-05-05"]
    csv_encoding = "windows-1252"
    csv_delimiter = "\t"
