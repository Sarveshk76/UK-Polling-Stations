from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "WLI"
    addresses_name = (
        "2023-05-04/2023-03-02T08:28:35.838932/Democracy_Club__04May2023.tsv"
    )
    stations_name = (
        "2023-05-04/2023-03-02T08:28:35.838932/Democracy_Club__04May2023.tsv"
    )
    elections = ["2023-05-04"]
    csv_encoding = "windows-1252"
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "100061614139",  # KINGSLEY, CATTESHALL LANE, GODALMING
            "10034686366",  # THE COTTAGE, LAUGHTON WOOD CORNER, LAUGHTON, GAINSBOROUGH
            "10034686362",  # PINE VIEW COTTAGE, LAUGHTON WOOD CORNER, LAUGHTON, GAINSBOROUGH
            "100030955999",  # ELLERS FARM, BLYTON CARR, GAINSBOROUGH
            "100032029197",  # EAST LODGE, THE BELT ROAD, GAINSBOROUGH
            "10034697585",  # THORNOCK GROVE FARM COTTAGE, THE BELT ROAD, GAINSBOROUGH
            "100032029197",  # EAST LODGE, THE BELT ROAD, GAINSBOROUGH
            "10013815969",  # WEST VIEW FARM, STOW PARK, LINCOLN
            "10090696854",  # HORIZON BARN, BULLY HILL TOP, TEALBY, MARKET RASEN
            "200001151020",  # HILL CREST, BULLY HILL TOP, TEALBY, MARKET RASEN
            "10013810973",  # WOLD VIEW HOUSE, BULLY HILL TOP, TEALBY, MARKET RASEN
            "200001151019",  # HAZE HIGH, BULLY HILL TOP, TEALBY, MARKET RASEN
            "10013811352",  # SPRINGFIELD, BLEASBY MOOR, MARKET RASEN
            "10013811351",  # THE SANCTUARY, BLEASBY MOOR, MARKET RASEN
            "10013810009",  # INGS FARM, TOFT NEXT NEWTON, MARKET RASEN
            "10034701979",  # NETTLETON GAP, MOORTOWN ROAD, NETTLETON, MARKET RASEN
            "10013809476",  # SWINTHORPE HOUSE, SNARFORD, MARKET RASEN
            "100030954683",  # WEST WHARTON FARM, MILL LANE, MORTON, GAINSBOROUGH
            "10013809617",  # GREENFIELD HOUSE, LISSINGLEY LANE, LISSINGTON, LINCOLN
            "10013809613",  # LISSINGLEA HOUSE FARM, LISSINGLEY LANE, LISSINGTON, LINCOLN
        ]:
            return None

        if record.addressline6 in ["DN21 1HL", "DN21 1TU", "LN8 3SU", "LN2 3PD"]:
            return None

        return super().address_record_to_dict(record)
